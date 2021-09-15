import os
import re

def is_dummy_line(line):
    return line.startswith('#') or line in ['\n', ' ']

def get_bib_file_paths_in(dir_path):
    file_paths = []
    for file in os.listdir(dir_path):
        if file.endswith(".bib"):
            file_paths.append(os.path.join(dir_path, file))
    return file_paths

def remove_multi_whitespace(line):
    return re.sub(r'\s+', ' ', line)

def remove_keys(string, keys=["[PDF]", "[PPT]", "[SOFTWARE]", "[ACK]"]):
    for key in keys:
        string = string.replace(key, "")
    string = remove_multi_whitespace(string)
    return string

def unicode_quote_to_ascii_quote(line):
    line = re.sub(u'\u201c','"',line)
    line = re.sub(u'\u201d','"',line)
    return line
    
def is_year(string):
    string = string.strip(',').strip('.')
    try:
        year = int(string)
        return 0 < year and year < 2030
    except:
        return False