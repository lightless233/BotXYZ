#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    __init__.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    $END$

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017-2020 lightless. All rights reserved
"""
from peewee import SqliteDatabase, Model

from data.base_data import DATABASE_PATH

db = SqliteDatabase(DATABASE_PATH, autoconnect=False)


class BaseModel(Model):
    class Meta:
        database = db
