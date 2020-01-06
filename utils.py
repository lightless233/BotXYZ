#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    utils
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    $END$

    :author:    lightless <root@lightless.me>
    :homepage:  None
    :license:   GPL-3.0, see LICENSE for more details.
    :copyright: Copyright (c) 2017-2020 lightless. All rights reserved
"""
import re
from typing import Union, Optional


class utils:

    @staticmethod
    def build_at_msg(at_qq: Union[int, str]) -> Optional[str]:
        if isinstance(at_qq, int):
            at_qq = str(at_qq)
        else:
            return None

        return "[CQ:at,qq=" + at_qq + "]"

    @staticmethod
    def get_qq_from_at_msg(msg: str) -> Optional[str]:
        if msg is None:
            return None
        else:
            matcher = re.search(r"\[CQ\s*:\s*at\s*,\s*qq=\s*(?P<qq>\d+)\s*\]", msg, flags=re.IGNORECASE)
            if matcher is not None:
                return matcher.group('qq')
            else:
                return None
