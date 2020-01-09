#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    RepeatBanPipeline
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    $END$

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017-2020 lightless. All rights reserved
"""

import random

from utils import utils
from ._base import BasePipeline

last_message = ""
repeat_count = 1


class RepeatBanPipeline(BasePipeline):

    def __init__(self, api, logger):
        super(RepeatBanPipeline, self).__init__(api, logger)

        # self.api: CQPlusApi = api
        # self.logger: CQPlusLogging = logger
        self.name = "repeat-ban-pipeline"

        # self.last_message = ""
        # self.repeat_count = 1

    def process(self, msg: str, from_qq: int, from_group: int) -> bool:

        global last_message, repeat_count

        if msg == last_message:
            # 是复读的消息，累加计数
            repeat_count += 1
        else:
            # 不是复读的消息，更新计数
            last_message = msg
            repeat_count = 1

        self.logger.info(f"last_message: {last_message} -> {repeat_count}")

        # 根据复读次数，进行概率ban
        # 1次、2次 不禁言
        # 10次以上 100%禁言
        if repeat_count in (1, 2):
            return True

        if repeat_count >= 10:
            self.api.set_group_ban(from_group, from_qq, 10)

            m = utils.build_at_msg(from_qq) + "\n您怕不是个复读机吧？\n劝你次根香蕉冷静冷静"
            self.api.send_group_msg(from_group, m)
            return False

        # r = 1- (n-1)/n
        # n = 3 => r = 1/3
        # n = 4 => r = 1/4
        # n = 5 => r = 1/5
        # n = 6 => r = 1/6
        # ...
        # n = 9 => r = 1/9
        # 1 / (12 - n)
        prob = 1.0 / (11 - repeat_count)
        point = random.random()
        self.logger.info(f"prob: {prob}, point: {point}")
        if point < prob:
            m = utils.build_at_msg(from_qq) + "\n老哥被我抓住了吧？"
            self.api.send_group_msg(from_group, m)
            self.api.set_group_ban(from_group, from_qq, repeat_count * repeat_count / 2 * 60)
            return False

        return True
