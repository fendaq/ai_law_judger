# -*- coding: utf-8 -*-
"""
案件证据：id,名称，【证明对象】，提交人
其中，证明对象指向了审判逻辑树下的某个节点
"""

class Evidence(object):
    def __init__(self, id,name,prove_object):
        self.id=id
        self.name=name
        self.prove_object=prove_object

    # below omit set and get of fields.

    def set_prove_object(self,prove_object):
        self.prove_object=prove_object

    def get_prove_object(self):
        return self.prove_object
