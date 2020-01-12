#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    regain_service
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    $END$

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017-2020 lightless. All rights reserved
"""

import time
from datetime import datetime

from models import db
from models.regain import RegainModel


class RegainService:

    def __init__(self):
        super(RegainService, self).__init__()

        self.hp_time = 10 * 60
        self.sp_time = 5 * 60

    def update_next_hp_time(self, qq):
        with db:
            next_ts = time.time() + self.hp_time
            next_dt = datetime.fromtimestamp(next_ts)
            query = RegainModel.update(hp_next_time=next_dt).where(RegainModel.qq == qq)

            return query.execute()

    def update_next_sp_time(self, qq):
        with db:
            next_ts = time.time() + self.sp_time
            next_dt = datetime.fromtimestamp(next_ts)
            query = RegainModel.update(sp_next_time=next_dt).where(RegainModel.qq == qq)

            return query.execute()
