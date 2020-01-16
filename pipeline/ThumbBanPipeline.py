#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    ThumbBanPipeline.py
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
from ._base import BasePipeline


class ThumbBanPipeline(BasePipeline):

    def __init__(self, api, logger):
        super(ThumbBanPipeline, self).__init__(api, logger)
        self.name = "ThumbBan-pipeline"

        # self.api: CQPlusApi = api
        # self.logger: CQPlusLogging = logger

        self.THUMBS_ID = [
            "[CQ:emoji,id=128077]",
            "[CQ:face,id=76]",
            "4",
            "[强]"
        ]

    def process(self, msg: str, from_qq: int, from_group: int) -> bool:
        clean_msg = msg.replace(" ", "")
        thumb_count = 0
        for thumb in self.THUMBS_ID:
            if thumb in clean_msg:
                thumb_count += clean_msg.count(thumb)
        if thumb_count > 0:
            self.api.set_group_ban(group_id=from_group, user_id=from_qq, duration=120 * thumb_count)
            self.api.send_group_msg(group_id=from_group, msg="发现大拇指！QNMD！\n" + utils.build_at_msg(from_qq))
            return False
        return True
