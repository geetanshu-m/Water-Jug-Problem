# For makeing the tree
relations = {}

# Generates the nodes for the graph
def make_tree(n):
	for i in range(int(n)):
	    relations[int(i)] = set()

# Makeing edges for nodes
def make_relations(e):
	for i in range(int(e)): 
		edges = input().split(' ')
		relations[x] = set(relations[int(edges[0])]).add(int(edges[1]))
	return relations