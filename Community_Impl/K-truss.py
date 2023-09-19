import cugraph as cnx
import cudf
import networkx as nx
import time
t1=time.time()
G = nx.barabasi_albert_graph(100,7)
cg = cnx.Graph()
cg.from_networkx(G)
t2=time.time()
kcg = cnx.ktruss_subgraph(cg,7)
t3=time.time()
print(t2-t1)
print(t3-t2)
print(kcg)
