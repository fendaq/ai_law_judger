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

<img src="https://github.com/brightmart/ai_law_judger/blob/master/resources/small_tree.jpg"  width="60%" height="60%" />


2.Main Objects and  Relationship
------------------------------------------------------------------------------------------------------------------------

<img src="https://github.com/brightmart/ai_law_judger/blob/master/resources/logical_graph.jpg"  width="60%" height="60%" />


3.Type of Claims and Logical Operator
------------------------------------------------------------------------------------------------------------------------
There are many type of law cases, e.g. traffic accident, private lending, marriage and so on. for each type of law case,

people judgers can abstract some key claims use their knowledge and experience. below we will list some key claims for private lending

which account for one of highest percentage among all civil cases. for each claim, there will be a logical tree associated with.

the root of this logical tree is the claim.


Key claims of private lending:

 1) claim of principal: demand to pay back the principal
 
 2) claim of interest: demand to pay interest of principal
 
 3) claim for loss of contract breach: cause some loss by a party who violate a contract
 
 4) claim of mutual debt of husband and wife: may apply to a person in a marriage whose spouse involve in liability
 
 5) claim of guarantee liability: someone or organization take guarantee responsibility for lending.
 
 
 Logical operators are used to reasoning among sub nodes or parents nodes in knowledge graph.
 
 Two main type of Logical Operator:
 
 1) AND: true if meet all requirements 
 
 2) OR:  true if meet one requirement among all requirement
 
 
 

4.How we implement it
------------------------------------------------------------------------------------------------------------------------
TODO

5.Usage
------------------------------------------------------------------------------------------------------------------------

6.Envornment
------------------------------------------------------------------------------------------------------------------------
Todo

5.Case Study
------------------------------------------------------------------------------------------------------------------------
TODO

6.Todo list
------------------------------------------------------------------------------------------------------------------------
TODO
