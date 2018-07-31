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
    # print("No of " + str(list(parent_node)) + " child = " + str(len(list(node_list))))
    states_count = states_count + len(list(node_list))
    print("stack",stack)

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

    add_node(int(0),x,y)
    
    current_node = str(list([int(0),x,y]))
    stack.append(current_node)
    print("stack1",stack)
    i = 0
    for states in graph[stack[-1]]:
        if i == 0:
            i = i + 1
        else:
            x = list(stack[-1])
            add_node(int(x[1]), states[0], states[1])
            del stack[-1]
    
    for x in graph:
        print(str(x) + " - " + str(graph[x]))
        if (2, 0) in graph[x]:
            print("Found")
    print("Total No of States = " + str(states_count))
