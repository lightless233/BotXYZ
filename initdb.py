#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    initdb
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    $END$

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017-2020 lightless. All rights reserved
"""
from peewee import DoesNotExist

from models import db
from models.ExpModel import ExpModel
from models.PlayerModel import PlayerInfoModel


db.connect()
db.create_tables([
    ExpModel,
    PlayerInfoModel,
])

for level in range(1, 50):
    exp = (level - 1) * 20 + 100
    ExpModel.create(level=level, exp=exp)

