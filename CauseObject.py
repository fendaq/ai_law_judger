# -*- coding: utf-8 -*-
"""
案由：根据名称，得到特定案由下的逻辑树
"""
from LogTreeObject import cause_log_tree
class Cause(object):
    def __init__(self, name):  # 构造方法
        """
        :param name: 案由名字
        """
        self.name=name
        self.appeal_log_tree=cause_log_tree[name]

    def set_cause_name(self,name):
        self.cause_name=name


    def get_cause_name(self):
        return self.cause_name

    def set_appeal_log_tree(self,appeal_log_tree):
        self.appeal_log_tree=appeal_log_tree

    def get_appeal_log_tree(self):
        return self.appeal_log_tree

