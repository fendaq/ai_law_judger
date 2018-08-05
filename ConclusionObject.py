# -*- coding: utf-8 -*-
"""
案件结论（请求类型，成立的路径，不成立的路径）
"""
class Conclusion(object):
    def __init__(self, appeal_id,result_bool,path_yes,path_no):
        """
        :param conclusion: conclusion can be a tuple (appeal_id, result_bool,path_yes,path_no)
        path_no is similiarly
        """
        self.appeal_id=appeal_id
        self.result_bool=result_bool
        self.path_yes=path_yes
        self.path_no=path_no

    def get_appeal_id(self):
        return self.appeal_id

    def get_result_bool(self):
        return self.result_bool

    def get_path_yes(self):
        return self.path_yes

    def get_path_no(self):
        return self.path_no

