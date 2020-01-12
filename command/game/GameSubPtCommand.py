#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    GameSubPtCommand
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
from models.player import PlayerInfoModel
from models.service import PlayerInfoService
from utils import utils


class GameSubPtCommand(BaseCommand):
    def __init__(self, api: CQPlusApi, logger: CQPlusLogging):
        super(GameSubPtCommand, self).__init__(api, logger)

        self.command_name = "%game pt"

        self.err_msg = "%game pt STR 1"

        self.available_prop = ["STR", "VIT", "AGI"]

        self.player_info_service = PlayerInfoService()

    def send_err_msg(self, msg=None):
        if msg is None:
            self.send_msg(utils.build_at_msg(self.from_qq) + f"\n格式错误！{self.err_msg}")
        else:
            self.send_msg(utils.build_at_msg(self.from_qq) + f"\n{msg}")

    def process(self, from_group: int, from_qq: int, command_list: List[str]):
        """
        点数分配
        :param from_group:
        :param from_qq:
        :param command_list:
        """

        # 初始化数据
        self.from_qq = from_qq
        self.from_group = from_group

        # 获取参数
        try:
            prop = command_list[2]
            pt = int(command_list[3])
        except (IndexError, ValueError):
            self.send_err_msg()
            return

        if prop.upper() not in self.available_prop:
            self.send_err_msg()
            return

        # 获取这个玩家的所有剩余PT
        pc: PlayerInfoModel = self.player_info_service.get_player_info_by_qq(from_qq)
        if pc is None:
            self.send_err_msg("无此玩家")
            return
        player_rest_pt = pc.rest_pt
        if pt < 0 or pt > player_rest_pt:
            self.send_err_msg("PT点数不足")
            return

        """
        更新PT，要一起更新其他数值
        """
        if self.player_info_service.update_player_prop(prop, from_qq, pt) is None:
            self.send_err_msg()
            return
        else:
            self.send_msg(utils.build_at_msg(from_qq) + "\n点数分配成功！")
