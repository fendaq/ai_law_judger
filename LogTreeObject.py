# -*- coding: utf-8 -*-
"""
用于案由对应逻辑树的初始化：1、定义节点基本信息、2、节点逻辑属性树（节点ID、运算符、子节点父节点）
"""
PRIVATE_LENDING='PRIVATE_LENDING' #民间借贷纠纷

appeal_node_lending={   # 0：根
    5: {'id':5,'name':u'本金诉求','result_bool':False,'operation': 'and', 'child_nodes': [6, 30], 'father_node': None},#子节点：'借贷合意6','款项交付30'， #178：主合同诉求

    # 1：一级节点
    6: {'id':6,'name':u'借贷合意','result_bool':False,'operation': 'or', 'child_nodes': [7, 15, 19], 'father_node': 5},#子节点：'书面协议7'，'电子合同15'，'口头协议19'
    30: {'id':30,'name':u'款项交付','result_bool':False,'operation': 'or', 'child_nodes': [31, 43], 'father_node': 5},

    # 2：二级节点
    # '借贷合意6'的子节点：
    7: {'id':7,'name':u'书面协议','result_bool':False,'operation': 'and', 'child_nodes': [8, 9], 'father_node': 6}, #子节点：u'借的意思表示8',u'当事人签章9',u'本金14'
    15: {'id':15,'name':u'电子合同','result_bool':False,'operation': 'and', 'child_nodes': None, 'father_node': 6},
    19: {'id':19,'name':u'口头协议','result_bool':False,'operation': 'or', 'child_nodes': None, 'father_node': 6},
    # '款项交付30'的子节点
    31: {'id':31,'name':u'交付凭证','result_bool':False,'operation': 'and', 'child_nodes':None, 'father_node': 30}, #无子节点
    43: {'id':43,'name':u'现金（票据）交付','result_bool':False,'operation': 'or', 'child_nodes': [44,  -99,], 'father_node': 30},#子节点：u'出具现金（票据）的收条44',u'被告自认-99'

    # 3:三级节点
    #'书面协议'下的子节点：
    8: {'id':8,'name':u'借的意思表示','result_bool':False,'operation': None, 'child_nodes': None, 'father_node': 7},
    9: {'id':9,'name':u'当事人签章','result_bool':False,'operation': 'and', 'child_nodes': None, 'father_node': 7},
    # 现金（票据）交付下的子节点：
    44: {'id':44,'name':u'出具现金（票据）的收条','result_bool':False,'operation': 'and', 'child_nodes': None, 'father_node': 43},
    -99: {'id':-99,'name':u'被告自认','result_bool':False,'operation': None, 'child_nodes': None, 'father_node': 43},
}


cause_log_tree={PRIVATE_LENDING:appeal_node_lending}