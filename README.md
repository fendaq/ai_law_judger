# ai_law_judger

judicial/trial engine with knowledge graph

1.Desc
------------------------------------------------------------------------------------------------------------------------

Judicial/trial engine is used to make a judgement during law/legal case. Instead of replacing judger,

it is working together with judger and make judger's job more efficient, less time consuming and easier.

Judicial/trail engine achieve this purpose by incorporating knowledge from team of experienced judgers who have many years of judicial practical experiences. 

These people judgers work together and transform the knowledge of how they make a judgement for a law case into a graph.
 
for simplification, we call this graph as judicial knowledge graph.

Once judicial knowledge graph is formed, our job is to transform it into a runnable module in AI system.

The key idea of judicial engine is start reasoning from claim, using judicial knowledge graph, associate evidences to nodes of knowledge graph, 

then we can make a conclusion that we support a claim or not. Another way of saying, if there are three claims in a law case

form who file a lawsuit(plaintiff). for each claim, we will ask plaintiff to provide evidences, then these evidences will be used to prove something

on the knowledge graph, then once meet all the requirement for a claim, we can support the claim.

<img src="https://github.com/brightmart/ai_law_judger/blob/master/resources/small_tree.jpg"  width="80%" height="80%" />


2.Main Objects and  Relationship
------------------------------------------------------------------------------------------------------------------------

For a [legal case], it has serveral [claim]s, interested parties should provide with [evidence]s to support their [claim]s (or called appeals),

AI judger will reasoning among [logical tree], which is a form of [knowledge graph], based on proof of evidences, and then reach a [conclusion].

Each type of case has its own logical tree. the main branches of logical tree are claims.
 
Legal case combine all object together(claim, evidence and logical tree).

<img src="https://github.com/brightmart/ai_law_judger/blob/master/resources/logical_graph.jpg"  width="60%" height="60%" />


3.Type of Claims and Logical Operators
------------------------------------------------------------------------------------------------------------------------
There are many type of law cases, e.g. traffic accident, private lending, marriage and so on. For each type of law case,

people judgers will abstract key claims use their knowledge and experience. 

Below we will list some key claims for private lending which account for one of highest percentage among all civil cases. 

For each claim, there will be a logical tree associated with. by default, the root of this logical tree is the claim.


### Key claims of private lending:

 1) claim of principal: demand to pay back the principal
 
 2) claim of interest: demand to pay interest of principal
 
 3) claim for loss of contract breach: cause some loss by a party who violate a contract
 
 4) claim of mutual debt of husband and wife: may apply to a person in a marriage whose spouse involve in liability
 
 5) claim of guarantee liability: someone or organization take guarantee responsibility for lending.
 
 
 ### Logical operators are used to reasoning among sub nodes or parents nodes in knowledge graph.
 
 Two main types of Logical Operator:
 
 1) AND: true if meet all requirements 
 
 2) OR:  true if meet one requirement among all requirement
 
 There are other type of operators except these main types, including NOT, XOR(exclusive OR), we will omit for now.
 

4.Usage
------------------------------------------------------------------------------------------------------------------------
command to run:

    python main.py
  
It will print some logs, including the claim, evidences supported this claim, conclusion. 

If the claim is support, the reason(path) to support it; if it is overturn, the reason why it is not support.
  
  
Envornment:

    Python 2.7 or  Python 3.x


5.How we implement it
------------------------------------------------------------------------------------------------------------------------
We use three steps to reasoning on the knowledge graph. basically, it is a form of bottom-up solution.

For your better understanding, we will describe main steps first, then in the following section #7 Case Study, we will give you two examples.

1) Step one, compute path starting from node (node_start)of knowledge graph where evidence point to, to a claim(or appeal, as node_end) which is a sub root

   node in knowledge graph. you can do this simply by getting parent node of node_start, then parent node of this parent node...util it reach root node.

2) Step two, for each path, try to set value of all nodes along the path, util you are not able to. 

   Essentially, if a node is proofed by a evidence, you can set it to True(Activate); and if its parent node's(node_p) operator is OR,

   which means node_p is true if one condition of sub nodes is met, you can set node_p's value to True(Activate).

   However if its node_p's operator is AND, you need check and see whether all sub nodes's value is True.


3) Step three, start from the claim, you can check the value of the sub nodes of this claim,

   and get a conclusion to support the claim or not.


6.Case Study 
------------------------------------------------------------------------------------------------------------------------
We will give two examples, one is claim is supported, another is overthrown.

### Case Study 1: a claim with evidences that AI judger support

the claim is [appeal of principal 1], and in this case, it has two evidences approval of following nodes:

[written agreement 4] and [receipt of cash(bill) 11], the question is should a AI judger support this claim or not?

<img src="https://github.com/brightmart/ai_law_judger/blob/master/resources/tree_case_1.jpg"  width="80%" height="80%" />


Solution:
  
  Step 1, that's compute path from evidence to claim. take frist evidence [written agreement 4], it parent node is [loan agreement 2],
      
      [loan agreement 2]'s parent node is [appeal of principal1]. 
      
      so the path is:
        
        [written agreement 4, loan agreement 2, appeal of principal 1], or [4, 2, 1]. 
        
      for evidence of [receipt of cash(bill)], you can also get its path: 
      
        [receipt of cash(bill) 11, cash(bill) delivery 8, delivery of money 3, appeal of principal 1], or [11, 8, 3, 1]. 
        
      these numbers are IDs represent nodes in knowledge graph,
  
  Step2, try to set value of nodes along the path.
     
     take the first path: [written agreement 4, loan agreement 2, appeal of principal 1], or [4, 2, 1].
     
     as there is an evidence point to [written agreement 4], we set this node 4 to be True.  how about the value of [loan agreement 2]?
     
     [loan agreement 2]'s operator is [or], means if will be True if one sub node is True. as we can see from knowledge graph that [written agreement 4]
     
     is its sub node, its value is True, so [loan agreement 2] will be True.
     
     for [appeal of principal 1], as its operator is [and], it need both of its sub node is True, but we only know [loan agreement 2] is True, so we will not 
     
     able to set its value. 
     
     so we know now:[written agreement 4:True, loan agreement 2:True, appeal of principal 1:False]. we will set value in a field named as [result] in each node. 
     
     for any node we can't set to True, its value will be False( as default value).

  Step 3, check sub nodes of the claim.
     

Logs:

Input： 

        Claim(or appeal): appeal of principal 1
        
        Evidence list:written agreement 4,receipt of cash(bill) 11
        
Output： 
        Conclusion:support(yes)
        
Path to support:

        written agreement4-->loan agreement2-->appeal of principal1
        
        receipt of cash(bill)11-->cash(bill) delivery8-->delivery of money3-->appeal of principal1
        

### Case Study 2: a claim with evidences that AI judger overthrow

7.Todo list
------------------------------------------------------------------------------------------------------------------------
TODO
