# -*- coding: utf-8 -*-
"""
诉讼请求（诉请类型：'本金诉求'/'利息诉求'/'夫妻共同债务诉求'/'违约损失诉求'/'担保责任诉求'）
"""

class Claim(object):

    def __init__(self, type): #构造方法
        """
        :param type: 诉请类型：'本金诉求'/'利息诉求'/'夫妻共同债务诉求'/'违约损失诉求'/'担保责任诉求'
        """
        self.appeal_type=type

    def set_appeal_type(self,type):
        self.appeal_type=type

    def get_appeal_type(self):
        return self.appeal_type
