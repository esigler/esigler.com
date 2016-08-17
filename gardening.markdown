---
layout: page
title: gardening
---
<ul>
{% for post in site.posts %}
{% if post.category == "gardening" %}
  <li><a href="{{ post.url }}">{{ post.heading }}</a></li>
{% endif %}
{% endfor %}
</ul>
