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

For a [legal case], it has serveral [claim]s, interested parties should provide with [evidence]s to support their appeals,

AI judger will reasoning among [logical tree], which is a form of [knowledge graph] based on proof of evidences, and then reach a [conclusion].


<img src="https://github.com/brightmart/ai_law_judger/blob/master/resources/logical_graph.jpg"  width="60%" height="60%" />


3.Type of Claims and Logical Operators
------------------------------------------------------------------------------------------------------------------------
There are many type of law cases, e.g. traffic accident, private lending, marriage and so on. For each type of law case,

people judgers will abstract key claims use their knowledge and experience. 

Below we will list some key claims for private lending which account for one of highest percentage among all civil cases. 

For each claim, there will be a logical tree associated with. by default, the root of this logical tree is the claim.


####Key claims of private lending:

 1) claim of principal: demand to pay back the principal
 
 2) claim of interest: demand to pay interest of principal
 
 3) claim for loss of contract breach: cause some loss by a party who violate a contract
 
 4) claim of mutual debt of husband and wife: may apply to a person in a marriage whose spouse involve in liability
 
 5) claim of guarantee liability: someone or organization take guarantee responsibility for lending.
 
 
 ####Logical operators are used to reasoning among sub nodes or parents nodes in knowledge graph.
 
 Two main types of Logical Operator:
 
 1) AND: true if meet all requirements 
 
 2) OR:  true if meet one requirement among all requirement
 
 There are other type of operators except these main types, including NOT, XOR(exclusive OR), we will omit for now.
 

4.Usage
------------------------------------------------------------------------------------------------------------------------

5.Envornment
------------------------------------------------------------------------------------------------------------------------
Todo

6.How we implement it
------------------------------------------------------------------------------------------------------------------------
We use three steps to reasoning among knowledge graph. basically, it is from bottom-up solution.

For your better understanding, we will describe it first, then in the following section #7 Case Study, we will give you two examples.

1) Step one, compute path starting from node in knowledge graph where evidence point to, to a claim which is a sub root

node in knowledge graph.


2) Step two, for each path, try to set value of all nodes along the path, util you are not able to. 

Essentially, if a node is proofed by a evidence, you can set it to True(Activate); and if its parent node's(node_p) operator is OR,

which means node_p is true if one condition of sub nodes of this parent node is met, you can set node_p's value to True(Activate).

However if its node_p's operator is AND, you need check to see whether all sub nodes's value is True.


3) Step three, start from the claim, which is a sub root, you can check the value of the sub nodes of this claim,

and get a conclusion that we should support the claim or not.


7.Case Study
------------------------------------------------------------------------------------------------------------------------
TODO

8.Todo list
------------------------------------------------------------------------------------------------------------------------
TODO
