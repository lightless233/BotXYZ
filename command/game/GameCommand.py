#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    GameCommand
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

from command.game.StatusSubCommand import StatusSubCommand
from command.game.RegisterSubCommand import RegisterSubCommand
from .._base import BaseCommand

error_msg = """Unknown sub-command.
sub-command list:

%game register - register an player
%game status - show my status
%game attack - attack others, %game attack @qq [skill_name]
"""


class GameCommand(BaseCommand):

    def __init__(self, api: CQPlusApi, logger: CQPlusLogging):
        super(GameCommand, self).__init__(api, logger)

        self.command_name = "%game"

        self.sub_command = {
            "register": RegisterSubCommand(self.api, self.logger),
            "status": StatusSubCommand(self.api, self.logger),
        }

    def process(self, from_group: int, from_qq: int, command_list: List[str]):

        self.from_group = from_group
        self.from_qq = from_qq

        try:
            sub_command: str = command_list[1]
        except IndexError:
            self.send_msg(error_msg)
            return

        sub_command = sub_command.lower()
        if sub_command not in self.sub_command:
            self.send_msg(error_msg)
            return
        else:
            # 调用对应的sub command 进行处理
            self.sub_command.get(sub_command).process(from_group, from_qq, command_list)
