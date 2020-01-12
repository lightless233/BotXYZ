#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    HelpCommand.py
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

from ._base import BaseCommand

help_msg = """BotXYZ version 1.0.1

--- 普通命令 ---
%help - 显示这个页面
%attack - 攻击某个玩家，格式：%attack @目标 时长(分钟)
%game - 游戏命令
%news - 每日新闻 (Author: WinFog)
---------------

--- Admin命令 ---
%ban - 干掉指定人，格式：%ban @目标 时长(分钟)
%unban - 解封指定人，格式：%unban @目标
---------------

--- 其他信息 ---
项目地址：https://github.com/lightless233/BotXYZ
Bug、Request报告地址：https://github.com/lightless233/BotXYZ/issues
---------------
"""


class HelpCommand(BaseCommand):

    def __init__(self, api: CQPlusApi, logger: CQPlusLogging):
        super(HelpCommand, self).__init__(api, logger)

        self.command_name = "%help"

    def process(self, from_group: int, from_qq: int, command_list: List[str]):
        self.api.send_group_msg(group_id=from_group, msg=help_msg)
