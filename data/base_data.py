#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    BaseData
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    $END$

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017-2020 lightless. All rights reserved
"""

class BaseData:
    BASE_HP = 50
    BASE_SP = 10
    BASE_ATK = 10
    BASE_DEF = 10
    BASE_CRI = 0.02
    BASE_EVA = 0.04
    BASE_HIT = 0.02

class AttackParams:
    K1 = 3.2
    K2 = 0
    K3 = 0.85
    K4 = 0

    CRI_PARAM = 0.5

PropertyCovertValue:dict = {
    "STR": {
        "ATK": 1,
        "DEF": 0.4,
        "HP": 4,
        "SP": 0,
        "CRI": 0,
        "EVA": 0,
        "HIT": 0,
    },
    "VIT": {
        "ATK": 0,
        "DEF": 0.7,
        "HP": 15,
        "SP": 1,
        "CRI": 0,
        "EVA": 0,
        "HIT": 0,
    },
    "AGI": {
        "ATK": 0,
        "DEF": 0,
        "HP": 0,
        "SP": 0,
        "CRI": 0.01,
        "EVA": 0.015,
        "HIT": 0.015,
    },
    "LEVEL": {
        "ATK": 0.3,
        "DEF": 0.2,
        "HP": 2,
        "SP": 0.2,
        "CRI": 0,
        "EVA": 0,
        "HIT": 0,
    }
}

