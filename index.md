---
layout: default
title: Home
---

# Hi, this is blog.

## Last posts

<ul>
{% for post in site.posts %}
  <li>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    — {{ post.date | date: "%d.%m.%Y" }}
  </li>
{% else %}
  <li>Nothing, try later.</li>
{% endfor %}
</ul>
