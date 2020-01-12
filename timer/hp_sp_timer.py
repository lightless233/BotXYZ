#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    hp_sp_timer
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    $END$

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017-2020 lightless. All rights reserved
"""
import datetime
import time

from peewee import DoesNotExist

from models import db
from models.player import PlayerInfoModel
from models.regain import RegainModel
from models.service import PlayerInfoService
from models.service.regain_service import RegainService
from ._base import BaseTimer


class HPSPTimer(BaseTimer):
    def __init__(self, api, logger):
        super(HPSPTimer, self).__init__(api, logger)

        self.name = "hp_sp_timer"

        self.player_service = PlayerInfoService()
        self.regain_service = RegainService()

    def process(self):
        self.logger.info(f"{self.name} execute!")

        with db:
            # 1. 取出所有hp和sp不满的玩家
            players: dict = PlayerInfoModel.select().where(
                (PlayerInfoModel.sp_max != PlayerInfoModel.sp_current) |
                (PlayerInfoModel.hp_max != PlayerInfoModel.hp_current)
            ).dicts()

            if len(players) == 0:
                return

            self.logger.info(f"[{self.name}] 有{len(players)}个记录需要更新")

            # 2. 检查这些玩家下次的恢复时间，如果当前时间大于下次恢复时间
            # 如果regain表中没有对应的玩家信息，那么就添加进去
            for player in players:
                qq = player.get("qq")
                try:
                    pc_regain = RegainModel.get(RegainModel.qq == qq)
                except DoesNotExist:
                    pc_regain = RegainModel.create(qq=qq)

                # 获取当前的时间戳
                current_ts = int(time.time())

                self.logger.info(
                    f"[{self.name}] next_hp_ts: {pc_regain.hp_next_time}, next_sp_ts: {pc_regain.sp_next_time}")

                if isinstance(pc_regain.hp_next_time, str):
                    next_hp_ts = time.mktime(
                        datetime.datetime.strptime(pc_regain.hp_next_time, "%Y-%m-%d %H:%M:%S").timetuple())
                    next_sp_ts = time.mktime(
                        datetime.datetime.strptime(pc_regain.sp_next_time, "%Y-%m-%d %H:%M:%S").timetuple())
                else:
                    next_hp_ts = time.mktime(pc_regain.hp_next_time.timetuple())
                    next_sp_ts = time.mktime(pc_regain.sp_next_time.timetuple())

                # 更新hp
                hp_max = player.get("hp_max")
                hp_current = player.get("hp_current")
                if current_ts >= next_hp_ts and hp_max > hp_current:
                    if hp_current + 10 <= hp_max:
                        self.player_service.update_player_hp(qq, 10)
                    else:
                        self.player_service.update_player_hp(qq, hp_max - hp_current)
                    # 重置下次更新时间
                    self.regain_service.update_next_hp_time(qq)

                # 更新sp
                sp_max = player.get("sp_max")
                sp_current = player.get("sp_current")
                if current_ts >= next_sp_ts and sp_max > sp_current:
                    if sp_current + 1 <= sp_max:
                        self.player_service.update_player_sp(qq, 1)
                    else:
                        self.player_service.update_player_sp(qq, sp_max - sp_current)
                    # 重置下次更新时间
                    self.regain_service.update_next_sp_time(qq)
