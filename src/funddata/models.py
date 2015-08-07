
# import all related package
from django.db import models
from django.utils.encoding import smart_unicode

import sys
import urllib2
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtWebKit import *
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf8')

CANDIDATE_LINK = 'http://www.jisilu.cn/data/sfnew/#tlink_3'
MATCH_TYPES = [['tr', 'odd'], ['tr', 'even']]

# Create your models here.
class ShowData(models.Model):
  fund_id = models.CharField(max_length=120, null=True, blank=True)
  fund_name = models.CharField(max_length=120, null=True, blank=True)
  fund_current_price = models.CharField(max_length=120, null=True, blank=True)
  fund_growth_rate = models.CharField(max_length=120, null=True, blank=True)
  fund_turnover = models.CharField(max_length=120, null=True, blank=True)
  fund_net_value = models.CharField(max_length=120, null=True, blank=True)
  fund_discount_rate = models.CharField(max_length=120, null=True, blank=True)
  fund_interest_rule = models.CharField(max_length=120, null=True, blank=True)
  fund_current_interest_rate = models.CharField(max_length=120, null=True, blank=True)
  fund_next_intereste_rate = models.CharField(max_length=120, null=True, blank=True)
  fund_fixed_yield = models.CharField(max_length=120, null=True, blank=True)
  fund_remaining_period = models.CharField(max_length=120, null=True, blank=True)
  fund_reference_index = models.CharField(max_length=120, null=True, blank=True)
  fund_index_growth_rate = models.CharField(max_length=120, null=True, blank=True)
  fund_to_discount_required_rate = models.CharField(max_length=120, null=True, blank=True)
  fund_discount_yield = models.CharField(max_length=120, null=True, blank=True)
  first_name = models.CharField(max_length=120, null=True, blank=True)
  fund_overrall_rate = models.CharField(max_length=120, null=True, blank=True)
  fund_T1_rate = models.CharField(max_length=120, null=True, blank=True)
  fund_T2_rate = models.CharField(max_length=120, null=True, blank=True)
  fund_A_share = models.CharField(max_length=120, null=True, blank=True)
  fund_A_increased_share = models.CharField(max_length=120, null=True, blank=True)
  fund_AB_ratio = models.CharField(max_length=120, null=True, blank=True)
  fund_next_rate_date = models.DateTimeField(auto_now_add=True, auto_now=False)
  def __unicode__(self):
  	return smart_unicode(fund_name)

#class for render page to pyqt and return html for analysis
class URLRender(QWebPage):
	def __init__(self, url):
		self.app = QApplication(sys.argv)
		QWebPage.__init__(self)
		self.loadFinished.connect(self._loadFinished)
		self.mainFrame().load(QUrl(url))
		self.app.exec_()
	def _loadFinished(self, result):
		self.frame = self.mainFrame()
		self.app.quit()

## Fetch data 
def FetchData(CANDIDATE_LINK, MATCH_TYPES): 
	rendered_url = URLRender(CANDIDATE_LINK)
	html = rendered_url.frame.toHtml()
	html = str(html)
	parsed_html = BeautifulSoup(html)
	for match_type in MATCH_TYPES:
		sections = parsed_html.find_all(match_type[0], attrs={match_type[1]})
		for section in sections:
			print section.get_text(',')

fectch_data = FetchData(CANDIDATE_LINK, MATCH_TYPES)			
## need to cast data to data base here