---
layout: post
title: "Getting Started with Flask"
description: An Introduction to web development with the Flask Framework
category: python		
tags: [python,flask,web-development]
---



</style>
<h3>What is Flask?</h3>
<p>Flask is a MicroFramework for Python based on Werkzeug, Jinja 2 and good intentions.</p>
<h3>What does it come with?</h3>
<ul style="font-size:18px">
	<li style="font-size:16px">Built in development server and debugger</li>
	<li style="font-size:16px">Integrated unit testing support</li>
	<li style="font-size:16px">RESTful request dispatching</li>
	<li style="font-size:16px">Uses Jinja2 templating</li>
	<li style="font-size:16px">Support for secure cookies (client side sessions)</li>
	<li style="font-size:16px">100% WSGI 1.0 compliant</li>
	<li style="font-size:16px">Unicode based</li>
	<li style="font-size:16px">Extensively documented</li>
</ul>
<h1 style="margin-top: 0px;padding-top: 1px;">Installation</h1>
<p>
	<b><u>Make sure you have a working Python Installation.</b></u><br/><br/>
We will be installing Flask in a VirtualEnv(Virtual Environment) to make sure there is no conflict of dependency versions.<br/><br/>

On Mac OSX and Linux Systems the following commands should be enough to get you up and running with virtualenv.<br/>
     
	 {% highlight python %}
	 sudo easy_install virtualenv
	 {% endhighlight %}
	 
	 OR
     {% highlight python %}
	 sudo pip install virtualenv
	 {% endhighlight %}
	 

<p><b>Otherwise please follow <a href="http://pip.readthedocs.org/en/latest/installing.html">these instructions</a> to install Pip</b><br/><br/>
	
	Now to create a VirtualEnv
	
	{% highlight python lineos %}
	 #bash
	 mkdir myproject
	 cd myproject
	 virtualenv venv
	 New python executable in venv/bin/python
	 Installing distribute............done.
	
	{% endhighlight %}
	
Now, whenever you want to work on a project, you only have to activate the corresponding environment. On OS X and Linux, do the following:
	
	{% highlight python %}
	. venv/bin/activate
	{% endhighlight %}

On Windows:

	{% highlight python %}
	 venv\scripts\activate
	{% endhighlight %}
	
And now you should finally be able to:

	{% highlight python %}
	pip install Flask
	{% endhighlight %}	
	
	
	


</p>
	 
	 
    
</p>

<h3>Runnning your first Flask App</h3>

{%highlight python%}
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to Flask!"

if __name__ == "__main__":
    app.run()
{%endhighlight%}	

Now open <a href="http://localhost:5000">localhost:5000</a> to see the magic.