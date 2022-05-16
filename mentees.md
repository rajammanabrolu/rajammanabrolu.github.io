---
layout: splash
title: Collabs

---

# Mentees and Collaborators
I am fortunate to have had a chance to work with and help advise an amazingly talented group of people on research projects.

**PhD Students**

<ul>
{% for x in site.data.phds.members %}
  <li>
    <a href="{{ x.website }}">{{ x.name }}</a>
  </li>
{% endfor %}
</ul>

**Masters Students**

<ul>
{% for x in site.data.masters.members %}
  <li>
    <a href="{{ x.website }}">{{ x.name }}</a>
  </li>
{% endfor %}
</ul>

**Undergraduate Students**

<ul>
{% for x in site.data.undergrads.members %}
  <li>
    <a href="{{ x.website }}">{{ x.name }}</a>
  </li>
{% endfor %}
</ul>

