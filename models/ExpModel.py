#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    ExpModel
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    $END$

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017-2020 lightless. All rights reserved
"""
from peewee import SqliteDatabase, Model, BigIntegerField, IntegerField, CharField
from . import db, BaseModel


class ExpModel(BaseModel):

    class Meta:
        table_name = "xyz_exp"

    level = IntegerField()
    exp = IntegerField()
