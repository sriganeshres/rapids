import cugraph as cnx
import networkx as nx
import time 
nodes = int(input())
edges = int(input())
t0 = time.time()
G = nx.barabasi_albert_graph(nodes, edges)
t01 = time.time() - t0
t1 = time.time()
A = cnx.edge_betweenness_centrality(G) # cugraph
t2 = time.time() - t1 
print(f"time taken to create the graph of {nodes} nodes and {edges} edges is {t01} milliseconds\ntime to find betweenness_centrality is {t2} milliseconds" )
