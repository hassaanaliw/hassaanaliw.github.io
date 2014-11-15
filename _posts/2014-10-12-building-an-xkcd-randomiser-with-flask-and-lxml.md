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
   Lets load a random XKCD url with requests and load the source with lxml.
</p>
{% highlight python %}
import requests, random
from lxml import html

#open a random xkcd comic between 1 & 1446

source = requests.get("http://xkcd.com/%d" % random.randint(1,1446)).text
tree = html.fromstring(source.encode('utf-8'))


{%endhighlight%}


Now we need to extract the actual image and the short-title for the comic from the source. To do this we will be using XPath.	 

<strong>XPath is used to navigate through elements and attributes in an XML document.</strong>

A nice tutorfial for XPath can be found [here](http://www.w3schools.com/xpath/)

First off, we will need to build our selectors. Remember that our required div had an id <strong>"comic"?</strong> So, our selector starts off as 
     
     '//div[@id="comic"]'
Next we have an <strong>img</strong> tag.

     '//div[@id="comic"]/img'
Next we want the <strong>src</strong> and the <strong>alt</strong> attributes within the img tag.

     #for the src

     '//div[@id="comic"]/img/@src'

     #for alt

     '//div[@id="comic"]/img/@alt'

Now, since are selectors are complete, lets add them to our Python code.

{% highlight python %}

import requests, random
from lxml import html

#open a random xkcd comic between 1 & 1446

source = requests.get("http://xkcd.com/%d" % random.randint(1,1446)).text
tree = html.fromstring(source.encode('utf-8'))

img = tree.xpath('//div[@id="comic"]/img/@src')
alt = tree.xpath('//div[@id="comic"]/img/@alt')

{% endhighlight %} 

We should add a for loop into this so that we get 10 comics instead of one.

{% highlight python %}

import requests, random
from lxml import html

#open ten random xkcd comics between 1 & 1446

for i in range(0,10):
	source = requests.get("http://xkcd.com/%d" % random.randint(1,1446)).text
	tree = html.fromstring(source.encode('utf-8'))

	img = tree.xpath('//div[@id="comic"]/img/@src')
	alt = tree.xpath('//div[@id="comic"]/img/@alt')

{% endhighlight %} 







     

    