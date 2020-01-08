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
import re
import sqlite3
from typing import List, Dict, Optional

import cqplus._api

import constant
import pipeline
from command import BaseCommand, BanCommand, UnBanCommand, AttackCommand, ChangelogCommand
from command import HelpCommand
from pipeline import BasePipeline
from utils import utils


class MainHandler(cqplus.CQPlusHandler):

    def __init__(self):
        super(MainHandler, self).__init__()
        self.TAG = "[XYZ]"

        self.pipelines: List[BasePipeline] = [
            pipeline.ThumbBanPipeline(self.api, self.logging),
            pipeline.RepeatBanPipeline(self.api, self.logging),
        ]

        self.commands: Dict[str, BaseCommand] = {
            "%help": HelpCommand(self.api, self.logging),
            "%ban": BanCommand(self.api, self.logging),
            "%unban": UnBanCommand(self.api, self.logging),
            "%attack": AttackCommand(self.api, self.logging),
            "%changelog": ChangelogCommand(self.api, self.logging),
        }

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
        self.info(f"params: {params}")

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
        from_qq = params.get("from_qq")

        # 非目标Q群来的消息 直接返回
        if str(from_group) not in constant.TARGET_GROUP:
            return

        self.info("receive message: " + msg + ", from: " + str(from_qq))

        # pipeline start #
        # 如果是 % 开头的消息，认为是命令消息，否则就是普通的消息，走正常的pipeline进行处理
        if msg.startswith("%"):
            command_list = re.split(r"\s+", msg)
            input_command_name = command_list[0]
            command_instance: Optional[BaseCommand] = self.commands.get(input_command_name, None)
            if command_instance is None:
                self.commands.get("%help").process(from_group, from_qq, command_list=command_list)
            else:
                try:
                    command_instance.process(from_group, from_qq, command_list)
                except:
                    self.api.send_group_msg(from_group, utils.build_at_msg(from_qq) + "\nUnknown Error!")

        else:
            for p in self.pipelines:
                p.process(msg, from_qq, from_group)
