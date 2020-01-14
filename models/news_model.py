#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    news_model
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    $END$

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017-2020 lightless. All rights reserved
"""
from peewee import TextField

from . import BaseModel


class NewsModel(BaseModel):
    class Meta:
        table_name = "xyz_news"

    title = TextField()

