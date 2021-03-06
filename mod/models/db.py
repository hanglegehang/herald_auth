#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-10-26 12:50:52
# @Author  : yml_bright@163.com

import os

DB_HOST = 'localhost'
DB_USER = 'herald_auth'
DB_PWD = 'herald'
DB_NAME = 'herald_auth'

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
dbengine = create_engine('mysql://%s:%s@%s/%s?charset=utf8' %
                       (DB_USER, DB_PWD, DB_HOST, DB_NAME),
                       encoding='utf-8', echo=False,
                       pool_size=100, pool_recycle=10)