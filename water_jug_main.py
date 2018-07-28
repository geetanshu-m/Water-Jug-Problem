import make_states as ms

graph = {}

def add_node(x, y):
    '''
    Denoteing each node child
    params : current capacity in A, current capacity in B, previous related node
    '''
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

    graph[str(set(parent_node))] = node_list
    

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

    add_node(x, y)
    
    current_node = str(set([x,y]))

    node_queue = set()
    node_queue.add(current_node)
    i = 0
    for x in list(node_queue):
        m=0
        first_node=''
        for states in graph[x]:
            add_node(states[0], states[1])
            if m is 0:
                first_node = str(set([states[0], states[1]]))
            current_node = str(set([states[0], states[1]]))
            node_queue.add(current_node)
            print("node queue" + str(node_queue))
        node_queue.remove(first_node)
        print("node queue" + str(node_queue))
        i = i + 1
        if i is 10:
            break
        
    print(graph)