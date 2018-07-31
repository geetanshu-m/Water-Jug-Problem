from make_states import make_states
import graph_operation as go
from graphviz import Graph

graph = {}
states_count = 0
stack = list()

def add_node(i, x, y):
    '''
    Denoteing each node child
    params : current capacity in A, current capacity in B, previous related node
    '''
    global states_count
    global stack
    init_i = i
    parent_node = [x, y]
    node_list = set()

    node_list.add(ms.fillA(parent_node[0], parent_node[1]))
    node_list.add(ms.fillB(parent_node[0], parent_node[1]))
    node_list.add(ms.pourBtoA(parent_node[0], parent_node[1]))
    node_list.add(ms.pourAtoB(parent_node[0], parent_node[1]))
    node_list.add(ms.emptyA(parent_node[0], parent_node[1]))
    node_list.add(ms.emptyB(parent_node[0], parent_node[1]))
    if (0,0) in node_list:
        node_list.remove((0,0))
    if (parent_node[0], parent_node[1]) in node_list:
        node_list.remove((parent_node[0], parent_node[1]))
    node_list = list(node_list)

    final_node_list = list()
    for x in node_list:
        x = list(x)
        i = i + 1
        x.insert(0,i)
        final_node_list.append(x)
        stack.append(x)
    graph[str(list([init_i, parent_node[0], parent_node[1]]))] = final_node_list
    states_count = states_count + len(list(node_list))
    print("stack",stack)

if __name__ == "__main__":
    A = 4
    B = 3
    x = 0
    y = 0
    desired_x = 2
    desired_y = 0

    ms = make_states(A, B)

    add_node(int(0),x,y)
    k = 0
    while stack:
        x = list(stack[-1])
        print(x)
        if x[1] == 2 and x[2] == 0:
            continue
        else:
            add_node(int(x[0]), x[1], x[2])
        del stack[-1]
        k = k + 1
        if k == 100:
            break
    
    for x in graph:
        print(str(x) + " - " + str(graph[x]))
        for y in graph[x]:
            if y[1] == 2 and y[2] == 0:
                print("found")
    print("Total No of States = " + str(states_count))
