# For makeing the tree
relations = {}

# Generates the nodes for the graph
def make_tree(n):
	for i in range(int(n)):
	    relations[int(i)] = {}
	print(relations)

# Makeing edges for nodes
def make_relations(e):
	for i in range(int(e)):
		new_line_str = input()
		edges = new_line_str.split(' ')
		x = int(edges[0])
		y = int(edges[1])
		draw_edge(x, y)
	print(relations)

# Drawing edges
def draw_edge(x, y):
	node_names = set(relations[int(x)])
	node_names.add(int(y))
	relations[int(x)] = node_names
