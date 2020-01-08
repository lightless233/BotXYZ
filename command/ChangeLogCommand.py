#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    ChangeLogCommand
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


changelog = \
"""
v1.0.1
- 削弱%attack时的见切机制
- 削弱%attack时的debuff效果
- 程序框架重构，方便多人开发

v1.0.0
- 基本框架完成
- 新增%ban、%unban、%attack命令
"""


class ChangelogCommand(BaseCommand):

    def __init__(self, api: CQPlusApi, logger: CQPlusLogging):
        super(ChangelogCommand, self).__init__(api, logger)

        self.command_name = "%changelog"

    def process(self, from_group: int, from_qq: int, command_list: List[str]):
        self.api.send_group_msg(from_group, changelog)
