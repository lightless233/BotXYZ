#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    _base.py
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    $END$

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017-2020 lightless. All rights reserved
"""

import abc
from typing import List

from cqplus._api import CQPlusApi
from cqplus._logging import CQPlusLogging

import constant
from utils import utils


class BaseCommand:
    def __init__(self, api: CQPlusApi, logger: CQPlusLogging):
        super(BaseCommand, self).__init__()

        self.command_name = "%default"

        self.api = api
        self.logger = logger

    def __check_admin(self, from_group, from_qq) -> bool:
        if from_qq not in constant.ADMIN_QQ:
            at_msg = utils.build_at_msg(from_qq)
            self.api.send_group_msg(from_group, at_msg + "\n您还不是管理员呢！")
            self.api.set_group_ban(from_group, from_qq, 60)
            return False
        else:
            return True

    @abc.abstractmethod
    def process(self, from_group: int, from_qq: int, command_list: List[str]):
        pass
