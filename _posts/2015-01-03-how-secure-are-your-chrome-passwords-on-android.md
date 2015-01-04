---
layout: post
title: "How secure are your Chrome Passwords on Android?"
description: ""
category: 
tags: []
---

If you have ever provided an app root access, not very secure it would seem.

Pre-Summary:

* On Android and on Ubuntu, Chrome does not encrypt saved passwords
* These passwords are stored in a database called LoginData.
* The passwords can be easily viewed with a database browser.

Storage
----------

When you enter a password for a website into [Chrome on Android](https://play.google.com/store/apps/details?id=com.android.chrome&hl=en), chances are you see a prompt to save your password. 

<img src="/assets/article_images/Screenshot_2015-01-03-23-45-50.png " alt="Drawing" style="width: 300px; height:500px;"/>

If you click yes, Chrome will save information about the page such as the names of the form elements as well as the <strong>password</strong> to a database called __LoginData__.

This database resides in the /data/data directory, so to access it, root access __is required__

The full path to the database is:

>/data/data/com.android.chrome/app_chrome/Default/Login Data

<img src="/assets/article_images/Screenshot_2015-01-03-23-10-48.png" style="width:300px; height:500px; " />

##The Problem

If you haven't rooted your phone or just don't give root access to apps, you will probably be fine.

__However__, any app with root access can access the database with the passwords.

And the problem is, Chrome stores these passwords in the database in __PlainText__.

If you have rooted your phone and want to test this, retrieve the database from the aforementioned directory and transfer it to your computer.

Then load the DataBase using [SQLite Browser](http://sqlitebrowser.org/) and open the Logins table.

Here you should be able to see all your saved usernames and passwords.

## The Test.

To test this, I set up a simple website form on [Heroku](https://droidpw.herokuapp.com)

<img src="/assets/article_images/Screenshot_2015-01-04-18-16-33.png" alt="Drawing" style="width: 300px; height:500px;"/>

Then I entered 5 different username/password combinations and saved them in Chrome

<table><thead>
<tr>
<th>Username</th>
<th>Password</th>
</tr>
</thead><tbody>
<tr>
<td>mine</td>
<td>craft</td>
</tr>
<tr>
<td>hello</td>
<td>hi</td>
</tr>
<tr>
	<td>usb</td>
	<td>mouse</td>
</tr>
<tr>
    <td>droid</td>
    <td>pw</td>
</tr>
<tr>
	<td>reddit</td>
	<td>android</td>
</tr>	
</tbody></table>

I then sent the database to my computer and opened it up with SQLite Browser and this is the result:

<img src="/assets/article_images/Screenshot from 2015-01-04 18:54:46.png" alt="Drawing" />


##Conclusion

As long as you are careful with/do not use root access, you should be fine.

However, it still seems quite scary that Google itself isn't encrypting the passwords.

The news for Ubuntu Chromium isn't much better either. The daabase located at

> /home/username/.config/chromium/Default/Login Data

can be viewed freely as well with the database browser linked above .

On Windows, it is atleast encrypted with the WinCrypt API. But these passwords can be decrypted very easily with a simple [python script](https://github.com/hassaanaliw/chromepass).
