#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    AttackCommand
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    $END$

    :author:    wINfOG <xrhwxy2009@aliyun.com>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017-2020 lightless. All rights reserved
"""
import datetime
import re
from typing import List, Dict, Tuple
from urllib.request import Request, urlopen

from cqplus._api import CQPlusApi
from cqplus._logging import CQPlusLogging

from ._base import BaseCommand

# {年月日: (更新的小时计数，[数据列表])}
g_news_cache: Dict[str, Tuple[int, List[str]]] = {}


class SecTodayCommand(BaseCommand):

    def __init__(self, api: CQPlusApi, logger: CQPlusLogging):
        super(SecTodayCommand, self).__init__(api, logger)
        self.command_name = "%sectoday"

    # 从cache中获取今天的新闻，每4小时更新一次
    def get_today_news(self) -> List[str]:

        date = str(datetime.date.today())
        hours = datetime.datetime.now().hour
        today_new = g_news_cache.get(date)

        if today_new is None or (hours // 4) != today_new[0]:
            refresh_new = self.get_today_news_from_sectoday()
            g_news_cache[date] = (hours // 4, refresh_new)
            return refresh_new
        else:
            return today_new[1]

    def get_today_news_from_sectoday(self) -> List[str]:
        ret_list = []
        sec_today_url = "https://sec.today/pulses/"
        url_request = Request(sec_today_url, headers={"User-Agent": "Mozilla/5.0"})
        webpage = urlopen(url_request).read()

        find = re.finditer(r'<div class="card-body">([\s\S]*?)</div>'.encode('utf-8'), webpage)

        for each in find:
            date = re.search(r"<small>([\s\S]*?)</small>".encode("utf-8"), each.group())
            if "hours" not in date.group().decode("utf-8") and "小时" not in date.group().decode("utf-8"):
                break
            title = re.search(r"<q>([\s\S]*?)</q>".encode("utf-8"), each.group())
            link = re.search(r'href="(.*)"'.encode("utf-8"), each.group())
            ret_list.append(title.group().decode("utf-8")[3:-4] + " http://sec.today"+link.group().decode("utf-8")[6:-1])

        self.logger.info(f"{ret_list}")
        return ret_list

    def process(self, from_group: int, from_qq: int, command_list: List[str]):
        self.api.send_group_msg(group_id=from_group, msg="\n".join(self.get_today_news()))
