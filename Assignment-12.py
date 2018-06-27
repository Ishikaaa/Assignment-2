#Q1.
print('''Access Tokens - An access_token is a unique string of letters and numbers that you pass with every API call.Access tokens are private, so they should never be shared or passed as a GET or POST argument. You should never email your access token to a third-party.
To Generate access token for any API -
a.Go to https://dev.twitter.com/apps/new and log in, if necessary
b.Enter your Application Name, Description and your website address. You can leave the callback URL empty.
c.Accept the TOS, and solve the CAPTCHA.
d.Submit the form by clicking the Create your Twitter Application
e.Copy the consumer key (API key) and consumer secret from the screen into your application''')

#Q2.
import socket
a=socket.gethostbyname("google.com")
b=socket.gethostbyname("facebook.com")
print("IP address of google -",a)
print("IP address of facebook -",b)

#2..
print('''Steps to get the IP address -
1. You type www.facebook.com into the address bar of your of browser.
2. The browser checks the cache for a DNS record to find the corresspondinf IP address www.facebook.com.
3. If the requested URL is not in the cache, IPS's DNS server initiates a DNS query to find the IP address of the server that hosts.
4. Browser initiates a TCP connection with the server.
5. The browser sends an HTTP request to the web server.
6. The server handles the request and sends back a response.
7. The server sends out an HTTP response.
8. The browser displays the html content.''')

#Q3.
from keys import Access_Token,Consumer_Key,Consumer_Secret,Access_Token_Secret
import tweepy
a=tweepy.OAuthHandler(Consumer_Key,Consumer_Secret)
a.set_access_token(Access_Token,Access_Token_Secret)
b=tweepy.API(a)
print(b.search("#sanju"))
user=b.get_user("@IshikaG62386743")
c=b.user_timeline(screen_name="@IshikaG62386743",count=200,tweet_node="extended")
print(c)

#Q4.
print('''Difference between library and API -
A library is a chunk of code that you can call from your own code, to help ypu do things more easily and quickly.
For example : Numpy is a library of Python, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
An API(Application Programming Interface) is a term meaning the functions/methods in a library that you can call to ask it to do things for you.
For eg - We can create our own APIs using Python Framework like Django and Flask which can be used in websites. You can follow documentation of Django in order to create your own website with Python. 
''')

#Q5.
from keys import Access_Token,Consumer_Key,Consumer_Secret,Access_Token_Secret
import tweepy

a=tweepy.OAuthHandler(Consumer_Key,Consumer_Secret)
a.set_access_token(Access_Token,Access_Token_Secret)
b=tweepy.API(a)
print(b.search("#sanju"))
user=b.get_user("@IshikaG62386743")
print(user.screen_name)
print(user.followers_count)
def tweet_status():
    mm=input("What is hapenning?.........thweet here.......")
    b.update_status(mm)
c=b.user_timeline(screen_name="@IshikaG62386743",count=200,tweet_node="extended")
print(c)