# For makeing the tree
relations = {}

# Generates the nodes for the graph
def make_tree(n):
	for i in range(int(n)):
	    relations[int(i)] = list()

# Makeing edges for nodes
def make_relations(e):
	for _ in range(int(e)):
		new_line_str = input()
		edges = new_line_str.split(' ')
		x = int(edges[0])
		y = int(edges[1])
		draw_edge(x, y)
	return relations

# Drawing edges
def draw_edge(x, y):
	node_names = list(relations[x])
	node_names.append(y)
	relations[x] = node_names
