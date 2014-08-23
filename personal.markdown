---
layout: default
title: Personal
heading: Personal
category: top
---
{% for post in site.posts %}
{% if post.category == "personal" %}
* [{{ post.heading }}]({{ post.url }})
{% endif %}
{% endfor %}
