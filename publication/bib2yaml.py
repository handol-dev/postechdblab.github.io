import os
import yaml
from utils import unicode_quote_to_ascii_quote, remove_multi_whitespace, is_year, get_bib_file_paths_in, is_dummy_line, remove_keys

Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
Months += ['Jan.', 'Feb.', 'Mar.', 'Apr.', 'May.', 'Jun.', 'Jul.', 'Aug.', 'Sep.', 'Oct.', 'Nov.', 'Dec.']

def parse_details(line):
    def remove_key(tmp, key):
        tmp = tmp.replace(key, '')
        return remove_multi_whitespace(tmp).strip()
    KEY_ISSN = '(ISSN:'
    KEY_CORRESPONDING_AUTHOR = '(Corresponding Author)'
    KEY_CO_CORRESPONDING_AUTHOR = '(Co-Corresponding Author)'


    NORMALIZE = True
    if NORMALIZE:
        line = line.replace("Corresponding author", "Corresponding Author")

    sub_template = {
        'is_corresponding_author': False,
        'is_co-corresponding_author': False,
        'year': None,
        'month': None,
        'info': None,
    }
    # Check corresponding author
    if KEY_CO_CORRESPONDING_AUTHOR in line:
        sub_template['is_co-corresponding_author'] = True
        line = remove_key(line, KEY_CO_CORRESPONDING_AUTHOR)
    elif KEY_CORRESPONDING_AUTHOR in line:
        sub_template['is_corresponding_author'] = True
        line = remove_key(line, KEY_CORRESPONDING_AUTHOR)
    
    # Check ISSN number
    if KEY_ISSN in line:
        start_idx = line.index(KEY_ISSN)
        end_idx = start_idx+line[start_idx:].index(')')
        sub_template['ISSN'] = line[start_idx+ len(KEY_ISSN):end_idx].strip()
        line = remove_key(line, line[start_idx:end_idx+1])

    # Year
    toks = line.split(' ')
    for idx, tok in enumerate(toks):
        if tok in Months and is_year(toks[idx+1]):
            sub_template['year'] = int(toks[idx+1].strip('.'))
            month_num = Months.index(tok) % 12 + 1
            sub_template['month'] = Months[month_num+11]
            line = ' '.join(toks[:idx])
            
    if sub_template['year'] is None:
        # if Korean
        if u'년' in line:
        #     sub_template['year'] = toks[-2].strip(',').strip('.')
        #     sub_template['month'] = toks[-1].strip(',').strip('.')
            for idx, tok in enumerate(toks):
                if u'년' in tok:
                    sub_template['year'] = int(tok.strip(',').strip('.')[:-1])
                if u'월' in tok:
                    sub_template['month'] = int(tok.strip(',').strip('.')[:-1])
                if sub_template['year'] and sub_template['month']:
                    line = ' '.join(toks[:idx-1])
                    break
        # else English
        else:
            for idx, tok in enumerate(reversed(toks)):
                if is_year(tok):
                    sub_template['year'] = int(tok.strip(',').strip('.'))
                    line = ' '.join(toks[:-idx-1])
                    break

    sub_template['info'] = line.strip(',').strip(' ')
    return sub_template


def parse_string_to_dic(line):
    template = {
        "title": None,
        "image": None,
        "description": None,
        "authors": None,
        "link": None,
        "ISSN": None,
        "is_corresponding_author": False,
        "is_co-corresponding_author": False,
        "year": None,
        "month": None,
        "info": None,
        "highlight": 0
    }
    cnt = line.count('"')
    assert cnt == 2, f"There should be only one pair of quotations. But found: {cnt}"
    authors, title, etc = line.split('"')
    
    # Parse details
    details = parse_details(etc)
    
    # Add details
    for key, item in details.items():
        assert key in template.keys()
        template[key] = item
    template['authors'] = authors.strip().strip(',')
    template['title'] = title.strip().strip(',')
    return template


if __name__ == "__main__":
    # Get bib files
    bib_paths = get_bib_file_paths_in("./bibs")
    
    # Create dump directory
    if not os.path.exists("./yamls"):
        os.mkdir("./yamls")
    
    # For all bib files
    for file_path in bib_paths:
        dics = []
        # Read in and create dictionary
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = [unicode_quote_to_ascii_quote(line) for line in f.readlines()]
            lines = [remove_keys(line) for line in lines]
            line_cnt = 0
            for line in lines:
                if is_dummy_line(line):
                    line_cnt += 1
                    continue
                try:
                    dics.append(parse_string_to_dic(line))
                except Exception as e:
                    print(e)
                    print(f"Check: {file_path} line: {line_cnt+1}")
                line_cnt += 1
        
        # Dump as yaml
        if line_cnt == len(lines):
            # Change directory
            out_path = file_path.replace("bibs/", "yamls/")
            # Change file extension
            out_path = out_path.replace(".bib", ".yml")
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(yaml.dump(dics, default_flow_style=False, allow_unicode=True))
        else:
            print(f"Skipping: {file_path}\n")

    print("Done!")