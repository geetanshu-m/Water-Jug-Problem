# For makeing the tree
nodes = []
relations = {}

# Generates the nodes for the graph
def make_tree(n):
	for i in range(int(n)):
	    nodes.append(chr(i+65))
	print(nodes)

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
	if chr(x+65) in relations:
		node_names = set(relations[chr(x+65)])
		node_names.add(chr(y+65))
		relations[chr(x+65)] = node_names
	else:
		relations[chr(x+65)] = (chr(y+65))
