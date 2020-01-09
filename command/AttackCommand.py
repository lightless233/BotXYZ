#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    AttackCommand
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    $END$

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017-2020 lightless. All rights reserved
"""
import math
import random
from typing import List

from cqplus._api import CQPlusApi
from cqplus._logging import CQPlusLogging

from utils import utils
from ._base import BaseCommand


class AttackCommand(BaseCommand):

    def __init__(self, api: CQPlusApi, logger: CQPlusLogging):
        super(AttackCommand, self).__init__(api, logger)

        self.command_name = "%attack"

    def ban(self, is_stake, from_group, from_qq, duration):
        if not is_stake:
            self.api.set_group_ban(from_group, from_qq, duration)

    def process(self, from_group: int, from_qq: int, command_list: List[str]):

        try:
            target_qq = command_list[1]
            duration = command_list[2]
        except IndexError:
            self.api.send_group_msg(
                from_group,
                utils.build_at_msg(from_qq) + "\nError arguments.\n%attack qq duration(min.)"
            )
            return

        at_qq = utils.get_qq_from_at_msg(target_qq)
        if at_qq is not None:
            real_target = at_qq
        else:
            real_target = target_qq

        try:
            real_target = int(real_target)
            duration = int(duration)
        except:
            self.logger.info("[XYZ] err argument.")
            self.api.send_group_msg(
                from_group,
                utils.build_at_msg(from_qq) + "\nError arguments.\n%attack qq duration(min.)"
            )
            return

        at_attacker_qq_msg = utils.build_at_msg(from_qq)
        at_target_qq_msg = utils.build_at_msg(real_target)
        is_stake = False

        # 校验参数
        if duration < 0:
            self.api.send_group_msg(from_group, at_attacker_qq_msg + "\n你再乱搞试试？")
            self.api.set_group_ban(from_group, from_qq, 60)
            return
        if duration == 0:
            self.api.send_group_msg(from_group, at_attacker_qq_msg + "\n彩蛋已经修复咯！")
            self.api.set_group_ban(from_group, from_qq, 60 * 60)
            return

        # 如果这个傻子要打自己
        if int(real_target) == from_qq:
            self.api.set_group_ban(from_group, from_qq, duration * 60)
            self.api.send_group_msg(from_group, at_attacker_qq_msg + "\n小老弟你是个傻子？")
            return

        # 如果打群主
        # 群主作为木桩人使用
        if int(real_target) == 2522031536:
            # self.api.set_group_ban(from_group, from_qq, duration * 60 * 2)
            # self.api.send_group_msg(from_group, at_attacker_qq_msg + "\n二营长，你他娘的意大利炮呢？给老子拉上来！开炮！开炮！开炮！")
            is_stake = True

        # 正常攻击，先开始roll点
        attacker_pt = random.randint(0, 100)
        target_pt = random.randint(0, 100)

        base_msg = at_attacker_qq_msg + f"的点数：{attacker_pt}\n"
        base_msg += at_target_qq_msg + f"的点数：{target_pt}\n"

        # 如果俩人点数相等，统统干掉，但是时间减半
        # 如果攻击者和目标都是100点，统统禁言，并且翻倍时间
        if attacker_pt == target_pt and attacker_pt != 100:
            base_msg += "旗鼓相当的对手，两败俱伤！"
            self.api.send_group_msg(from_group, base_msg)

            # self.api.set_group_ban(from_group, from_qq, duration * 60 / 2)
            # self.api.set_group_ban(from_group, real_target, duration * 60 / 2)
            self.ban(is_stake, from_group, from_qq, duration * 60 / 2)
            self.ban(is_stake, from_group, real_target, duration * 60 / 2)
            return
        if attacker_pt == target_pt and attacker_pt == 100:
            base_msg += "你俩怎么一起开大招？"
            self.api.send_group_msg(from_group, base_msg)
            # self.api.set_group_ban(from_group, from_qq, duration * 60 * 2)
            # self.api.set_group_ban(from_group, real_target, duration * 60 * 2)
            self.ban(is_stake, from_group, from_qq, duration * 60 * 2)
            self.ban(is_stake, from_group, real_target, duration * 60 * 2)
            return

        # 如果攻击者roll到100点，无视防御
        if attacker_pt == 100 and target_pt != 100:
            base_msg += at_attacker_qq_msg + "居然开大了！无视防御！双倍伤害！"
            self.api.send_group_msg(from_group, base_msg)
            # self.api.set_group_ban(from_group, real_target, duration * 60 * 2)
            self.ban(is_stake, from_group, real_target, duration * 60 * 2)
            return

        # 如果目标roll到了100点，无视攻击
        if target_pt == 100 and attacker_pt != 100:
            base_msg += at_attacker_qq_msg + "发动了：绝 对 防 御，并且反击成功！"
            self.api.send_group_msg(from_group, base_msg)
            # self.api.set_group_ban(from_group, from_qq, duration * 60 / 2)
            self.ban(is_stake, from_group, from_qq, duration * 60 / 2)
            return

        # todo: 处理一下roll到0点的情况
        if duration >= 20:
            final_attacker_pt = math.floor(attacker_pt - (duration / 0.8))
        else:
            final_attacker_pt = math.floor(attacker_pt - (duration / 1.5))

        base_msg = at_attacker_qq_msg + f"的点数：{attacker_pt}，叠加debuff后的点数：{final_attacker_pt}\n"
        base_msg += at_target_qq_msg + f"的点数：{target_pt}\n"
        can_counter = False
        if final_attacker_pt > target_pt:
            # 攻击成功
            base_msg += at_attacker_qq_msg + "的攻击得手了！"
            # self.api.set_group_ban(from_group, real_target, duration * 60)
            self.ban(is_stake, from_group, real_target, duration * 60)
            self.api.send_group_msg(from_group, base_msg)
        elif final_attacker_pt < target_pt:
            # 攻击失败
            base_msg += at_attacker_qq_msg + "手滑了，啥也没打到。"
            self.api.send_group_msg(from_group, base_msg)
            can_counter = True
        else:
            # 相等了
            base_msg += "旗鼓相当的对手，两败俱伤，伤害均摊。"
            self.api.send_group_msg(from_group, base_msg)
            # self.api.set_group_ban(from_group, real_target, duration / 2 * 60)
            # self.api.set_group_ban(from_group, from_qq, duration / 2 * 60)
            self.ban(is_stake, from_group, real_target, duration / 2 * 60)
            self.ban(is_stake, from_group, from_qq, duration / 2 * 60)

        # 开始反击判定
        if not can_counter:
            return
        # 临时patch，在大时长下增强见切概率
        if duration >= 10 and duration <= 20:
            counter_attack_pt = math.floor(random.randint(0, 100) * 1.2)
        elif duration >= 20:
            counter_attack_pt = math.floor(random.randint(0, 100) * 1.5)
        else:
            counter_attack_pt = math.floor(random.randint(0, 100) * 1.0)
        self.logger.info(f"[XYZ] counter_attack_pt: {counter_attack_pt}")
        if counter_attack_pt > final_attacker_pt:
            # 反击成功
            self.api.send_group_msg(from_group, at_target_qq_msg + f"见切成功！斩于马下！反击值：{counter_attack_pt}")
            # self.api.set_group_ban(from_group, from_qq, duration * 60 * 0.2)
            self.ban(is_stake, from_group, from_qq, duration * 60 * 0.55)
        else:
            # 反击失败
            self.api.send_group_msg(from_group, at_target_qq_msg + f"反击失败了，真可惜。反击值：{counter_attack_pt}")
