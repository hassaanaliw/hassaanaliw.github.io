---
layout: post
title: "Building a XKCD Randomiser with Flask and lxml"
description: "A tutorial about scraping XKCD and displaying results as a web app with Flask."
category: python  
tags: [flask]
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

A nice tutorial for XPath can be found [here](http://www.w3schools.com/xpath/)

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

We should add a for loop into this so that we get 10 comics instead of one and add the results to a list.

{% highlight python %}

import requests, random
from lxml import html

comics_list = []

#open ten random xkcd comics between 1 & 1446

for i in range(0,10):
	source = requests.get("http://xkcd.com/%d" % random.randint(1,1446)).text
	tree = html.fromstring(source.encode('utf-8'))

	img = tree.xpath('//div[@id="comic"]/img/@src')
	alt = tree.xpath('//div[@id="comic"]/img/@alt')

	comics_list.append({
		'img':img[0],
		'alt':alt[0]
		})

{% endhighlight %} 

So our parsing script is complete. Let's move on to the Flask Webapp.

#Flask Webapp

You can find a detailed tutorial on getting started with flask [here](http://hassaanaliw.github.io/python/2014/10/11/getting-started-with-flask.html).

First lets create a directory for our app, create a VirtualEnv and install Flask, requests and lxml.

	 $ mkdir randomxkcd
	 $ cd randomxkcd
	 $ virtualenv venv
	 $ . venv/bin/activate
	 $ pip install Flask requests lxml


A typical Flask App Directory structure looks like:
     
    /application
		>app.py
		/static
			/css
			/js
		/templates
			>index.html	
		/venv
			.......... 	

To create a structure like this, simply run the following commands

	 $ mkdir static
	 $ mkdir templates
	 $ touch app.py
	 $ cd templates
	 $ touch index.html	
	 $ cd ..		

Now add the Flask app template to app.py 

{% highlight python %}

import os
from flask import Flask, render_template
import requests
import random
from lxml import html

app = Flask(__name__)
app.config.update(
    DEBUG=True,
)


@app.route('/')
def index():

	return 'Hello'


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)	




{% endhighlight %}


Now run app.py and if all went well throughout this process, by navigating to  [localhost:5000](http://localhost:5000), you should be greeted by "Hello".

Lets add the parsing logic we wrote earlier to a function parse() in app.py and add a check to see if an image is absent, to replace it with a 404 image.

{% highlight python %}

import os
from flask import Flask, render_template
import requests
import random
from lxml import html

app = Flask(__name__)
app.config.update(
    DEBUG=True,
)


@app.route('/')
def index():

	return 'Hello'


def parse():
	comics_list = []

	#open ten random xkcd comics between 1 & 1446

	for i in range(0,10):
		source = requests.get("http://xkcd.com/%d" % random.randint(1,1446)).text
		tree = html.fromstring(source.encode('utf-8'))

		img = tree.xpath('//div[@id="comic"]/img/@src')
		alt = tree.xpath('//div[@id="comic"]/img/@alt')

		try: 
			img[0]
		except:
		    img.append('http://i0.kym-cdn.com/photos/images/newsfeed/000/178/254/c86.jpg')
		    alt.append("Error: Image Not Found.")	


		comics_list.append({
			'img':img[0],
			'alt':alt[0]
			})

	return comics_list


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)	




{% endhighlight %}



Ok now pass the comics_list to the index.html file. Our python script <strong>app.py</strong> should finally look like

{% highlight python %}

import os
from flask import Flask, render_template
import requests
import random
from lxml import html

app = Flask(__name__)
app.config.update(
    DEBUG=True,
)


@app.route('/')
def index():
    
    #pass the comic_list to index.html
    return render_template('index.html',data=parse())


def parse():
    comics_list = []

    #open ten random xkcd comics between 1 & 1446

    for i in range(0,10):
        source = requests.get("http://xkcd.com/%d" % random.randint(1,1446)).text
        tree = html.fromstring(source.encode('utf-8'))

        img = tree.xpath('//div[@id="comic"]/img/@src')
        alt = tree.xpath('//div[@id="comic"]/img/@alt')

        try: 
            img[0]
        except:
            img.append('http://i0.kym-cdn.com/photos/images/newsfeed/000/178/254/c86.jpg')
            alt.append("Error: Image Not Found.")   


        comics_list.append({
            'img':img[0],
            'alt':alt[0]
            })

    return comics_list


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


{%endhighlight%}

In the end we add a very simple index.html file to display the results.

<script src="https://gist.github.com/hassaanaliw/f8d3ac8491ea8fd6aa1a.js"></script>

Now run 
	 python app.py

And you should be greeted with something like this.

![Success!](https://raw.githubusercontent.com/hassaanaliw/hassaanaliw.github.io/master/assets/images/localhost5000.png) 

#Deploying to Heroku.

Now we want our Flask App to be hosted online. Heroku is the best choice for this. It will provide a 512 MB free dyno for us to host this app and host up to 5 free apps. Our app is not really memory hungry so 512 MB is more than enough.

First follow the first two steps in [this tutorial](https://devcenter.heroku.com/articles/getting-started-with-python#introduction) to set up heroku and log yourself in on your machine. Now in our app directory (randomxkcd) run the following command to setup a git repo and create a heroku app.

	git init
	heroku create

Heroku requires a requirements.txt file to see what Python modules it will need to install and a Procfile to tell it what processes to run. To create a requirements.txt file 

	pip freeze > requirements.txt

and to create the Procfile
	
	touch Procfile

Edit the Procfile to say

	web: python app.py

Now rename the heroku app to what you want with 
	
	heroku apps:rename uniquenameiwant

I chose randomxkcd so this command becomes

	heroku apps:rename randomxkcd
	#this name is taken by me now.

Now to add these files to git and push them to Heroku.

	git add -A
	git commit -m "Original Commit"
	git push heroku master

Your app will now be availabe at 

	uniquenameiwant.herokuapp.com
	#in my case it becomes randomxkcd.herokuapp.com

[Find the Source Code on Github](https://github.com/hassaanaliw/randomxkcd)<br/>
[Live Demo on Heroku](http://randomxkcd.herokuapp.com/)



	











     

    
