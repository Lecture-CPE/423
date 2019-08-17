import networkx as nx
import matplotlib.pyplot as plt
import sys


def minDistance(dist, sptSet, V):
   	min = sys.maxsize 
   	for v in range(V):
   		if sptSet[v] == False and dist[v] <= min:
   			min = dist[v]
   			min_index = v
	return min_index

 
def dijsktras(G, source, pos):
	V = len(G.nodes()) 
	dist = [] 
	parent = [None]*V 
	sptSet = [] 
	
	for i in range(V):
		dist.append(sys.maxsize)
		sptSet.append(False)
	dist[source] = 0
	parent[source]= -1 
	for count in range(V-1):
		u = minDistance(dist, sptSet, V) 
		sptSet[u] = True
		
		for v in range(V):
			if (u, v) in G.edges():
				if sptSet[v] == False and dist[u] != sys.maxsize and dist[u] + G[u][v]['length'] < dist[v]:
					dist[v] = dist[u] + G[u][v]['length']
					parent[v] = u
	
	for X in range(V):
		if parent[X] != -1: 
			if (parent[X], X) in G.edges():
				nx.draw_networkx_edges(G, pos, edgelist = [(parent[X], X)], width = 2.5, alpha = 0.6, edge_color = 'r')
	return




def CreateGraph():
	G = nx.DiGraph()
	f = open('Dataset.txt')
	n = int(f.readline())
	wtMatrix = []
	for i in range(n):
		list1 = map(int, (f.readline()).split())
		wtMatrix.append(list1)
	source = int(f.readline()) 
	for i in range(n) :
		for j in range(n) :
			if wtMatrix[i][j] > 0 :
					G.add_edge(i, j, length = wtMatrix[i][j]) 
	return G, source



 
def DrawGraph(G):
	pos = nx.spring_layout(G)
	nx.draw(G, pos, with_labels = True) 
	edge_labels = dict([((u, v), d['length']) for u, v, d in G.edges(data = True)])
	nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labels, label_pos = 0.3, font_size = 11) 
	return pos


if __name__ == "__main__":
	G,source = CreateGraph()
	pos = DrawGraph(G)
	dijsktras(G, source, pos)
	plt.show()