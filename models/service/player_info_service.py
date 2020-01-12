#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    PlayerInfoService
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    $END$

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017-2020 lightless. All rights reserved
"""
from peewee import DoesNotExist

from models import db
from models.PlayerModel import PlayerInfoModel


class PlayerInfoService:

    def __init__(self):
        super(PlayerInfoService, self).__init__()

    def get_player_info_by_qq(self, qq):
        with db:
            try:
                return PlayerInfoModel.get(PlayerInfoModel.qq == qq)
            except DoesNotExist:
                return None

    def update_player_prop(self, prop, qq, pt):
        with db:
            if prop == "STR":
                query = PlayerInfoModel \
                    .update(base_str=PlayerInfoModel.base_str + pt, rest_pt=PlayerInfoModel.rest_pt - pt) \
                    .where(PlayerInfoModel.qq == qq)
            elif prop == "AGI":
                query = PlayerInfoModel \
                    .update(base_agi=PlayerInfoModel.base_agi + pt, rest_pt=PlayerInfoModel.rest_pt - pt) \
                    .where(PlayerInfoModel.qq == qq)
            elif prop == "VIT":
                query = PlayerInfoModel \
                    .update(base_vit=PlayerInfoModel.base_vit + pt, rest_pt=PlayerInfoModel.rest_pt - pt) \
                    .where(PlayerInfoModel.qq == qq)
            else:
                return None

            return query.execute()
