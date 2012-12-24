import urllib2
import xlrd
import mechanize
import re
import time 
import unicodedata
from bs4 import BeautifulSoup


all_posts = {}

# returns the content of the post for each article
def get_content(url):
	try:
		req = urllib2.Request(url)
		response = urllib2.urlopen(req)
		html_doc = response.read()
		soup = BeautifulSoup(html_doc)
		for each_div in soup.find_all('div'):
			div_strings = each_div.get('class')
			if(div_strings is not None):
				if(div_strings[0].find('content') > -1):
					#print each_div
					return each_div
		
	except urllib2.URLError,e:
		print e

# returns the heading of the post for each article 
def get_heading(url):
	print "returning heading"



#creates the html page 
#gets all the posts from the post_details dictionary 
#prints them in the order ..

	
def make_htmlpage(post_details):
	fo= open("greatandhra.html","w")
	fo.write("<html>")
	fo.write("<head>This is my greatandhra plonder</head><body>")
	try:
	 for key,value in post_details.iteritems():
		fo.write("<h2><b><u>")
		fo.write("<a href=\"")
		fo.write(key)
		fo.write("\">Topic Link</a> ")
		fo.write("</u></b></h2><br><br><p>")
		if(value is not None):
			fo.write(value.prettify().encode('ascii','ignore'))
		fo.write("</p><br><br><br>")
	except urllib2.URLError,e:
		print e
	fo.write("</body></html>")	
	fo.close()
	
	
	
if __name__ == "__main__":
	url="http://greatandhra.com"
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	html_doc = response.read()
	soup = BeautifulSoup(html_doc)
	for list_elements in soup.find_all('ul'):
	   list_linkelement = list_elements.find_all('a')
	   for each_element in list_linkelement: 
	    links = each_element.get('href')
	    if(links.find("viewnews") > -1):
			url_post = "http://greatandhra.com/"+links
			url_content =""
			url_content =get_content(url_post)
			all_posts[url_post] =  url_content
			print 'content added for ',url_post
			#make_htmlpage(all_posts)
			#print all_posts 
	make_htmlpage(all_posts)			
			
			
	     

