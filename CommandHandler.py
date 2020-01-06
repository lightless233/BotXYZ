#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    CommandHandler
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    $END$

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017-2020 lightless. All rights reserved
"""

from cqplus._api import CQPlusApi
from cqplus._logging import CQPlusLogging

from utils import utils


class CommandHandler:

    def __init__(self, api, logger):
        super(CommandHandler, self).__init__()

        self.logger: CQPlusLogging = logger
        self.api: CQPlusApi = api

    def handler(self, msg: str, from_group: int, from_qq: int):

        command_list = msg.split(" ")
        command = command_list[0]

        if command == "%help":
            self.help(from_group, from_qq)
        else:
            self.api.send_group_msg(group_id=from_group, msg=utils.build_at_msg(from_qq) + "\nUnknown Command!")

    def help(self, from_group, from_qq):
        help_msg = "BotXYZ version 1.0.0\n\n" \
                   "Command List:\n" \
                   "%help - show this message"

        self.api.send_group_msg(group_id=from_group, msg=help_msg)
