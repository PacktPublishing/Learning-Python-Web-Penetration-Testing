# Learning Python Web Penetration Testing

<a href="https://www.packtpub.com/networking-and-servers/learning-python-web-penetration-testing?utm_source=github&utm_medium=repository&utm_campaign=9781789533972"><img src="https://www.packtpub.com/sites/default/files/9781789533972%20-%20Copy_0.png" alt="Learning Python Web Penetration Testing" height="256px" align="right"></a>

This is the code repository for [Learning Python Web Penetration Testing](https://www.packtpub.com/networking-and-servers/learning-python-web-penetration-testing?utm_source=github&utm_medium=repository&utm_campaign=9781789533972), published by Packt.

**Automate web penetration testing activities using Python**

## What is this book about?
Web penetration testing is the use of tools and code to attack a website or web app in order to assess its vulnerability to external threats. While there are an increasing number of sophisticated, ready-made tools to scan systems for vulnerabilities, the use of Python allows you to write system-specific scripts, or alter and extend existing testing tools to find, exploit, and record as many security weaknesses as possible. Learning Python Web Penetration Testing will walk you through the web application penetration testing methodology, showing you how to write your own tools with Python for each activity throughout the process. The book begins by emphasizing the importance of knowing how to write your own tools with Python for web application penetration testing. You will then learn to interact with a web application using Python, understand the anatomy of an HTTP request, URL, headers and message body, and later create a script to perform a request, and interpret the response and its headers. As you make your way through the book, you will write a web crawler using Python and the Scrappy library. The book will also help you to develop a tool to perform brute force attacks in different parts of the web application. You will then discover more on detecting and exploiting SQL injection vulnerabilities. By the end of this book, you will have successfully created an HTTP proxy based on the mitmproxy tool.

This book covers the following exciting features:
* Interact with a web application using the Python and Requests libraries
* Create a basic web application crawler and make it recursive
* Develop a brute force tool to discover and enumerate resources such as files and directories
* Explore different authentication methods commonly used in web applications
* Enumerate table names from a database using SQL injection

If you feel this book is for you, get your [copy](https://www.amazon.com/dp/178953397X) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" 
alt="https://www.packtpub.com/" border="5" /></a>


## Instructions and Navigations
All of the code is organized into folders. For example, Chapter02.

The code will look like the following:
```
import requests
payload= {'url':'http://www.edge-security.com'}
r=requests.get('http://httpbin.org/redirect-to',params=payload)
print "Status code:"
```

**Following is what you need for this book:**
Learning Python Web Penetration Testing is for web developers who want to step into the world of web application security testing. Basic knowledge of Python is necessary.

With the following software and hardware list you can run all code files present in the book (Chapter 2-7).

### Software and Hardware List

| Chapter  | Software required                   | OS required                        |
| -------- | ------------------------------------| -----------------------------------|
| 2-7        | VirtualBox                     | Windows, Mac OS X, Linux, and Solaris |



We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](https://www.packtpub.com/sites/default/files/downloads/LearningPythonWebPenetrationTesting_ColorImages.pdf).

### Related products <Paste books from the Other books you may enjoy section>
* Web Penetration Testing with Kali Linux - Third Edition [[Packt]](https://www.packtpub.com/networking-and-servers/web-penetration-testing-kali-linux-third-edition?utm_source=github&utm_medium=repository&utm_campaign=9781788623377) [[Amazon]](https://www.amazon.com/dp/1788623371)

* Python Penetration Testing Cookbook [[Packt]](https://www.packtpub.com/networking-and-servers/python-penetration-testing-cookbook?utm_source=github&utm_medium=repository&utm_campaign=9781784399771) [[Amazon]](https://www.amazon.com/dp/1784399779)

## Get to Know the Author
**Christian Martorella**
Christian Martorella has been working in the field of information security for the last 18 years and is currently leading the product security team for Skyscanner. Earlier, he was the principal program manager in the Skype product security team at Microsoft. His current focus is security engineering and automation. He has contributed to open source security testing tools such as Wfuzz, theHarvester, and Metagoofil, all included in Kali, the penetration testing Linux distribution.



### Suggestions and Feedback
[Click here](https://docs.google.com/forms/d/e/1FAIpQLSdy7dATC6QmEL81FIUuymZ0Wy9vH1jHkvpY57OiMeKGqib_Ow/viewform) if you have any feedback or suggestions.
