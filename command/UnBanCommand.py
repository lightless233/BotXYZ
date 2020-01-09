#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    UnBanCommand
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

from utils import utils
from ._base import BaseCommand


class UnBanCommand(BaseCommand):

    def __init__(self, api: CQPlusApi, logger: CQPlusLogging):
        super(UnBanCommand, self).__init__(api, logger)

        self.command_name = "%unban"

    def process(self, from_group: int, from_qq: int, command_list: List[str]):

        if not self._check_admin(from_group, from_qq):
            return

        try:
            target_qq = command_list[1]
        except IndexError:
            self.api.send_group_msg(
                from_group,
                utils.build_at_msg(from_qq) + "\nError arguments.\n%unban qq"
            )
            return

        at_qq = utils.get_qq_from_at_msg(target_qq)
        if at_qq is None:
            self.api.set_group_ban(group_id=from_group, user_id=int(target_qq), duration=0)
        else:
            self.api.set_group_ban(group_id=from_group, user_id=int(at_qq), duration=0)
        self.api.send_group_msg(from_group, utils.build_at_msg(from_qq) + "\nUnban operation success!")
