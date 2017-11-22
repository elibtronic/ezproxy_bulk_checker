#
# EzProxy Bulk URL checker
#
# Utilizes the _ProxyURLPassword_ directive to cmake a bulk check of urls

from settings import *
import requests
import xml.etree.cElementTree as ET
from urllib.parse import urlparse
import re,sys


if __name__ == "__main__":
	u_file = open(sys.argv[1],"r")
	#String to change to XML
	post_start = '<?xml version="1.0"?>\n<proxy_url_request password="'+PROXY_URL_REQUEST_PASSWORD+'">\n<urls>\n'
	post_middle = ""
	for u in u_file:
		if re.search("├",u):
			next
		parsed_uri = urlparse(u)
		u_clean = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)
		post_middle += "<url>"+u_clean.strip('\n"')+"</url>\n"
	post_end = "</urls>\n</proxy_url_request>"
	post_data = post_start+post_middle+post_end
	u_file.close()

	xml_post = ET.fromstring(post_data)
	r = requests.post(PROXY_URL,post_data)
	check_results = ET.fromstring(r.text)

	good_urls = open("good.txt","a")
	bad_urls = open("bad.txt","a")


	for u in check_results[0]:
		print(u.text+" ... ",end="")
		if u.attrib['proxy'] == "true":
			print("good")
			good_urls.write(u.text+'\n')
		else:
			print("bad")
			bad_urls.write(u.text+'\n')
		
