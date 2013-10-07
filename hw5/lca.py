# doing LCA

tree = dict(); # in {child:parent}

def height(x):
	h = 0
	while x in tree and tree[x] is not None:
		x = tree[x]
		h = h + 1
	return h

def LCA(x, y):
	hx = height(x)
	hy = height(y)
	if( hx < hy ):
		hx, hy = hy, hx
		x, y = y, x
	diff = hx - hy
	for _ in xrange(diff):
		if x in tree:
			x = tree[x]
	while x in tree and y in tree:
		if x is y:
			return x
		else:
			x = tree[x]
			y = tree[y]
	return None

if __name__ == '__main__':
	f = open('lca.txt')
	for line in f:
		x, _, z = line[0:-1].split(' ')[0:3]
		x = int(x)
		z = ''.join(c for c in z if c.isdigit())
		z = int(z) if len(z) > 0 else 0
		tree[x] = z
	for i in xrange(1,6):
		for j in xrange(1,6):
			print LCA(i, j), 
		print ""
		