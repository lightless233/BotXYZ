#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    news
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    $END$

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017-2020 lightless. All rights reserved
"""
import datetime

from peewee import TextField, IntegerField, DateTimeField

from . import BaseModel


class NewsModel(BaseModel):
    class Meta:
        table_name = "xyz_news"

    title = TextField()
    url = TextField()
    has_send = IntegerField(default=0)
    created_time = DateTimeField(default=datetime.datetime.now())
    updated_time = DateTimeField(default=datetime.datetime.now())
