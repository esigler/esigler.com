---
layout: default
title: chatops
heading: Chatops
category: top
---
{% for post in site.posts %}
{% if post.category == "chatops" %}
* [{{ post.heading }}]({{ post.url }})
{% endif %}
{% endfor %}

I also maintain several plugins:

* [lita-datadog](https://github.com/esigler/lita-kegbot)
* [lita-deploygate](https://github.com/esigler/lita-deploygate)
* [lita-dig](https://github.com/esigler/lita-dig)
* [lita-jira](https://github.com/esigler/lita-jira)
* [lita-locker](https://github.com/esigler/lita-locker)
* [lita-pagerduty](https://github.com/pagerduty/lita-pagerduty)
* [lita-statuspage](https://github.com/esigler/lita-statuspage)
