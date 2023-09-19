import cugraph as cnx
import networkx as nx
import time
nodes = int(input())
edges = int(input())
t0 = time.time()
G = nx.barabasi_albert_graph(nodes, edges)
t01 = time.time() - t0
t1 = time.time()
A = cnx.k_core(G) # cugraph
t2 = time.time() - t1
print(f"time taken to create the graph of {nodes} nodes and {nodes*edges} edges is {t01} milliseconds\ntime to find betweenness_centrality is {t2} milliseconds" 
        )
print("k-core graph")
print("\tNumber of vertices:" + str(A.number_of_vertices()))
print("\tNumber of Edges: " + str(A.number_of_edges()))

