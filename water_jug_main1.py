'''
@TODO Mapping of nodes(0,0) and keys(0) to prevent overridding
'''
from make_states import make_states
import graph_operation as go
from graphviz import Graph

graph = {}
states_count = 0
i = 0
curr_node = 0

def add_node(x, y):
    '''
    Denoteing each node child
    params : current capacity in A, current capacity in B, previous related node
    '''
    global states_count,i,curr_node
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

    parent_node = [i,x, y]
    final_node_list = list()
    for x in node_list:
        x = list(x)
        i = i + 1
        x.insert(0,i)
        final_node_list.append(x)

    print(parent_node)
    print(final_node_list)

    graph[str(list(parent_node))] = list(final_node_list)
    print(graph)
    # print("No of " + str(list(parent_node)) + " child = " + str(len(list(node_list))))
    states_count = states_count + len(list(node_list))

if __name__ == "__main__":
    '''
    A = input("Enter the maximum capacity of the jug A")
    B = input("Enter the maximum capacity of the jug B")
    x = input("Enter the current water in jug A")
    y = input("Enter the current water in jug B")
    desired_x = input("Water desired in jug A")
    desired_y = input("Water desired in jug B")
    '''
    A = 4
    B = 3
    x = 0
    y = 0
    desired_x = 2
    desired_y = 0

    ms = make_states(A, B)

    add_node(x, y)
    j=0
    current_node = str([curr_node,x,y])
    curr_node = curr_node + 1
    visited = list()
    visited.append(current_node)
    for node in visited:
        for states in graph[str(node)]:
            add_node(states[1], states[2])
            new_node = str([curr_node, states[1], states[2]])
            curr_node = curr_node + 1
            if new_node not in visited:
                visited.append(new_node)
        
    for x in graph:
        print(str(x) + " - " + str(graph[x]))
        if (2, 0) in graph[x]:
            print("Found")
    print("Total No of States = " + str(states_count))
