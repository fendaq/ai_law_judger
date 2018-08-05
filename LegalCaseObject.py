# -*- coding: utf-8 -*-
"""
案件对象：关联原告证据，诉讼请求，被告证据，抗辩请求（案件结论）
"""

class LegalCase(object):
    def __init__(self, cause_name, id, appeal_id, evidence_list_plaintiff): # plead_list, evidence_list_defendant
        """
        :param cause_name: 案由名称
        :param id: 案件ID
        :param appeal_list: 诉请
        :param evidence_list_plaintiff: 原告证据列表
        """
        self.cause_name=cause_name
        self.id=id
        self.appeal_id=appeal_id
        self.evidence_list_plaintiff=evidence_list_plaintiff

    # below omit setting and getting of fields