---
layout: post
title: "Building a XKCD Randomiser with Flask and lxml"
description: "A tutorial about scraping XKCD and displaying results as a web app with Flask."
category: python  
tags: []
---

In this tutorial, we will be scraping xkcd for its brilliant comics and displaying ten random ones on our website with Flask.
Our Logic will consist of two parts:<br/><br/>
<b>1)The HTML Parsing with lxml</br>
2)Building a web app with Flask.</b></br>

First, let's create a parsing script.
<h3>Parsing XKCD</h3>
<p>The first part of any scraping operation is to study the HTML Source of our target pages. So open up the page of any comic (<a href="http://xkcd.com/936/">this should do</a>) and start reading its source.
	There are a few things to note now:</p>
	<ol style="padding-bottom: 0px;">
		<li style="font-size:18px">There are roughly 1446 XKCD Comics at the time of writing</li>
		<li style="font-size:18px">The information we want is inside a <b>&lt;div id='comic'&gt;</b> tag </li>
		<li style="font-size:18px">This div contains a <b>img</b>, an <b>alt</b> and a <b>title</b> tag.</li>
	</ol>

<p>We are going to be using the img tags and the alt tags for our app. So let's get started with the parsing <br/><br/>
   Lets load the url with requests.
</p>

     import requests
	 
	 html = requests.get("http://xkcd.com/936").text
	 


     

    