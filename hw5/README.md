README for Problem 1
Vaibhav Gupta
vg6663

To run `python lca.py` with `lca.txt` in the same directory

it was understood that input would be read from a file (as it was not specified)

Some basic testing was done, but the logic seems sound and I was not able to think of any test cases that would fail it

The idea:
LCA(a, b):
	get depth of a and b
	move the one of greater depth up to its parent while the depths are not the same
	if a and b are the same:
		return a (we've found the node)
	else (we need to move up the tree more)
		a = a.parent
		b = b.parent
