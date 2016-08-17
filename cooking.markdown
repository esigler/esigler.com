---
layout: page
title: Cooking
---
{% for post in site.posts %}
{% if post.category == "cooking" %}
* [{{ post.heading }}]({{ post.url }})
{% endif %}
{% endfor %}
