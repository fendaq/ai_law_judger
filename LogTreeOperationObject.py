# -*- coding: utf-8 -*-
"""
根据诉请，结合证据（和或法官的反馈），利用逻辑树（的逻辑操作符），得到判决结论。
"""
from LogTreeObject import cause_log_tree
from EvidenceObject import Evidence
from ConclusionObject import Conclusion
class LogTreeOperation(object):
    def __init__(self,legal_case):
        """
        :param legal_case: 案件类：案由名，诉请，证据
        :return:
        """
        self.legal_case=legal_case
        cause_name=self.legal_case.cause_name # 案由名
        self.log_tree=cause_log_tree[cause_name] #某一个案由下的逻辑树
        self.no_path=[]
        self.yes_path=[]
        self.conclusion=None # result, yes_path, no_path

    def get_conclusion(self):
        return self.conclusion

    def logic_operation(self):
        """
        # 根据诉请，利用逻辑关系，得到诉请支持与否
        # 1.得到相关参数;
        # 2.从证据出发，获得证据对应的节点到诉请节点的整个路径;
        # 3.对每一个路径，分别设置每一个可以设置的节点值，直到不能计算的节点;
        # 4.从诉请根节点出发，结合树的状态，得到最终的结论;
        # 5.输出成立（或不成立的）路径;
        :return:
        """
        # 1. 得到相关参数（案由名、诉请ID、证据列表、特定案由下的逻辑树）
        appeal_id=self.legal_case.appeal_id # 诉请ID
        print(u"诉讼请求: %s" %self.log_tree[appeal_id]['name']+str(appeal_id))
        evidence_list=self.legal_case.evidence_list_plaintiff #证据列表
        evidence_id_list=[]
        for evidence in evidence_list:
            evidence_id=evidence.get_prove_object()
            evidence_id_list.append(evidence_id)
        evidence_id_list_print=[self.log_tree[id]['name']+str(id) for id in evidence_id_list]
        print(u"证据列表:"+",".join(evidence_id_list_print)) #log_tree_operation.log_tree[id]['name']

        # 2. 从证据出发，获得证据对应的节点到诉请节点的整个路径（有几个证据，就有几个路径）
        path_node_list_list=[]
        for i,node_evidence_id in enumerate(evidence_id_list):
            path_node_list_temp=self.get_path_from_evidence_to_appeal(node_evidence_id, appeal_id)
            print("path_node_list_temp:",path_node_list_temp)
            path_node_list_list.append(path_node_list_temp)
        print("path_node_list_list:",path_node_list_list)

        # 3. 对每一个路径，分别设置每一个可以设置的节点值，直到不能计算的节点
        for sub_path_list in path_node_list_list:
            length_path=len(sub_path_list)
            for i in range(length_path-1):
                temp_flag=self.set_parent_node_value_using_logic_operation(sub_path_list[i],sub_path_list[i+1])
                if temp_flag==False:break # 如果flag为false,那么当前缺少父节点条件为真的条件。if flag is false then lack condition that parent node is true
        #print("log_tree:",self.log_tree)

        # 4. 从诉请根节点出发，结合树的状态，得到最终的结论
        operator=self.log_tree[appeal_id]['operation']  # 得到诉请下的操作符
        appeal_subnode_id_list=self.log_tree[appeal_id]['child_nodes']  # 得到诉请下的子节点列表以及他们的值
        result_flag=True if operator=='and' else False # 如果运算符是'and',
        for sub_node_id in appeal_subnode_id_list:
            sub_flag = self.log_tree[sub_node_id]['result_bool']
            if operator=='and':
                if sub_flag==False:
                    result_flag=False
                    break # 当运算符为AND时，一个不成立，运算就结束了
            else: # operator=='or'
                if sub_flag==True: # 当运算符为OR时，一个成立，结果就成了。结束运算
                    result_flag=True
                    break

        # 5. 输出成立（或不成立的）路径: 非核心方法（optional）
        yes_path, no_path=self.get_yes_path_no_path(result_flag,path_node_list_list)

        conclusion=Conclusion(appeal_id,result_flag,yes_path,no_path)
        self.conclusion=conclusion

    def set_parent_node_value_using_logic_operation(self,sub_node_id,parent_node_id):
        """
        设置从node_id_1到node_id_2，在node_id_2的值
        :param sub_node_id: 某一子节点ID
        :param parent_node: 某一子节点下的父节点ID
        :return:
        """
        # 1.设置子节点的值
        self.log_tree[sub_node_id]['result_bool'] = True
        # 2. 得到父节点的逻辑运算符 get operator of parent node
        operator=self.log_tree[parent_node_id]['operation']
        # 3.  设置父节点的值 set value of parent node
        flag=False
        if operator=='or':
            flag=True
        else: # operator='and' ==> 从父节点得到子节点的列表，查看子节点是否都为真，如果都为真，则设父节点为真。get parent_node's sub list, check whether it is all true. if all true, set to true
            sub_node_id_list=self.log_tree[parent_node_id]['child_nodes']
            flag=True
            for sub_node_id in sub_node_id_list:
                sub_node_value=self.log_tree[sub_node_id]['result_bool']
                if sub_node_value==False:flag=False;break;
        self.log_tree[parent_node_id]['result_bool']=flag
        return flag

    def get_path_from_evidence_to_appeal(self,node_id_1,node_id_2):
        """
        从证据指向的证明对象的节点,到诉请节点的路径
        :param log_tree: a tree
        :param node_id_1: id of starting node(evidence node)
        :param node_id_2: id of ending node(appeal node)
        :return: a list represent path. e.g.[-99,43,30,5]
        """
        #print("node_id_1:",node_id_1,";node_id_2:",node_id_2)
        result_list=[]
        start_node=self.log_tree[node_id_1]
        result_list.append(start_node['id'])
        #print("result_list:",result_list)
        flag=True
        while(flag):
            next_father_node_id=start_node['father_node'] # father node id
            if next_father_node_id is not None:
                result_list.append(next_father_node_id)
                start_node=self.log_tree[next_father_node_id]
            else:
                break
        return result_list

    def get_yes_path_no_path(self,result_flag,path_node_list_list):
        """
        得到成立的路径和或不成立的路径 get yes_path & no_path【这个是非核心方法】
        :param result_flag: result(boolean)
        :param path_node_list_list: list of list. 从证据到诉请的路径（有多少个证据，就有多少个路径）
        :return: yes_path, no_path
        """
        if result_flag==True: # 如果成立，将所有路径一并输出
            return path_node_list_list,[]
        # 如果不成立，只需要找出不成立的路径或理由
        for sub_path_list in path_node_list_list: # 遍历没一个路径
            length_path = len(sub_path_list)
            for i in range(length_path - 1): # 对于每一个路径，看看路径上的节点
                # 获取父节点ID、父节点逻辑运算符、父节点的子节点列表、父节点的结果
                temp_parent_node_id= sub_path_list[i + 1]
                operator=self.log_tree[temp_parent_node_id]['operation']
                subnode_list=self.log_tree[temp_parent_node_id]['child_nodes'] # get sublist of this parent node
                value=self.log_tree[temp_parent_node_id]['result_bool']
                if operator=='and':
                    if value==False: # if operator=='and' and parent node is not true ===> 只需获取任一不为真的节点就可以了 get a sub node that is not true
                        for sub_node_id in subnode_list:
                            sub_node_value=self.log_tree[sub_node_id]['result_bool']
                            if sub_node_value==False:
                                return [],[sub_node_id,temp_parent_node_id]
                else: # operator=='or':
                   pass