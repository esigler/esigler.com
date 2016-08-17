---
layout: page
title: Personal
---
{% for post in site.posts %}
{% if post.category == "personal" %}
* [{{ post.heading }}]({{ post.url }})
{% endif %}
{% endfor %}
