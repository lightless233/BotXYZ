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
from models.player import PlayerInfoModel
from utils.tools import PropertiesTools


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
            query.execute()

            # 一级属性更新完成，计算二级属性
            pc: PlayerInfoModel = self.get_player_info_by_qq(qq)
            new_props = PropertiesTools.calc_properties(pc.level, pc.base_str, pc.base_vit, pc.base_agi)
            query = PlayerInfoModel.update(
                hp_max=new_props.get("hp"), sp_max=new_props.get("sp"), atk=new_props.get("atk"),
                defe=new_props.get("def"), cri=new_props.get("cri"), hit=new_props.get("hit"),
                eva=new_props.get("eva"),
            ).where(PlayerInfoModel.qq == qq)

            return query.execute()

    def update_player_hp(self, qq, value):
        with db:
            query = PlayerInfoModel.update(
                hp_current=PlayerInfoModel.hp_current + value
            ).where(PlayerInfoModel.qq == qq)
            return query.execute()

    def update_player_sp(self, qq, value):
        with db:
            query = PlayerInfoModel.update(
                sp_current=PlayerInfoModel.sp_current + value
            ).where(PlayerInfoModel.qq == qq)
            return query.execute()
