---
layout: post
title: "Challenges"
description: ""
category: 
tags: []
---
<h3>Welcome to PyChallenge!</h3>
<p>Here you can find a list of all the challenges</p>
<ul>
  {% for post in site.posts %}
  <li>
    <a href="{{ post.url }}">{{ post.title }}</a>
  </li>
  {% endfor %}
</ul>
