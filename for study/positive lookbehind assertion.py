#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
【教程】详解Python正则表达式之： (?<=…) positive lookbehind assertion 后向匹配 /后向断言
http://www.crifan.com/detailed_explanation_about_python_regular_express_positive_lookbehind_assertion
 
Version:    2012-11-14
Author:     Crifan
"""
 
import re;
 
#提示：
#相关教程：
#【教程】详解Python正则表达式之： (?=…) lookahead assertion 前向匹配 /前向断言
#http://www.crifan.com/detailed_explanation_about_python_regular_express_lookahead_assertion
 
reLookbehindTestStr = """
fake html begin
 
some sohu blog pic url is something like this:
"http://1802.img.pp.sohu.com.cn/images/blog/2012/4/12/16/20/u173669005_13766a912eag214.jpg"
which use img.pp.sohu.com.cn as its image server.
 
<img style="text-align:center;margin:0px auto 10px;zoom:1;display:block" border="0" src="http://1821.img.pp.sohu.com.cn/images/blog/2012/4/12/16/19/u173669005_13766a7cbebg214.jpg">
 
fake html end
"""
 
# 1. (?<=...) - positive lookbehind assertion 后向匹配 /后向断言
 
# 下列的，通过普通的匹配操作，会误匹配出来前面的那个jpg图片地址
foundAllJpgUrl = re.findall(u'"(http://[\w\./]+\.jpg)"', reLookbehindTestStr);
print "foundAllJpgUrl=",foundAllJpgUrl; #foundAllJpgUrl= ['http://1802.img.pp.sohu.com.cn/images/blog/2012/4/12/16/20/u173669005_13766a912eag214.jpg', 'http://1821.img.pp.sohu.com.cn/images/blog/2012/4/12/16/19/u173669005_13766a7cbebg214.jpg']
 
# 而加上了 lookbehind assertion后，就可以精确只匹配 图片地址之前必须是 src= 的jpg图片
foundAllJpgUrl_lookbehind = re.findall(u'(?<=src=)"(http://[\w\./]+\.jpg)"', reLookbehindTestStr);
print "foundAllJpgUrl_lookbehind=",foundAllJpgUrl_lookbehind; #foundAllJpgUrl_lookbehind= ['http://1821.img.pp.sohu.com.cn/images/blog/2012/4/12/16/19/u173669005_13766a7cbebg214.jpg']