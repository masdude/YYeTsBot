# coding: utf-8
# YYeTsBot - config.py
# 2019/8/15 18:42

__author__ = 'Benny <benny.think@gmail.com>'

import os

BASE_URL = "http://www.rrys2020.com"
LOGIN_URL = "http://www.rrys2020.com/user/login"
GET_USER = "http://www.rrys2020.com/user/login/getCurUserTopInfo"
# rss is unavailable as of 2021.01.10
RSS_URL = "http://rss.rrys.tv/rss/feed/{id}"
RESOURCE_SCORE = "http://www.rrys2020.com/resource/getScore"  # post rid=38000
SEARCH_URL = "http://www.rrys2020.com/search?keyword={kw}&type=resource"
AJAX_LOGIN = "http://www.rrys2020.com/User/Login/ajaxLogin"
SHARE_URL = "http://www.rrys2020.com/resource/ushare"
SHARE_WEB = "http://got002.com/resource.html?code={code}"
# http://got002.com/api/v1/static/resource/detail?code=9YxN91
SHARE_API = "http://got002.com/api/v1/static/resource/detail?code={code}"

TOKEN = os.environ.get("TOKEN") or "TOKEN"
USERNAME = os.environ.get("USERNAME") or "USERNAME"
PASSWORD = os.environ.get("PASSWORD") or "password"
PROXY = os.environ.get("PROXY")
MAINTAINER = os.environ.get("MAINTAINER")
REDIS = os.environ.get("REDIS") or "redis"
REPORT = os.environ.get("REPORT") or False
