def getMin(G, mstFlag):
    min = sys.maxsize 
    for i in [(u, v, edata['length']) for u, v, edata in G.edges( data = True) if 'length' in edata ]:
    	if mstFlag[i] == False and i[2] < min:
    		min = i[2]
    		min_edge = i
    return min_edge


def findRoot(parent, i):
    if parent[i] == i:
        return i
    return findRoot(parent, parent[i])




def union(parent, order, x, y):
    xRoot = findRoot(parent, x)
    yRoot = findRoot(parent, y)
    if order[xRoot] < order[yRoot]:
        parent[xRoot] = yRoot
    elif order[xRoot] > order[yRoot]:
        parent[yRoot] = xRoot
    else :
        parent[yRoot] = xRoot
        order[xRoot] += 1

def kruskals(G, pos):
	eLen = len(G.edges()) 
	vLen = len(G.nodes()) 
	mst = [] 
	mstFlag = {}
	for i in [ (u, v, edata['length']) for u, v, edata in G.edges(data = True) if 'length' in edata ]:
		mstFlag[i] = False 

 	parent = [None] * vLen 
	order = [None] * vLen	
	for v in range(vLen):
		parent[v] = v
		order[v] = 0
	while len(mst) < vLen - 1 :
		curr_edge = getMin(G, mstFlag) 
		mstFlag[curr_edge] = True 
		y = findRoot(parent, curr_edge[1])
		x = findRoot(parent, curr_edge[0])

		if x != y:
			mst.append(curr_edge)
			union(parent, order, x, y)
	for X in mst:
	 	if (X[0], X[1]) in G.edges():
	 		nx.draw_networkx_edges(G, pos, edgelist = [(X[0], X[1])], width = 2.5, alpha = 0.6, edge_color = 'r')
	return


def CreateGraph():
	G = nx.Graph()
	f = open('Dataset.txt')
	n = int(f.readline())
	wtMatrix = []
	for i in range(n):
		list1 = map(int, (f.readline()).split())
		wtMatrix.append(list1)
	
	for i in range(n) :
		for j in range(n)[i:] :
			if wtMatrix[i][j] > 0 :
					G.add_edge(i, j, length = wtMatrix[i][j]) 
	return G


def DrawGraph(G):
	pos = nx.spring_layout(G)
	nx.draw(G, pos, with_labels = True)  
	edge_labels = nx.get_edge_attributes(G, 'length')
	nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, font_size = 11) 
	return pos


if __name__ == "__main__":
	G = CreateGraph()
	pos = DrawGraph(G)
	kruskals(G, pos)
	plt.show()