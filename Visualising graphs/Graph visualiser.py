import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
#edge=("a","b")

n=int(input())
for i in range(n):
	edge=tuple(int(x.strip()) for x in input().split())
	G.add_edge(*edge)

#G.add_node("a");
#G.add_nodes_from(edge)


print("Nodes: ",G.nodes())
print("Edges: ",G.edges())
nx.draw(G)
plt.savefig("graph1.png") #change name of file
plt.show()  #immediate output
