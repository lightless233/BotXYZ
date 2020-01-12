#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    GameSubAttackCommand
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    $END$

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017-2020 lightless. All rights reserved
"""
from typing import List

from cqplus._api import CQPlusApi
from cqplus._logging import CQPlusLogging

from command import BaseCommand


class GameSubAttackCommand(BaseCommand):
    def __init__(self, api: CQPlusApi, logger: CQPlusLogging):
        super(GameSubAttackCommand, self).__init__(api, logger)

        self.command_name = "%game attack"

        self.err_msg = "%game attack @qq [skill]"

    def process(self, from_group: int, from_qq: int, command_list: List[str]):
        """
        1. 检查攻击方的SP点数
        2. 检查目标是否存活
        3. 伤害结算
            3.0 SP结算
            3.1 命中计算
            3.2 暴击结算
            3.3 伤害结算
        4. 经验结算
            4.1 升级结算
        5. 死亡结算
        6. 道具掉落结算
        """
        pass
