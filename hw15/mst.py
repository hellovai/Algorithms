import sys

def Kruskal(G):
    tree = []
    edges = [(G[u][v],u,v) for u in G for v in G[u]]
    edges.sort()
    inTree = set()
    for W,u,v in edges:
    	if u not in inTree or v not in inTree:
    		tree.append((u,v))
    		inTree.update(u)
    		inTree.update(v)
        # if subtrees[u] != subtrees[v]:
        #     tree.append((u,v))
        #     subtrees.union(u,v)
    return tree        

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print "Usage: python mst.py <inputfile>"
		exit()
	G = {}
	for line in open(sys.argv[1]):
		data = line[:-1].split(' ')
		key = data[0]
		neigh = ' '.join(data[1:]).replace('(', '').replace(')','').split(', ')
		G[key] = {}
		for x in neigh:
			adj, weight = x.split(',')
			G[key][adj] = int(weight)
	tree = Kruskal(G)
	mst = {}
	for u, v in tree:
		if u not in mst:
			mst[u] = set()
		if v not in mst:
			mst[v] = set()
		mst[u].update(v)
		mst[v].update(u)
	for x in sorted(mst):
		print x, str([int(i) for i in mst[x]]).replace('[','(').replace(']',')')
	