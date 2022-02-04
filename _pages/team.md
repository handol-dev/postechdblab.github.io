---
title: "Database & Data Mining Lab - Team"
layout: gridlay
excerpt: "Database & Data Mining Lab: Team members"
sitemap: false
permalink: /team/
---

# Group Members

**We are seeking for self-motivated master and Ph.D. students!** <br>
(Unfortunately, we do not have any opening for foreign students.) <br>
Please send an email to Prof. Wook-Shin Han at [wshan@dblab.postech.ac.kr](mailto:wshan@dblab.postech.ac.kr) regarding the scholarship.

Jump to [Professor](#professor), [Research Professor](#research-professor), [Post Doc.](#post-doc), [Ph.D. and Master Students](#phd-and-master-students), [Bachelor Students](#bachelor-students), [Alumni](#alumni).

## Professor

<div class="row">
<div class="col-sm-12 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/wshan.jpeg" class="img-responsive" width="160px" style="float: left" />
  <h4>Wook-Shin Han</h4>
  <i>Professor
  <ul style="overflow: hidden">
  <li><a href="https://wscrony.github.io/">Detailed Information</a></li>
  </ul>
</div>
</div>

## Research Professor
{% assign number_printed = 0 %}
{% for member in site.data.professors %}

<div class="row">
<div class="col-sm-12 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="140px" style="float: left" />
  <h4><a href="{{ member.homepage }}">{{ member.name }}</a></h4>
  <i>{{ member.info }} <!--<br>email: <{{ member.email }}></i>-->
  <ul style="overflow: hidden">

  {% if member.number_educ == 1 %}
  <li> {{ member.education1 }} </li>
  {% endif %}

  {% if member.number_educ == 2 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  {% endif %}

  {% if member.number_educ == 3 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  {% endif %}

  {% if member.number_educ == 4 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  <li> {{ member.education4 }} </li>
  {% endif %}

  {% if member.number_educ == 5 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  <li> {{ member.education4 }} </li>
  <li> {{ member.education5 }} </li>
  {% endif %}

  </ul>
</div>
</div>

{% endfor %}


## Post Doc.
{% assign number_printed = 0 %}
{% for member in site.data.postdoc %}

<div class="row">
<div class="col-sm-12 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="140px" style="float: left" />
  <h4>{{ member.name }}</h4>
  <i>{{ member.info }} <!--<br>email: <{{ member.email }}></i> -->
  <ul style="overflow: hidden">

  {% if member.number_educ == 1 %}
  <li> {{ member.education1 }} </li>
  {% endif %}

  {% if member.number_educ == 2 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  {% endif %}

  {% if member.number_educ == 3 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  {% endif %}

  {% if member.number_educ == 4 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  <li> {{ member.education4 }} </li>
  {% endif %}

  {% if member.number_educ == 5 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  <li> {{ member.education4 }} </li>
  <li> {{ member.education5 }} </li>
  {% endif %}

  </ul>
</div>
</div>

{% endfor %}


## Ph.D. and Master Students
{% assign number_printed = 0 %}
{% for member in site.data.team_members %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="120px" style="float: left" />
  <h4><a href="{{ member.homepage }}">{{ member.name }}</a></h4>
  <i>{{ member.info }} <!-- <br>email: <{{ member.email }}></i> -->
  <ul style="overflow: hidden">

  {% if member.number_educ == 1 %}
  <li> {{ member.education1 }} </li>
  {% endif %}

  {% if member.number_educ == 2 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  {% endif %}

  {% if member.number_educ == 3 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  {% endif %}

  {% if member.number_educ == 4 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  <li> {{ member.education4 }} </li>
  {% endif %}

  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}


## Bachelor Students
{% assign number_printed = 0 %}
{% for member in site.data.students %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <h4>{{ member.name }}</h4>
  <i>{{ member.info }} <!-- <br>email: <{{ member.email }}></i> -->
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

<!--
## Administration Staff
-->

## Alumni

<div class="row" style="text-align:center;font-size:20px">
<i>I am proud of having worked with the following students!</i> -- wsh
</div>

<div class="row" style="text-align:center">
After Aug. 2013 (after Prof. Han moved to POSTECH)
</div>

### Post-docs and Researchers
<div class="row">
<div class="col-sm-6 clearfix">
<h4>Jinha Kim</h4>
<i>Principal member of Technical Staff @ Oracle Labs, Redwood Shores, USA
</div>

<div class="col-sm-6 clearfix">
<h4><a href="https://www.linkedin.com/in/jinohoh/">Jinoh Oh</a></h4>
<i>Applied Scientist, Alexa AI, Amazon
</div>
</div>

### Ph.D.
<div class="row">
<div class="col-sm-6 clearfix">
<h4><a href="https://www.linkedin.com/in/seongyun-ko-7aa698b2/">Seongyun Ko</a></h4>
<i>Facebook, Menlo Park, USA
</div>
</div>

### Master
<div class="row">
<div class="col-sm-6 clearfix">
<h4>Byeong hoon So</h4>
</div>
  
<div class="row">
<div class="col-sm-6 clearfix">
<h4>JungHo Cho</h4>
</div>
</div>
  
<div class="row">
<div class="col-sm-6 clearfix">
<h4>MinWoo Kim</h4>
</div>
  
<div class="row">
<div class="col-sm-6 clearfix">
<h4>SeungMin Lee</h4>
</div>
</div>  


<div class="row" style="text-align:center">
Before Aug. 2013 (Students supervised at Kyungpook National University)
</div>

### Post-docs
<div class="row">
<div class="col-sm-6 clearfix">
<h4><a href="https://de.linkedin.com/in/romans-kasperovics-355a239">Romans Kasperovics</a></h4> 
<i>Senior Developer @ SAP, Germany
</div>
</div>

### Ph.D.
<div class="row">
<div class="col-sm-6 clearfix">
<h4><a href="https://www.linkedin.com/in/jinsoo-lee-570275122/">Jinsoo Lee</a></h4> 
<i>Principal member of Technical Staff, Oracle Labs, Redwood Shores, USA
</div>
</div>

### Researcher
<div class="row">
<div class="col-sm-6 clearfix">
<h4><a href="https://lmanikon.github.io">Lydia Manikonda</a></h4> 
<i>Assistant Professor @ Rensselaer Polytechnic Institute, USA
</div>

<div class="col-sm-6 clearfix">
<h4>Pham Minh Duc</h4> 
<i>CWI, Netherland
</div>
</div>

### Master
<div class="row">
<div class="col-sm-6 clearfix">
<h4>Junyoung Kim</h4> 
<i>Columbia University, USA
</div>

<div class="col-sm-6 clearfix">
<h4>Won-Sik Kim</h4>
<i>Kakao, Korea
</div>

<div class="col-sm-6 clearfix">
<h4>Seon-Hyo Kim</h4>
</div>
</div>


<div class="row">
<div class="col-sm-6 clearfix">
<h4>Je-Yong Shin</h4>
<i>Samsung Inc.
</div>

<div class="col-sm-6 clearfix">
<h4>Woo-Seong Kwak</h4>
<i>Korea Color Steel Corp., Korea(CEO)
</div>
</div>


<div class="row">
<div class="col-sm-6 clearfix">
<h4>Sungjin Lee</h4>
<i>GS itm
</div>

<div class="col-sm-6 clearfix">
<h4>Pham Minh Duc</h4>
<i>CWI, Netherland
</div>
</div>


<div class="row">
<div class="col-sm-6 clearfix">
<h4>Sungmun Chung</h4>
<i>Hyundai MnSoft, Korea
</div>


<div class="col-sm-6 clearfix">
<h4>Sunji Kim</h4>
<i>Wemade, Korea
</div>
</div>


<div class="row">
<div class="col-sm-6 clearfix">
<h4><a href="https://www.linkedin.com/in/loganleedev-0606/">Sang-Yeon Lee</a></h4>
<i>Senior software engineer, Microsoft, USA
</div>

<div class="col-sm-6 clearfix">
<h4>Kyung-Yul Park</h4>
<i>SAP Labs, Korea
</div>
</div>

<div class="row">
<div class="col-sm-6 clearfix">
<h4>Phi-Minh-Tri Nguyen</h4>
<i>Virginia Tech Uni., USA
</div>
</div>

### Undergrads
<div class="row">
<div class="col-sm-6 clearfix">
<h4>Jaehwa Kim</h4>
<i>SAP Labs, Korea
</div>


<div class="col-sm-6 clearfix">
<h4>Min Yu</h4>
<i>SAP Labs, Korea
</div>
</div>


<div class="row">
<div class="col-sm-6 clearfix">
<h4>Changhyun Min</h4>
<i>Amazon, Canada
</div>
</div>

### Honorary members

<div class="row">
<div class="col-sm-6 clearfix">
<h4>Jeong-Ki Park</h4>
<i>Kyungpook National Univ., Korea
</div>

<div class="col-sm-6 clearfix">
<h4>KyoungHun Kim</h4>
<i>Kyungpook National Univ., Korea
</div>
</div>

<div class="row">
<div class="col-sm-6 clearfix">
<h4>Trong-Dat Nguyen</h4>
<i>Sungkyunkwan Univ., Korea
</div>

<div class="col-sm-6 clearfix">
<h4>Joong-Won Hwang</h4>
<i>We make price, Korea
</div>
</div>

<div class="row">
<div class="col-sm-6 clearfix">
<h4>Thanh-Hieu Bui</h4>
<i>Kyungpook National Univ., Korea
</div>

<div class="col-sm-6 clearfix">
<h4>Chang-Uk Kwak</h4>
<i>ETRI
</div>
</div>

<!--
## Alumni

{% assign number_printed = 0 %}
{% for member in site.data.alumni_members %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  <h4>{{ member.name }}</h4>
  <i>{{ member.duration }} <br> Role: {{ member.info }}</i>
  <ul style="overflow: hidden">

  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

## Former visitors, BSc/ MSc students
<div class="row">

<div class="col-sm-4 clearfix">
<h4>Visitors</h4>
{% for member in site.data.alumni_visitors %}
{{ member.name }}
{% endfor %}
</div>

<div class="col-sm-4 clearfix">
<h4>Master students</h4>
{% for member in site.data.alumni_msc %}
{{ member.name }}
{% endfor %}
</div>

<div class="col-sm-4 clearfix">
<h4>Bachelor Students</h4>
{% for member in site.data.alumni_bsc %}
{{ member.name }}
{% endfor %}
</div>

</div>


## Administrative Support
<a href="mailto:Rijsewijk@Physics.LeidenUniv.nl">Ellie van Rijsewijk</a> is helping us (and other groups) with administration.
-->
