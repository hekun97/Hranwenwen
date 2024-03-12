#!/usr/bin/env python3
# -*- coding:utf-8-*-
# 全局变量管理模块


def __init__():
    """在主模块初始化"""
    global GLOBALS_DICT
    GLOBALS_DICT = {}


def set_token(name, value):
    """设置token"""
    try:
        GLOBALS_DICT[name] = value
        return True
    except KeyError:
        return False


def get_token(name):
    """取值token"""
    try:
        return GLOBALS_DICT[name]
    except KeyError:
        return "Not Found"
