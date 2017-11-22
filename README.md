
# Ezproxy Bulk URL Checker

Makes use of the [EZproxy](https://www.oclc.org/en/ezproxy.html)  _ProxyURLPassword_ directive.

When provided with a `txt` file of urls it will check the `/proxy_url` service to see if the URL is in the allow list. One off demo [here](http://elibtronic.ca/code/proxy-checker-demo). Details of why [here](http://elibtronic.ca/content/20080821/checking-urls-connecting-ezproxy)


1. `cp settings.orig setting.py` and fill in the URL of your proxy server and the password you set to use the service

1. `urls.txt`in the directory.

1. `python3 ebc.py` results in `good.txt` and `bad.txt`


X-X-Xml yall!
