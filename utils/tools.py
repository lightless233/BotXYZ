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


class PropertiesTools:

    @staticmethod
    def d20():
        return random.randint(1, 20)

    @staticmethod
    def d4():
        return random.randint(1, 4)

    @staticmethod
    def calc_properties(level, str, vit, agi):
        pass
