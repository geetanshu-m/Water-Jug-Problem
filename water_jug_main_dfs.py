'''
@TODO Mapping of nodes(0,0) and keys(0) to prevent overridding
'''
from make_states import make_states
import graph_operation as go
from graphviz import Graph
from graphviz import Digraph

graph = {}
states_count = 0
child_count = 0
possible_path = []
stack = []

def add_node(i, parent, x, y):
    '''
    Denoteing each node child
    params : current capacity in A, current capacity in B, previous related node
    '''
    global states_count, child_count, possible_path, stack
    parent_node = [x, y]
    node_list = set()

    init = i

    # Generateing the nodes
    node_list.add(ms.fillA(parent_node[0], parent_node[1]))
    node_list.add(ms.fillB(parent_node[0], parent_node[1]))
    node_list.add(ms.pourBtoA(parent_node[0], parent_node[1]))
    node_list.add(ms.pourAtoB(parent_node[0], parent_node[1]))
    node_list.add(ms.emptyA(parent_node[0], parent_node[1]))
    node_list.add(ms.emptyB(parent_node[0], parent_node[1]))

    # Removing unwanted
    if (0,0) in node_list:
        node_list.remove((0,0))
    if (parent_node[0], parent_node[1]) in node_list:
        node_list.remove((parent_node[0], parent_node[1]))

    parent_node = [init, parent, x, y]

    # Cleaning list
    final_node_list = list()
    for x in node_list:
        x = list(x)
        i = i + 1
        child_count = child_count + 1
        x.insert(0, child_count)
        x.insert(1, init)
        stack.append(x)
        final_node_list.append(x)

    # Adding to the Graph
    graph[str(list(parent_node))] = final_node_list 

    # print("No of " + str(list(parent_node)) + " child = " + str(len(list(node_list))))
    states_count = states_count + len(final_node_list )

def create_graph(x,y):
    add_node(0,'null', x, y)
    stack.append(str([0,'null',x,y]))
    k = 0
    while stack:
        start = stack.pop(-1)
        print(start)
        for states in graph[start]:
            add_node(states[0], states[1], states[2], states[3])
        if k is 5:
            break
        k = k + 1

def print_graph():
    n=0
    for x in graph:
        #print(str(x) + " - " + str(graph[x]))
        for x in graph[x]:
            if x[2] is 2:
                path = trace_path(x[1])
                path.insert(0,x)
                possible_path.append(path)
                n = n + 1
                #print("Found")
    print("Total No of States = ", str(states_count), " And A=2 are ", n)

def generate_graph_image():
    #u = Digraph('Water Jug', filename='water_jug.png')
    u = Digraph('Water Jug', filename='water_jug_bfs')
    #u.attr(size='6,6')
    u.node_attr.update(color='lightblue2', style='filled')

    for x in graph:
        for y in graph[x]:
            u.edge(str((x)),str((y)))
    u.view()

def trace_path(parent_id,path=[]):
    for x in graph:
        for x in graph[x]:
            if x[0] is parent_id:
                path.append(x)
                trace_path(x[1])
    return path     

def print_all_possible_path():
    for x in possible_path:
        print('(',0,',',0,')', end= '->')
        for y in x[::-1]:
            print('(',y[2],',',y[3],')', end= '->')
            if y[2] is 2:
                break
        print('\n')

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

    print_all_possible_path()

    #generate_graph_image()

    '''
    start = str([0,0])
    print(go.bfs(graph, start))
    
    print("All posible path")
    print(graph)
    start = str([0,0])
    print(go.bfs(graph, start))
    '''