import sys

def eulerPath(graph):
    # counting the number of vertices with odd degree
    odd = [ x for x in graph.keys() if len(graph[x]) % 2 == 1 ]
    if len(odd)>3:
        return [-1]

    # we'd wanna start with a node with odd degrees if it exists, otherwise just pick the first node
    odd.append(graph.keys()[0])
    stack = [ odd[0] ]
    eulerPath = []
    
    while stack:
        node = stack.pop()
        if graph[node]:
            # get an edge and remove it from the graph
            neighbor = graph[node][0]
            del graph[neighbor][ graph[neighbor].index(node) ]
            del graph[node][0]
            # push both back on the stack since they still are useful
            stack.append(node)
            stack.append(neighbor)
            # print graph
            # print stack
        else:
            # remove the node from the graph
            eulerPath.append( node )
    
    # confirm that every node is indeed there, in case of isolated nodes
    if set(eulerPath) != set(graph.keys()):
        return [-1]
    # the path is poped is reverse order so reverse it
    return eulerPath[::-1]

def trim(arr):
    arr = arr.split(',')
    arr[0] = arr[0][1:]
    arr[-1] = arr[-1][:-1]
    if arr[0] == '':
        return []
    if arr[-1][-1] == ')':
        arr[-1] = arr[-1][0:-1]
    if len(arr[0]) > 0:
        for i in xrange(len(arr)):
            arr[i] = int(arr[i])
    else:
        arr = []
    return arr

if __name__ == '__main__':
    graph = {}
    f = open('output.txt', 'w')
    for line in sys.stdin:
        index, arr = line.split(' ')
        graph[int(index)] = trim(arr)
    barriar = ""
    for x in eulerPath(graph):
        f.write(barriar)
        f.write(str(x))
        barriar = " "
    f.close()