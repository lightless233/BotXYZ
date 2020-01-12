#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    StatusSubCommand
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
from peewee import DoesNotExist

from command import BaseCommand
from models import db
from models.PlayerModel import PlayerInfoModel
from utils import utils


class StatusSubCommand(BaseCommand):

    def __init__(self, api: CQPlusApi, logger: CQPlusLogging):
        super(StatusSubCommand, self).__init__(api, logger)

        self.command_name = "%game status"

        self.err_msg = "%game status [@qq/nickname]"

    def convert(self, n, decimals=0):
        multiplier = 10 ** decimals
        return int(n * multiplier) / multiplier

    def process(self, from_group: int, from_qq: int, command_list: List[str]):

        # 初始化数据
        self.from_qq = from_qq
        self.from_group = from_group
        target_pc = None
        target_type = None
        show_self = False

        try:
            target_pc = command_list[2]
            # 没异常，说明要查看其他人的数据
            result = utils.get_qq_from_at_msg(target_pc)
            if result == None:
                target_type = "NICKNAME"
            else:
                target_type = "QQ"

        except IndexError:
            # 没有指定参数，查看自己的数据
            target_pc = from_qq
            target_type = "QQ"
            show_self = True

        # 开始查询数据
        with db:
            try:
                if target_type == "QQ":
                    pc_result: PlayerInfoModel = PlayerInfoModel.get(
                        PlayerInfoModel.qq == target_pc
                    )
                else:
                    pc_result: PlayerInfoModel = PlayerInfoModel.get(
                        PlayerInfoModel.nickname == target_pc
                    )
            except DoesNotExist:
                # 查无此人
                self.send_msg(
                    utils.build_at_msg(from_qq) +
                    "\n无此人数据！"
                    "\n请确认目标是否正确，或请先执行%game register nickname进行注册！"
                )
                return

        # 格式化数据
        data_msg = "Nickname: " + pc_result.nickname + "\n"
        if show_self:
            data_msg += f"Rest PT: {pc_result.rest_pt}\n"
        data_msg += f"Level: {pc_result.level}\n" \
                    f"Exp: {pc_result.exp}\n" \
                    f"==========\n" \
                    f"STR: {pc_result.base_str}\n" \
                    f"VIT: {pc_result.base_vit}\n" \
                    f"AGI: {pc_result.base_agi}\n" \
                    f"LUK: {pc_result.base_luck}\n" \
                    f"==========\n" \
                    f"HP: {pc_result.hp_current} / {pc_result.hp_max}\n" \
                    f"SP: {pc_result.sp_current} / {pc_result.sp_max}\n" \
                    f"ATK: {pc_result.atk}\n" \
                    f"DEF: {pc_result.defe}\n" \
                    f"CRI: {self.convert(pc_result.cri * 100, 2)}%\n" \
                    f"HIT: {self.convert(pc_result.hit * 100, 2)}%\n" \
                    f"EVA: {self.convert(pc_result.eva * 100, 2)}%\n" \
                    f"=========="
        self.send_msg(utils.build_at_msg(from_qq) + "\n" + data_msg)
