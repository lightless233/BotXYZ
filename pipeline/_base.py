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


class BasePipeline:

    def __init__(self):
        super(BasePipeline, self).__init__()

        self.name = "default-pipeline"

    @abc.abstractmethod
    def process(self, msg, from_qq, from_group):
        pass
