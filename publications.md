---
layout: splash
title: Publications
classes: wide
---
<script type="text/javascript" src="toggle.js"> </script>

<style type="text/css" src="bibs.css">
a:link, a:visited, a:hover, a:active {text-decoration: none;}
.arxiv {
	font-size: small;
	background-color: red;
	color: white;
	border: 1px solid red;
	text-decoration: none;
	text-decoration-color: white;
	border-radius: 2px;
}
.openreview {
	font-size: small;
	background-color: red;
	color: white;
	border: 1px solid red;
	text-decoration: none;
	text-decoration-color: white;
	border-radius: 2px;
}
.pdf {
	font-size: small;
	background-color: blue;
	color: white;
	border: 1px solid blue;
	text-decoration: none;
	text-decoration-color: black;
	border-radius: 2px;
}
.link {
	font-size: small;
	background-color: blue;
	color: white;
	border: 1px solid blue;
	text-decoration: none;
	text-decoration-color: white;
	border-radius: 2px;
}
.journal {
	font-size: small;
	background-color: darkgreen;
	color: white;
	border: 1px solid darkgreen;
	text-decoration: none;
	text-decoration-color: white;
	border-radius: 2px;
}
.workshop {
	font-size: small;
	background-color: darkslateblue;
	color: white;
	border: 1px solid darkslateblue;
	text-decoration: none;
	text-decoration-color: white;
	border-radius: 2px;
}
.conference {
	font-size: small;
	background-color: purple;
	color: white;
	border: 1px solid purple;
	text-decoration: none;
	text-decoration-color: white;
	border-radius: 2px;
}
.website {
	font-size: small;
	background-color: sienna;
	color: white;
	border: 1px solid sienna;
	text-decoration: none;
	text-decoration-color: white;
	border-radius: 2px;
}
.code {
	font-size: small;
	background-color: grey;
	color: black;
	border: 1px solid grey;
	text-decoration: none;
	text-decoration-color: white;
	border-radius: 2px;
}
.talk {
	font-size: small;
	background-color: hotpink;
	color: black;
	border: 1px solid hotpink;
	text-decoration: none;
	text-decoration-color: white;
	border-radius: 2px;
}
.media {
	font-size: small;
	background-color: hotpink;
	color: black;
	border: 1px solid hotpink;
	text-decoration: none;
	text-decoration-color: white;
	border-radius: 2px;
}
.blog {
	font-size: small;
	background-color: sandybrown;
	color: black;
	border: 1px solid sandybrown;
	text-decoration: none;
	text-decoration-color: white;
	border-radius: 2px;
}
.bibbutton {
	font-size: small;
	background-color: black;
	color: white;
	border: 1px solid black;
	text-decoration: none;
	text-decoration-color: white;
	border-radius: 2px;
}
.bibtex {
	white-space: pre-wrap;
	font-size: small;
	font-family: Courier;
	background: #565656;
	border: 1px dotted black;
	width: 75%;
}	
</style>

# Publications

{% for y in site.data.years %}
## {{ y }}
<p>
{% for x in site.data.pubs.entries reversed %}
  {% assign ystr = y | downcase %}
  {% if x.year == ystr %}
	  <p>
	  	{% for a in x.author %}
	  		{% if forloop.last == true and forloop.first == false %}and{% endif%} {{ a.first }} {{ a.middle }} {{ a.last }}{% if forloop.last == false and forloop.length > 2 %},{% endif %}
	  	{% endfor %}<br>
	    <b>{{ x.title }}</b><br>
	    <em>{{ x.journal }}{{ x.booktitle }} 
	    {{ x.volume }} 
	    ({{ x.year }})</em>.<br>
	    {% if x.journal and x.volume %}<span class="journal">Journal</span>{% endif %}
	    {% if x.journal contains "preprint" %}<span class="arxiv">Preprint</span>{% endif %}
	    {% if x.booktitle %}{% if x.booktitle contains "Workshop" %}<span class="workshop">Workshop</span>{% else%}<span class="conference">Conference</span>{% endif %}{% endif %}
	    {% if x.bibtex %}
	    {% if x.url %}<a href="{{x.url}}"><span class="link">Paper Link</span></a>{% endif %}
	    {% if x.website %}<a href="{{x.website}}"><span class="website">Project Website</span></a>{% endif %}
	    {% if x.code %}<a href="{{x.code}}"><span class="code">Code</span></a>{% endif %}
	    {% if x.blog %}<a href="{{x.blog}}"><span class="blog">Blog</span></a>{% endif %}
	    {% if x.media %}<a href="{{x.media}}"><span class="media">Media Coverage</span></a>{% endif %}
	    {% if x.talk %}<a href="{{x.talk}}"><span class="talk">Talk</span></a>{% endif %}
	    <a onclick="toggleBibtex({{ x.id }});"><span class="bibbutton">bibtex</span></a><br>
	    <div class="bibtex" id="{{ x.id }}" style="display: none;">{{ x.bibtex }}</div>
	    {% endif %}
	  </p>
  {% endif %}
{% endfor %}
</p>
{% endfor %}

