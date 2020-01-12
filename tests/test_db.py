#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    test_db.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    $END$

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017-2020 lightless. All rights reserved
"""

from models.player import PlayerInfoModel

players = PlayerInfoModel.select().where(
    PlayerInfoModel.sp_max != PlayerInfoModel.sp_current,
    PlayerInfoModel.hp_max != PlayerInfoModel.hp_current
).dicts()

print(len(players))

for player in players:
    print(player)
