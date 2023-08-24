import cugraph as cnx
import networkx as nx
import time 
nodes = int(input())
edges = int(input())
t0 = time.time()
G = nx.barabasi_albert_graph(10000, 500)
t01 = time.time() - t0
t1 = time.time()
# A = nx.betweenness_centrality(G) #for networkx
A = cnx.betweenness_centrality(G) # cugraph
t2 = time.time() - t1 
print(f"time taken to create the graph of {nodes}nodes and {edges} edges is {t01} milliseconds\n time to find betweenness_centrality is {t2} milliseconds" )
