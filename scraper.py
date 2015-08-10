import sys
import urllib2
import json
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
from bs4 import BeautifulSoup
# used for ascii coding
reload(sys)
sys.setdefaultencoding('utf8')


def getsoup(link, tag, attrs={}):
	page = urllib2.urlopen(link)
	parsed_html = BeautifulSoup(page)
	sections = parsed_html.find_all(tag, attrs)
	return sections

# link 
testlink = 'http://www.dealmoon.com/search?lang=en&q=shoes'
#print getsoup(testlink, tag='p', attrs={'class':'tw_text'})

#jisilu link 
jisilulink = 'http://www.jisilu.cn/data/sfnew/#tlink_3'
#print getsoup(jisilulink, tag='tr', attrs={'class':'even'})
page = urllib2.urlopen(jisilulink)
#parsed_html = BeautifulSoup(page)
#print parsed_html
# print page
# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         print "Encountered a start tag:", tag
#     def handle_endtag(self, tag):
#         print "Encountered an end tag :", tag
#     def handle_data(self, data):
#         print "Encountered some data  :", data

# parser = MyHTMLParser()
# parser.feed(page)
class Render(QWebPage):
	def __init__(self, url):
		self.app = QApplication(sys.argv)
		QWebPage.__init__(self)
		self.loadFinished.connect(self._loadFinished)
		self.mainFrame().load(QUrl(url))
		self.app.exec_()
	def _loadFinished(self, result):
		self.frame = self.mainFrame()
		self.app.quit()

r = Render(jisilulink)
html = r.frame.toHtml()
html = str(html)
parsed_html = BeautifulSoup(html)
oddsections = parsed_html.find_all('tr', attrs={'odd'})
evensections = parsed_html.find_all('tr', attrs={'even'})
#file = open('parsed_data.txt', "wb")
result =[] 
for oddsection in oddsections:
	print oddsection.get_text(',')
	#file.write(oddsection.get_text(',').strip()+"\n")
for evensection in evensections:
	print evensection.get_text(',')
#	file.write(evensection.get_text(',').strip()+"\n")
#file.flush()
#file.close()
