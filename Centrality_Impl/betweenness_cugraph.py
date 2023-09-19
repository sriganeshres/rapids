import cugraph as cnx
import networkx as nx
import time 
nodes = int(input())
edges = int(input())
t0 = time.time()
G = nx.barabasi_albert_graph(nodes, edges)
t01 = time.time() - t0
t1 = time.time()
A = cnx.betweenness_centrality(G) # cugraph
t2 = time.time() - t1 
#A.sort_values(by='betweenness_centrality', ascending=False).head(5)
print(f"time taken to create the graph of {nodes} nodes and {nodes*edges} edges is {t01} milliseconds\ntime to find betweenness_centrality is {t2} milliseconds" )
maxi = - 1
maxKey = ''
for key in A.keys():
    if (A[key] > maxi):
        maxi = A[key]
        maxKey = key
print(maxi, maxKey)
