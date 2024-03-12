#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 主程序

import config.token_config  # 加载配置
import utils.token as glv

print(glv.get_token("token"))
