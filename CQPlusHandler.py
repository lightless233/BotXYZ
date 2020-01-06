#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    CQPlusHandler
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    $END$

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017-2020 lightless. All rights reserved
"""
import sqlite3
from typing import List

import cqplus._api

import constant
import pipeline
from CommandHandler import CommandHandler
from pipeline._base import BasePipeline


class MainHandler(cqplus.CQPlusHandler):

    def __init__(self):
        super(MainHandler, self).__init__()
        self.TAG = "[XYZ]"
        self.commandHandler = CommandHandler(self.api, self.logging)

        self.pipelines: List[BasePipeline] = [
            pipeline.ThumbBanPipeline(self.api, self.logging),
            pipeline.RepeatBanPipeline(self.api, self.logging),
        ]

        # db 连接
        self.db = sqlite3.connect(constant.DEV_DB_NAME)

    def info(self, msg):
        self.logging.info(self.TAG + " " + msg)

    def handle_event(self, event, params):
        self.logging.info(f"{self.TAG} receive event: {event}, params: {params}")

        if event == "on_group_msg":
            self.on_group_msg(params)
        elif event == "on_enable":
            self.on_enable(params)
        else:
            self.logging.info(f"{self.TAG} No handler for this event, {event}")

    def on_enable(self, params):
        self.info(self.api.get_app_directory() + ", bot start!")
        # value = self.api.send_private_msg(387210935, "bot start!")

    def on_group_msg(self, params):
        """
        sub_type	int32
        msg_id	int32
        from_group	int64
        from_qq	int64
        msg	str
        font	int32
        is_anonymous	bool
        anonymous	dict
        """
        self.logging.info(f"{self.TAG} On receive group message")

        # 获取必要信息
        from_group = params.get("from_group")
        msg: str = params.get("msg")
        clean_msg = msg.replace(" ", "")
        from_qq = params.get("from_qq")

        # 非目标Q群来的消息 直接返回
        if (str(from_group) not in constant.TARGET_GROUP):
            return

        self.info("receive message: " + msg + ", from: " + str(from_qq))

        # pipeline start #
        # 如果是 % 开头的消息，认为是命令消息，否则就是普通的消息，走正常的pipeline进行处理
        if msg.startswith("%"):
            self.commandHandler.handler(msg, from_group, from_qq)
        else:
            pass

        for pipeline in self.pipelines:
            pipeline.process(msg, from_qq, from_group)
