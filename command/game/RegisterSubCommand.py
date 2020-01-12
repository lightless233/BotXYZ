#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    RegisterSubCommand
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
from models.player import PlayerInfoModel
from utils import utils


class RegisterSubCommand(BaseCommand):

    def __init__(self, api: CQPlusApi, logger: CQPlusLogging):
        super(RegisterSubCommand, self).__init__(api, logger)

        self.command_name = "%game register"

        self.err_msg = "%game register your_nick_name"

    def process(self, from_group: int, from_qq: int, command_list: List[str]):
        # %game register lightless233

        # 初始化数据
        self.from_qq = from_qq
        self.from_group = from_group

        # 1 检查该QQ是否已经有角色了
        has_pc = False
        with db:
            try:
                PlayerInfoModel.get(PlayerInfoModel.qq == from_qq)
                has_pc = True
            except DoesNotExist:
                pass
        if has_pc:
            self.send_msg(
                utils.build_at_msg(from_qq) +
                "\n已经有角色啦！暂不支持多个角色！"
            )
            return

        # 2 创建角色
        try:
            nickname = command_list[2]
        except IndexError:
            self.send_msg(
                utils.build_at_msg(from_qq) +
                f"\n格式：{self.err_msg}"
            )
            return

        with db:
            player = PlayerInfoModel()
            player.qq = from_qq
            player.nickname = nickname
            player.save()

        self.send_msg(
            utils.build_at_msg(from_qq) +
            "\n注册成功！"
        )
