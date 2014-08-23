---
layout: default
title: gardening
heading: Gardening
category: top
---
<ul>
{% for post in site.posts %}
{% if post.category == "gardening" %}
  <li><a href="{{ post.url }}">{{ post.heading }}</a></li>
{% endif %}
{% endfor %}
</ul>
