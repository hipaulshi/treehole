#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# Created at Mar 20 19:50 by BlahGeek@Gmail.com

import sys
if hasattr(sys, 'setdefaultencoding'):
    sys.setdefaultencoding('UTF-8')

import logging
from treehole.renren import RenRen
from treehole.settings import COOKIE, PAGE_ID
import os
from ipaddr import IPNetwork, IPAddress

def checkIP(addr):
    IPS = (
            IPNetwork('59.66.0.0/16'), 
            IPNetwork('166.111.0.0/16'), 
            IPNetwork('101.5.0.0/16'), 
            IPNetwork('219.223.160.0/19'), 
            # private address
            IPNetwork('127.0.0.0/8'), 
            IPNetwork('10.0.0.0/8'), 
            IPNetwork('192.168.0.0/16'), 
            )
    return any([IPAddress(addr) in x for x in IPS])

def postStatu(status, number):
    text = '#' + str(number) + ' ' + status
    r = RenRen(PAGE_ID)
    r.loginByCookie(COOKIE)
    r.setStatu(text)

MSG = {
        'IP_NOT_VALID': '不允许您的IP发布', 
        'CONTENT_TOO_LONG': '状态长度应该在6-100字之间', 
        'TOO_MANY_TIMES': '每个IP相邻发布时间不能小于30分钟', 
        'PUBLISH_ERROR': '服务器错误，发布失败', 
        'PUBLISH_OK': '发布成功！'}
