#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    sec_today_news_timer
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    $END$

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017-2020 lightless. All rights reserved
"""
import requests
from bs4 import BeautifulSoup

from models.news import NewsModel
from models.service import NewsService
from ._base import BaseTimer


class SecTodayNewsTimer(BaseTimer):

    def __init__(self, api, logger):
        super(SecTodayNewsTimer, self).__init__(api, logger)

        self.target_url = "https://sec.today/pulses/"

        self.news_service = NewsService()

    def process(self):
        response = requests.get(self.target_url, timeout=9)
        page_value = response.text

        # 筛选数据
        soup = BeautifulSoup(page_value)
        articles = soup.find_all("div", "my-2")
        for x in articles:
            tag_a = x.find_all("a")[0]
            href = tag_a["href"]
            full_url = self.target_url + href[1:]
            title = tag_a.text

            # 检查这个新闻有没有入过库了
            # 如果没有，就入库
            # 如果已经入库了，那么看看有没有发送过了，如果没发过就发出去，并更新状态
            self.save(title, full_url)

    def save(self, title, url):
        news: NewsModel = self.news_service.get_news_by_url(url)
        if news is not None:
            has_send = news.has_send
            if has_send == 0:
                self.send_and_update(news)
        else:
            news = self.news_service.save(title, url, 1)
            self.send_and_update(news)

    def send_and_update(self, news: NewsModel):
        message = news.title + "\n" + news.url
        self.api.send_group_msg("672534169", message)
        self.news_service.update_send(news.title, news.url, 1)
