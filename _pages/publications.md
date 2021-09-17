---
title: "Database & Data Mining Lab - Publications"
layout: gridlay
excerpt: "Database & Data Mining Lab - Publications."
sitemap: false
permalink: /publications/
---


# Publications

## Group highlights

Please add group highlights

{% assign number_printed = 0 %}
{% for publi in site.data.publist %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if publi.highlight == 1 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
 <div class="well">
  <pubtit>{{ publi.title }}</pubtit>
  <img src="{{ site.url }}{{ site.baseurl }}/images/pubpic/{{ publi.image }}" class="img-responsive" width="33%" style="float: left" />
  <p>{{ publi.description }}</p>
  <p><em>{{ publi.authors }}</em></p>
  <p><strong><a href="{{ publi.link.url }}">{{ publi.link.display }}</a></strong></p>
  <p class="text-danger"><strong> {{ publi.news1 }}</strong></p>
  <p> {{ publi.news2 }}</p>
 </div>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endif %}
{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

<p> &nbsp; </p>

{% assign year_until = 2012%}

## International Journals
{% assign var_year = 2022 %}
{% for publi in site.data.publications.international_journals %}
  {% if var_year != publi.year and var_year > year_until%}
  **{{ publi.year }}** <br />
  {% endif %}
  {% assign var_year = publi.year %}
  **{{ publi.title }}** <br />
  <em>{{ publi.authors }} </em><br />
  {{publi.info}}, {{ publi.month }} {{ publi.year}}
  {% if publi.ISSN != null %} (ISSN: {{publi.ISSN}}){% endif %} {% if publi.is_corresponding_author == true %} (Corresponding Author){% endif %} {% if publi.is_co-corresponding_author == true %} (Co-Corresponding Author){% endif %} {% if publi.link != null %} <a href="{{ publi.link }}">[PDF]</a> {% endif %}

{% endfor %}

## International Conference Proceedings
{% assign var_year = 2022 %}
{% for publi in site.data.publications.international_conference_proceedings %}
  {% if var_year != publi.year and var_year > year_until%}
  **{{ publi.year }}** <br />
  {% endif %}
  {% assign var_year = publi.year %}
  **{{ publi.title }}** <br />
  <em>{{ publi.authors }} </em><br />
  {{publi.info}}, {{ publi.month }} {{ publi.year }}
  {% if publi.ISSN != null %} (ISSN: {{publi.ISSN}}){% endif %} {% if publi.is_corresponding_author == true %} (Corresponding Author){% endif %} {% if publi.is_co-corresponding_author == true %} (Co-Corresponding Author){% endif %} {% if publi.link != null %} <a href="{{ publi.link }}">[PDF]</a> {% endif %}

{% endfor %}

## Others
{% assign var_year = 2022 %}
{% for publi in site.data.publications.others %}
  {% if var_year != publi.year and var_year > year_until%}
  **{{ publi.year }}** <br />
  {% endif %}
  {% assign var_year = publi.year %}
  **{{ publi.title }}** <br />
  <em>{{ publi.authors }} </em><br />
  {{publi.info}}, {{ publi.month }} {{ publi.year }} {% if publi.link != null %}
  <a href="{{ publi.link }}">[PDF]</a>
  {% endif %}

{% endfor %}

## Domestic Journals
{% assign var_year = 2022 %}
{% for publi in site.data.publications.domestic_journals %}
  {% if var_year != publi.year and var_year > year_until%}
  **{{ publi.year }}** <br />
  {% endif %}
  {% assign var_year = publi.year %}
  **{{ publi.title }}** <br />
  <em>{{ publi.authors }} </em><br />
  {{publi.info}}, {{ publi.year }}년 {{ publi.month }}월 {% if publi.link != null %}
  <a href="{{ publi.link }}">[PDF]</a>
  {% endif %}

{% endfor %}


## Domestic Conference Proceedings
{% assign var_year = 2022 %}
{% for publi in site.data.publications.domestic_conference_proceedings %}
  {% if var_year != publi.year and var_year > year_until%}
  **{{ publi.year }}** <br />
  {% endif %}
  {% assign var_year = publi.year %}
  **{{ publi.title }}** <br />
  <em>{{ publi.authors }} </em><br />
  {{publi.info}}, {{ publi.year }}년 {{ publi.month }}월 {% if publi.link != null %}
  <a href="{{ publi.link }}">[PDF]</a>
  {% endif %}

{% endfor %}

## International Patents
{% assign var_year = 2022 %}
{% for publi in site.data.publications.international_patents %}
  {% if var_year != publi.year and var_year > year_until%}
  **{{ publi.year }}** <br />
  {% endif %}
  {% assign var_year = publi.year %}
  **{{ publi.title }}** <br />
  <em>{{ publi.authors }} </em><br />
  {{publi.info}}, {{ publi.month }} {{ publi.year }} {% if publi.link != null %} 
  <a href="{{ publi.link }}">[PDF]</a>
  {% endif %}

{% endfor %}
## Domestic Patents
{% assign var_year = 2022 %}
{% for publi in site.data.publications.domestic_patents %}
  {% if var_year != publi.year and var_year > year_until%}
  **{{ publi.year }}** <br />
  {% endif %}
  {% assign var_year = publi.year %}
  **{{ publi.title }}** <br />
  <em>{{ publi.authors }} </em><br />
  {{publi.info}}, {{ publi.year }}년 {{ publi.month }}월 {% if publi.link != null %}
  <a href="{{ publi.link }}">[PDF]</a>
  {% endif %}

{% endfor %}

## Invited Talks

{% for publi in site.data.publications.invited_talks %}

  **{{ publi.title }}** <br />
  {{publi.info}}, {{ publi.month }} {{ publi.year }}

{% endfor %}
