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


class HelpCommand(BaseCommand):

    def __init__(self, api: CQPlusApi, logger: CQPlusLogging):
        super(HelpCommand, self).__init__(api, logger)

        self.command_name = "%help"

    def process(self, from_group: int, from_qq: int, command_list: List[str]):
        help_msg = "BotXYZ version 1.0.0\n\n" \
                   "命令列表:\n" \
                   "%help - 显示这个页面"

        self.api.send_group_msg(group_id=from_group, msg=help_msg)
