# import generating_graph	as gp
import graph_operation as go


if __name__ == '__main__':
	graph = {0: [1, 2], 1: [4], 2: [3, 6, 1], 3: [5], 4: [7], 5: [], 6: [], 7: []}
	print(graph)
	print(go.dfs(graph, 0))
