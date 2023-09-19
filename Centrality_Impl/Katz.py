import cugraph as cnx
import networkx as nx
import time
nodes =int(input())
edges =int(input())
t0 = time.time()
G = nx.barabasi_albert_graph(nodes,edges)
t01 = time.time() - t0
degree = [G.degree(node) for node in G.nodes()]
lamda = max(degree)
print('The max degree is ' + str(lamda))
alpha = 1 / lamda
t1 = time.time()
A = cnx.katz_centrality(G, alpha = alpha)
t2 = time.time() - t1
print(f"{t01} s, {t2} s")
