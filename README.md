[![Codacy Badge](https://api.codacy.com/project/badge/Grade/0ff9237cf49f4b9192f8e6ec312d9872)](https://www.codacy.com/manual/proman24/Water-Jug-Problem?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=proman24/Water-Jug-Problem&amp;utm_campaign=Badge_Grade)

[![Build Status](https://travis-ci.org/proman24/Water-Jug-Problem.svg?branch=master)](https://travis-ci.org/proman24/Water-Jug-Problem)

# Water-Jug-Problem

Solution to the water jug problem in my way.

### Problem Statement

There are two jugs of volume ```A``` litre and ```B``` litre. Now, we have to trace a proper path to get ```x``` litre of water in jug ```A```. We have unlimited supply of water.

![Tree generated in 5 iterations](/images/tree.PNG)

### Node Defination

[ ```id```, ```parent_id```, ```water in A```, ```water in B```]

### Methodology

So, I have divided the execution in two major steps:
#### Creation of graph
1. First of all initial node  ```[0,'null', 0, 0]``` is added to the graph.
2. Then, taking the state ```(0, 0)``` as the initial state, all the procedures of class ```make_states.py``` is called with the help of a local object and the return states are saved as the child node of the initial node.
3. Repeating second step by makeing all the child as initial node, a full graph is generated.
4. In this program I have limited generations to ```256 iterations``` which do generates ```~1481``` states.
#### Tracing the path for the graph
1. Graph is traversed index wise till the node watnted is reached.
2. Now, when the desired node is reached, this node is backtracked to the initial node or ```root node``` and the path followed while backtracking is printed.
3. For every instance of the desired node this path is printed.

```
( 2 , 0 )<-( 0 , 2 )<-( 4 , 2 )<-( 3 , 3 )<-( 3 , 0 )<-( 0 , 3 )<-( 0 , 0 )
( 2 , 3 )<-( 2 , 0 )<-( 0 , 2 )<-( 4 , 2 )<-( 3 , 3 )<-( 3 , 0 )<-( 0 , 3 )<-( 0 , 0 )
( 2 , 0 )<-( 0 , 2 )<-( 4 , 2 )<-( 3 , 3 )<-( 3 , 0 )<-( 3 , 3 )<-( 3 , 0 )<-( 0 , 3 )<-( 0 , 0 )
( 2 , 0 )<-( 0 , 2 )<-( 4 , 2 )<-( 3 , 3 )<-( 4 , 2 )<-( 3 , 3 )<-( 3 , 0 )<-( 0 , 3 )<-( 0 , 0 )
( 2 , 0 )<-( 2 , 3 )<-( 2 , 0 )<-( 0 , 2 )<-( 4 , 2 )<-( 3 , 3 )<-( 3 , 0 )<-( 0 , 3 )<-( 0 , 0 )
( 2 , 0 )<-( 0 , 2 )<-( 4 , 2 )<-( 0 , 2 )<-( 4 , 2 )<-( 3 , 3 )<-( 3 , 0 )<-( 0 , 3 )<-( 0 , 0 )
( 2 , 0 )<-( 0 , 2 )<-( 4 , 2 )<-( 3 , 3 )<-( 3 , 0 )<-( 0 , 3 )<-( 4 , 3 )<-( 0 , 3 )<-( 0 , 0 )
( 2 , 0 )<-( 0 , 2 )<-( 4 , 2 )<-( 3 , 3 )<-( 3 , 0 )<-( 0 , 3 )<-( 1 , 3 )<-( 4 , 0 )<-( 0 , 0 )
( 2 , 0 )<-( 0 , 2 )<-( 4 , 2 )<-( 3 , 3 )<-( 3 , 0 )<-( 0 , 3 )<-( 4 , 3 )<-( 4 , 0 )<-( 0 , 0 )
( 2 , 3 )<-( 2 , 0 )<-( 0 , 2 )<-( 4 , 2 )<-( 3 , 3 )<-( 3 , 0 )<-( 3 , 3 )<-( 3 , 0 )<-( 0 , 3 )<-( 0 , 0 )
( 2 , 3 )<-( 2 , 0 )<-( 0 , 2 )<-( 4 , 2 )<-( 3 , 3 )<-( 4 , 2 )<-( 3 , 3 )<-( 3 , 0 )<-( 0 , 3 )<-( 0 , 0 )
Total No of States =  1481  And A=2 are  11
```

### How to run this file

run ```python water_jugg_main_bfs.py```

### Requirements

- graphviz (For graph image generation)
