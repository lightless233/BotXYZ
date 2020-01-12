#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    tools
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    $END$

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017-2020 lightless. All rights reserved
"""

import random

from data.base_data import (PropertyConverter, BaseData, PropNames)


class PropertiesTools:

    @staticmethod
    def d20():
        return random.randint(1, 20)

    @staticmethod
    def d4():
        return random.randint(1, 4)

    @staticmethod
    def calc_properties(level, _str, vit, agi):
        # 根据一级属性计算出二级属性的值

        """
        ATK = base_atk + (Level-1)*LEVEL_TO_ATK + STR*STR_TO_ATK
        DEF = base_def + (level-1)*LEVEL_TO_DEF + VIT*VIT_TO_DEF + STR*STR_TO_DEF
        HP = base_hp + (level-1)*LEVEL_TO_HP + STR*STR_TO_HP + VIT*VIT_TO_HP
        SP = base_sp + (level-1)*LEVEL_TO_SP + VIT*VIT_TO_SP
        CRI = base_cri + agi * AGI_TO_CRI
        EVA = base_eva + agi * AGI_TO_EVA
        HIT = base_hit + agi * AGI_TO_HIT
        """

        # ATK计算
        LEVEL_TO_ATK = PropertyConverter.get("LEVEL", "ATK")
        STR_TO_ATK = PropertyConverter.get("STR", "ATK")
        final_atk = BaseData.BASE_ATK + (level - 1) * LEVEL_TO_ATK + _str * STR_TO_ATK

        # DEF计算
        LEVEL_TO_DEF = PropertyConverter.get("LEVEL", "DEF")
        VIT_TO_DEF = PropertyConverter.get("VIT", "DEF")
        STR_TO_DEF = PropertyConverter.get("STR", "DEF")
        final_def = BaseData.BASE_DEF + (level - 1) * LEVEL_TO_DEF + _str * STR_TO_DEF + vit * VIT_TO_DEF

        # HP 计算
        LEVEL_TO_HP = PropertyConverter.get("LEVEL", "HP")
        STR_TO_HP = PropertyConverter.get("STR", "HP")
        VIT_TO_HP = PropertyConverter.get("VIT", "HP")
        final_hp = BaseData.BASE_HP + (level - 1) * LEVEL_TO_HP + _str * STR_TO_HP + vit * VIT_TO_HP

        # SP 计算
        LEVEL_TO_SP = PropertyConverter.get("LEVEL", "SP")
        VIT_TO_SP = PropertyConverter.get("VIT", "SP")
        final_sp = BaseData.BASE_SP + (level - 1) * LEVEL_TO_SP + vit * VIT_TO_SP

        # CRI
        AGI_TO_CRI = PropertyConverter.get("AGI", "CRI")
        final_cri = BaseData.BASE_CRI + agi * AGI_TO_CRI

        # EVA
        AGI_TO_EVA = PropertyConverter.get(PropNames.AGI, PropNames.EVA)
        final_eva = BaseData.BASE_EVA + agi * AGI_TO_EVA

        # HIT
        AGI_TO_HIT = PropertyConverter.get(PropNames.AGI, PropNames.HIT)
        final_hit = BaseData.BASE_HIT + agi * AGI_TO_HIT

        return {
            "atk": final_atk,
            "def": final_def,
            "hp": final_hp,
            "sp": final_sp,
            "cri": final_cri,
            "hit": final_hit,
            "eva": final_eva,
        }
