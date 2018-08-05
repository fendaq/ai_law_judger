# -*- coding: utf-8 -*-
"""
程序入口：得到需要的输入，构造相应的对象，调用逻辑树操作类，实现智能审判，并输出结论
超级版本：只考虑最小原型（10多个节点的知识图谱，一个诉讼请求，两个证据）；不考虑法官勾选代理的反馈、抗辩、设置默认值或交互功能等
        不考虑：
"""
from EvidenceObject import Evidence
from ClaimObject import Claim
from LegalCaseObject import LegalCase
from LogTreeOperationObject import LogTreeOperation

PRINCIPAL_DEMAND=5       # 本金诉求

WRITTEN_AGREEMENT=9     # 7:书面协议
DEFENDANT_CONFESSED=-99  # 被告自认
#

#WRITTEN_AGREEMENT=8     # 8：借的意思表示
#DEFENDANT_CONFESSED=-99  # 被告自认

#WRITTEN_AGREEMENT=44     # 44：出具现金的收条
#DEFENDANT_CONFESSED=-99  # 被告自认

#WRITTEN_AGREEMENT=7     #
#DEFENDANT_CONFESSED=15  #

#WRITTEN_AGREEMENT=15     #
#DEFENDANT_CONFESSED=31  #

#WRITTEN_AGREEMENT=9     # 9：当事人签章

# DEFENDANT_CONFESSED=8   # 8：借的意思表示

#WRITTEN_AGREEMENT=7     #

def main():
    print("输入：-----------------------------------")
    #1. 获得诉请列表：get appeal list
    appeal_principal=Claim(PRINCIPAL_DEMAND)
    #2. 获得证据列表：get evidence list
    evidence_list=[]
    evidence_1=Evidence( 0001, u'书面协议', WRITTEN_AGREEMENT)
    evidence_list.append(evidence_1)

    evidence_2=Evidence( 0002, u'被告自认', DEFENDANT_CONFESSED);evidence_list.append(evidence_2)

    #3. 案由名
    cause_name='PRIVATE_LENDING'

    #4. 案件
    legal_case=LegalCase(cause_name, '001',appeal_principal.get_appeal_type(), evidence_list)

    #5. 根据诉请，结合证据，调用逻辑树的运算功能，得到对诉请支持与否的结论
    log_tree_operation=LogTreeOperation(legal_case)
    # 逻辑运算
    log_tree_operation.logic_operation()
    # 得到结论
    conclusion=log_tree_operation.get_conclusion()
    result_bool=conclusion.get_result_bool()
    result_string=( u"成立" if result_bool==True else u"不成立")
    print("输出：-----------------------------------")
    print(u"判决结论:%s" %result_string)
    yes_path=conclusion.get_path_yes()
    no_path=conclusion.get_path_no()
    if result_bool==True:
        print("成立的路径:")
        for sub_list in yes_path:
            sub_list_print=[log_tree_operation.log_tree[id]['name']+str(id) for id in sub_list]
            print("-->".join(sub_list_print))
    else:
        sub_list_print=[log_tree_operation.log_tree[id]['name']+str(id) for id in no_path]
        print("")
        print("不成立的路径:" )
        print("-->".join(sub_list_print))

main()
#print("conclusion:", conclusion)
