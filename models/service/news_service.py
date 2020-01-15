#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    news_service
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    $END$

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017-2020 lightless. All rights reserved
"""
import datetime

from peewee import DoesNotExist

from models import db
from models.news import NewsModel


class NewsService:

    def __init__(self):
        super(NewsService, self).__init__()

    def get_news_by_url(self, url):
        with db:
            try:
                return NewsModel.get(NewsModel.url == url)
            except DoesNotExist:
                return None

    def save(self, title, url, has_send=0):
        with db:
            return NewsModel.create(
                url=url,
                title=title,
                has_send=has_send
            )

    def update_send(self, title, url, has_send):
        with db:
            query = NewsModel.update(has_send=has_send) \
                .where(NewsModel.title == title, NewsModel.url == url)

            return query.execute()

    def get_today_news(self):

        now = datetime.datetime.now()

        with db:
            try:
                return NewsModel.select().where(
                    (NewsModel.created_time.year == now.year)
                    & (NewsModel.created_time.month == now.month)
                    & (NewsModel.created_time.day == now.day)
                )
            except DoesNotExist:
                return None
