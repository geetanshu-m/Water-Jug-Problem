'''
Provides basic operations on the graph
Operation
 - BFS
 - BFS - Path
 - DFS
 - DFS - Path
'''

def bfs(graph, start, visited=list(), bfs=list()):
    queue = list()
    queue.append(start)
    ##print(len(list(graph.keys())))
    while queue:
        #print("_"*20)
        if start not in visited:
            #print("in IF")
            visited.append(start)
            for x in graph[start]:
                if x not in visited:
                    queue.append(x)
            bfs.append(queue[0])
        #print(queue)
        del queue[0]
        #print(queue)
        #print(visited)
        #print(bfs)
        if queue:
            #print(queue[0])
            start = queue[0]
    return bfs

def dfs(graph, start, dfs=list()):
    stack = list()
    stack.append(start)
    i = 0
    while stack:
        print("start of graph is", graph[start])
        start = stack.pop(-1)
        for x in graph[start]:
            print("x in graph is", x)
            stack.append(x)
        print(stack, start)
        dfs.append(start)
        i = i + 1
        if i == 10:
            break
    return dfs
