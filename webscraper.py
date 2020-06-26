import json
import requests
from bs4 import BeautifulSoup
url="https://en.wikipedia.org/wiki/Manchester_United_F.C."
r=requests.get(url)
#print(r)
#Responses: 100 information, 200, accept: 300, redirect, 400: Mistake from my pc, 500: Mistake from the server's side.
soup=BeautifulSoup(r.content,'html.parser')#What are html-parser & lxml
# print(soup)#-> returns the page source text
# print(soup.prettify())#-> formatted alignmentke saath
#print(soup.text.count("Man"))
#print(dir(soup))#->Helps with remembering the specific attributes of an object.
# print(type(soup))
# print(r.raw)
# print(r.text.count('Manchester_United_F.C.'))

#Find that image ka path ka tag on that manutd....# QUESTION:
soup=BeautifulSoup(r.content,'html.parser')
# print(soup.find_all("div", attrs = {'class': 'thumbinner'})
#print(dir(soup.find("div",attrs = {'class': 'thumbinner'}) ))

#Solution:
div_tag = soup.find("div", { "class" : "thumbinner" })
for images in div_tag.findAll("img"):
    print(images)


# Server side scraping easily hojata hai cuz the entire thing goes in the soup vs client side scraping.
# Client side mai problem hoga how to deal with it. eg INSTAGRAM.
# https://medium.com/@mahmudahsan/how-to-scrap-data-from-javascript-based-website-using-python-selenium-and-headless-web-driver-531c7fe0c01f
#use waituntil from selenium...then use bueatiful soup.
#
# Can't directly scrape iframe how to deal with it?
# https://stackoverflow.com/questions/54522364/python-beautifulsoup-scrape-web-content-inside-iframes?fbclid=IwAR2voxy3wq1d9KxEt3gSoH_c1vSaiUI10_GlF0M2BZ5xeKFMlrXQ6zFPyoc
# inspect element + one more get request.
#
# https status codes:https://www.restapitutorial.com/httpstatuscodes.html
# Method 1:429 status code. Can handle 429 alagse.
# Method 2: .sleep(1) kardo. Disadvantage: Won't get dynamic data. TO avoid that: New user pose...with proxy
#How to avoid getting banned: https://www.scraperapi.com/blog/5-tips-for-web-scraping
