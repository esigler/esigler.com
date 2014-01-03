---
layout: default
title: Personal
heading: Personal
category: top
---
<ul>
{% for post in site.posts %}
{% if post.category == "personal" %}
  <li><a href="{{ post.url }}">{{ post.heading }}</a></li>
{% endif %}
{% endfor %}
</ul>
