'''
@TODO Mapping of nodes(0,0) and keys(0) to prevent overridding
'''
from make_states import make_states
import graph_operation as go
from graphviz import Graph

graph = {}
states_count = 0

def add_node(x, y):
    '''
    Denoteing each node child
    params : current capacity in A, current capacity in B, previous related node
    '''
    global states_count 
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

    final_node_list = list()
    for x in node_list:
        x = list(x)
        final_node_list.append(x)

    graph[str(list(parent_node))] = final_node_list 
    # print("No of " + str(list(parent_node)) + " child = " + str(len(list(node_list))))
    states_count = states_count + len(final_node_list )

def create_graph(x,y):
    add_node(x, y)
    current_node = str([x,y])
    visited = list()
    visited.append(current_node)
    for node in visited:
        for states in graph[node]:
            add_node(states[0], states[1])
            new_node = str([states[0], states[1]])
            if new_node not in visited:
                visited.append(str([states[0], states[1]]))

def print_graph():
    for x in graph:
        print(str(x) + " - " + str(graph[x]))
        if [2, 0] in graph[x]:
            print("Found")
    print("Total No of States = " + str(states_count))

def generate_graph_image():
    g = Graph('G', filename='process.gv', engine='sfdp')
    for i,x in enumerate(graph):
        for j,y in enumerate(graph[x]):
            print("u.edge(str((",i,",",x,")),str((",j+i,",",y,")))")

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
    
    create_graph(x,y)

    print_graph()

    '''
    start = str([0,0])
    print(go.bfs(graph, start))
    '''
    print("All posible path")
    print(graph)
    start = str([0,0])
    print(go.bfs(graph, start))
