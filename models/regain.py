#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    RegainModel
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    $END$

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017-2020 lightless. All rights reserved
"""
from peewee import BigIntegerField, DateTimeField

from . import BaseModel


class RegainModel(BaseModel):
    class Meta:
        table_name = "xyz_regain"

    qq = BigIntegerField()
    hp_next_time = DateTimeField(default="2020-01-01 00:00:00")
    sp_next_time = DateTimeField(default="2020-01-01 00:00:00")
