#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Function:
【整理】关于http(GET或POST)请求中的url地址的编码和解码
http://www.crifan.com/summary_the_url_encode_and_decode_during_http_get_post_request
 
Version:    2012-11-20
Author:     Crifan
"""

import urllib;
 
encodedUrl_1 = "http://aigis.gcwiki.info/?%BB%FC%B0%A6%A4%CE%B5%A7%A4%EA%A5%B5%A1%BC%A5%EA%A5%A2";
decodedUrl_1 = urllib.unquote(encodedUrl_1);
print "encodedUrl=\t%s\r\ndecodedUrl=\t%s"%(encodedUrl_1, decodedUrl_1);
#encodedUrl=     
#decodedUrl=     

words = u'中文'
print words
check_words = isinstance(words, unicode)
print check_words
try:
    search_words = words.encode('GBK')
except ValueError, e:
    print 'Error:', e
    search_words = 'wrong'
print search_words

decodedUrl_2 = "http://index.baidu.com/?tpl=trend&type=0&area=0&time=12&word=" + search_words;
encodedUrl_2 = urllib.quote(decodedUrl_2, safe='/'+':'+'='+'&'+'?');
print "encodedUrl=\t%s\r\ndecodedUrl=\t%s"%(encodedUrl_2, decodedUrl_2);
#encodedUrl=     
#decodedUrl=    

a = raw_input()
print a