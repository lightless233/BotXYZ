#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    PlayerModel
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    $END$

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017-2020 lightless. All rights reserved
"""
from peewee import BigIntegerField, IntegerField, CharField

from data.BaseData import BaseData
from . import BaseModel


class PlayerInfoModel(BaseModel):

    class Meta:
        table_name = "xyz_player_info"

    # 基本信息
    qq = BigIntegerField()
    nickname = CharField()
    level = IntegerField(default=1)
    rest_pt = IntegerField(default=3)

    # 当前的经验值
    # 每升一级，清零
    exp = IntegerField(default=0)

    # 一级属性
    base_str = IntegerField(default=0)
    base_vit = IntegerField(default=0)
    base_agi = IntegerField(default=0)
    base_luck = IntegerField(default=0)

    # 二级属性
    hp_max = IntegerField(default=BaseData.BASE_HP)
    hp_current = IntegerField(default=BaseData.BASE_HP)
    sp_max = IntegerField(default=BaseData.BASE_SP)
    sp_current = IntegerField(default=BaseData.BASE_SP)
    atk = IntegerField(default=BaseData.BASE_ATK)
    defe = IntegerField(default=BaseData.BASE_DEF)
    cri = IntegerField(default=BaseData.BASE_CRI)
    hit = IntegerField(default=BaseData.BASE_HIT)
    eva = IntegerField(default=BaseData.BASE_EVA)
