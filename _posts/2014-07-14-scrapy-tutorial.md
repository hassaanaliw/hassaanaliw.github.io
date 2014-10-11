---
layout: post
title: "Scrapy Tutorial : Let's Crawl Google Play"
description: "Learn how to use Scrapy to crawl one of the biggest app stores."
category: Python
tags: []
---
<h3>An Introduction to Scrapy</h3>
<h3>What is Scrapy?</h3>
<p>Scrapy is a fast high-level screen scraping and web crawling framework, used to crawl websites and extract structured data from their pages. It can be used for a wide range of purposes, from data mining to monitoring and automated testing.</p>
<h3>Installation:</h3>
The entire Installation is outlined :: <a href = "http://doc.scrapy.org/en/latest/intro/install.html#intro-install"> In the Scrapy Documentation </a>

<h3>Let's Crawl.</h3>
<p>Navigate to a directory where you want to create a project and run 


       {% highlight python lineos %} scrapy startproject play {% endhighlight %}


This should create a project with the name 'play' with a directory structure of :
<pre>
+-- scrapy.cfg
+-- play
|   +-- items.py
|   +-- pipeline.py
|   +-- settings.py
|   +-- _init_.py
|   +-- spiders
      | +-- _init_.py
</pre>

Open items.py and change the code to :
 {% highlight python lineos %} 
 # -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PlayItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    
 {% endhighlight %}

 Title and link are the two fields we will be scraping from GooglePlay.


 Next open the Spiders Folder and create a python file with any name. I will name it : "gp.py"

Open gp.py and import the following :


     
{% highlight python lineos %} 
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from play.items import PlayItem #remember we declared PlayItem in items.py
from scrapy.http import Request {% endhighlight %}

Ok , now suppose we want to scrape links and titles from the Finance Category. Let's visit play.google.com and find the link for the category. Ok so the link is :

<a href = "https://play.google.com/store/apps/category/FINANCE"> Play Store Finance Category </a>

<p>Ok so lets create a Finance class. Change gp.py to :

{% highlight python lineos %}

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from play.items import PlayItem #remember we declared PlayItem in items.py
from scrapy.http import Request

class Finance(BaseSpider):
    name = "finance" #the name by which we will call the spyder
    allowed_domains    = ["play.google.com"]
    start_urls = ["https://play.google.com/store/apps/category/FINANCE"]
{%endhighlight%}

Now lets write the Parse Function.

NOTE : hxs Is the Selector that will find us the information from our page source. Unfortunately XPath is rather complicated at times and you will have to learn it via some external means.

<br></br>
<a href = "http://www.w3schools.com/XPath/"> XPath tutorial at w3schools </a>
<br></br>

{% highlight python lineos %}
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from play.items import PlayItem #remember we declared PlayItem in items.py
from scrapy.http import Request

class Finance(BaseSpider):
    name = "finance" #the name by which we will call the spyder
    allowed_domains    = ["play.google.com"]
    start_urls = ["https://play.google.com/store/apps/category/FINANCE"]

    def parse(self,response):
      hxs = HtmlXPathSelector(response)
      titles = hxs.select('//h2/a[@class = "title"]')

#This Basically searches the html for a tags with the 'title' class.
#Furthermore this "<a>" tag is the child of a H2 tag.

      for title in titles :
         item = PlayItem()
         item["title"] = title.select("text()").extract()
         item ["link"] = 'https://play.google.com'+title.select("@href").extract()[0]
          yield item


{%endhighlight%}
<br></br>


Let me explain the "for title in titles" part.
<br></br>

item['title'] extracts the text from the aforementionted "a" tag.
item['link'] extracts the href from the "a" tag.
These are assigned to the title and link declared as PlayItem() in items.py.
Then they are yielded.
<br></br>

Ok so our code is done.

Go back to the root directory of play and run 

{% highlight python lineos%}

scrapy crawl finance -o data.csv -t csv

{%endhighlight%}

This outputs our data to Data.csv file.

This concludes the tutorial. Now go scrape!


</p>
