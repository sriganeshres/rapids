import cugraph as cnx
import networkx as nx
import time
G=nx.barabasi_albert_graph(1000,500)

t1=time.time()
G1,mod=cnx.louvain(G)
t2=time.time()-t1
print(t2, mod)
