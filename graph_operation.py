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
                    queue.append(str(x))
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

def dfs(graph, start,visited=list(), dfs=list()):
    stack = list()
    stack.append(start)
    while stack:
        start = stack.pop(-1)
        if start not in visited:
            visited.append(start)
            for x in graph[start]:
                stack.append(x)
            dfs.append(start)
    return dfs
