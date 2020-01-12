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

from cqplus._api import CQPlusApi
from cqplus._logging import CQPlusLogging


class BaseTimer:

    def __init__(self, api: CQPlusApi, logger: CQPlusLogging):
        super(BaseTimer, self).__init__()

        self.api: CQPlusApi = api

        self.logger: CQPlusLogging = logger

    @abc.abstractmethod
    def process(self):
        pass
