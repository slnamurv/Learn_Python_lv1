# -*- coding: utf-8 -*-  
   
import string;
import urllib, urllib2;
   
#定义百度函数  
def chinaz_seo(url):     
    #i += 1
    sName = string.zfill('1',5) + '.html'#自动填充成六位的文件名  
    print '正在下载第' + str(1) + '个网页，并将其存储为' + sName + '......'  
    f = open(sName,'w+')  
    m = urllib2.urlopen(url).read()  
    f.write(m)
    f.close()  
   
   
#-------- 初始化参数 ------------------  
i = 0
#-------- 在这里输入参数 ------------------  
  
# 中国外汇交易中心首页SEO
#search_url = 'http://seo.chinaz.com/?m=&host=www.chinamoney.com.cn'  

search_url = 'http://seo.chinaz.com/?m=&host=' + str(raw_input('请输入地址：\n'))  
#-------- 在这里输入参数 ------------------  
   
  
#调用  
chinaz_seo(search_url)  