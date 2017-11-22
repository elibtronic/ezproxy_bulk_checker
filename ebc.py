#
# EzProxy Bulk URL checker
#
# Utilizes the _ProxyURLPassword_ directive to cmake a bulk check of urls

from settings import *
import requests
import xml.etree.cElementTree as ET

u_file = open("urls.txt","r")

#String to change to XML
post_start = '<?xml version="1.0"?>\n<proxy_url_request password="'+PROXY_URL_REQUEST_PASSWORD+'">\n<urls>\n'
post_middle = ""
for u in u_file:
	post_middle += "<url>"+u.strip('\n')+"</url>\n"
post_end = "</urls>\n</proxy_url_request>"
post_data = post_start+post_middle+post_end
u_file.close()

xml_post = ET.fromstring(post_data)
r = requests.post(PROXY_URL,post_data)
check_results = ET.fromstring(r.text)

good_urls = open("good.txt","w")
bad_urls = open("bad.txt","w")

for u in check_results[0]:
	print(u.text+" ... ",end="")
	if u.attrib['proxy'] == "true":
		print("good")
		good_urls.write(u.text+'\n')
	else:
		print("bad")
		bad_urls.write(u.text+'\n')
	
print("fin")
