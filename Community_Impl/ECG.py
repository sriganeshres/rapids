import cugraph 
import networkx as nx
import time
G=nx.barabasi_albert_graph(1000,50)
t1=time.time()
print(t1)
G1=cugraph.ecg(G)
t2=time.time()-t1
print(t2)
