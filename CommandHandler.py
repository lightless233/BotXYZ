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

import constant
from utils import utils


class CommandHandler:

    def __init__(self, api, logger):
        super(CommandHandler, self).__init__()

        self.logger: CQPlusLogging = logger
        self.api: CQPlusApi = api

    def __check_admin(self, from_qq):
        return from_qq in constant.ADMIN_QQ

    def handler(self, msg: str, from_group: int, from_qq: int):

        command_list = msg.split(" ")
        command = command_list[0]

        if command == "%help":
            self.help(from_group, from_qq)
        elif command == "%ban":
            self.ban(from_group, from_qq, command_list)
        elif command == "%unban":
            self.ubban(from_group, from_qq, command_list)
        else:
            self.api.send_group_msg(group_id=from_group, msg=utils.build_at_msg(from_qq) + "\nUnknown Command!")

    def help(self, from_group, from_qq):
        help_msg = "BotXYZ version 1.0.0\n\n" \
                   "Command List:\n" \
                   "%help - show this message"

        self.api.send_group_msg(group_id=from_group, msg=help_msg)


    def ban(self, from_group, from_qq, command_list):
        if not self.__check_admin(from_qq):
            self.api.send_group_msg(from_group, "You are not admin!\n" + utils.build_at_msg(from_qq))
            self.api.set_group_ban(from_group, from_qq, 60)
            return
        try:
            target_qq = command_list[1]
            duration = command_list[2]
        except IndexError:
            self.api.send_group_msg(from_group, utils.build_at_msg(from_qq) + "\nError arguments.\n%ban qq duration(min.)")
            return

        at_qq = utils.get_qq_from_at_msg(target_qq)
        if at_qq is None:
            self.api.set_group_ban(group_id=from_group, user_id=int(target_qq), duration=int(duration) * 60)
        else:
            self.api.set_group_ban(group_id=from_group, user_id=int(at_qq), duration=int(duration) * 60)
        self.api.send_group_msg(from_group, utils.build_at_msg(from_qq) + "\nBan operation success!")

    def ubban(self, from_group, from_qq, command_list):
        if not self.__check_admin(from_qq):
            self.api.send_group_msg(from_group, "You are not admin!\n" + utils.build_at_msg(from_qq))
            self.api.set_group_ban(from_group, from_qq, 60)
            return

        try:
            target_qq = command_list[1]
        except IndexError:
            self.api.send_group_msg(from_group,
                                    utils.build_at_msg(from_qq) + "\nError arguments.\n%unban qq")
            return

        at_qq = utils.get_qq_from_at_msg(target_qq)
        if at_qq is None:
            self.api.set_group_ban(group_id=from_group, user_id=int(target_qq), duration=0)
        else:
            self.api.set_group_ban(group_id=from_group, user_id=int(at_qq), duration=0)
        self.api.send_group_msg(from_group, utils.build_at_msg(from_qq) + "\nUnban operation success!")
