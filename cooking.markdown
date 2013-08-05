---
layout: default
title: cooking
heading: Cooking
category: top
---
<ul>
{% for post in site.posts %}
{% if post.category == "cooking" %}
  <li><a href="{{ post.url }}">{{ post.heading }}</a></li>
{% endif %}
{% endfor %}
</ul>
