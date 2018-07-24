import generating_graph	as gp
import graph_operation as go


if __name__ == '__main__':
	new_line_str = input()
	input_str = new_line_str.split(' ')
	n = int(input_str[0])
	e = int(input_str[1])
	gp.make_tree(n)
	graph = gp.make_relations(e)
	print(graph)
	go.bfs(graph, 0)
