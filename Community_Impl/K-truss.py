import cugraph
import cudf
import time
from cugraph.datasets import karate
G= karate.get_graph(download=True)
G=G.to_undirected()
print("Main Graph")
print("Number of vertices: " + str(G.number_of_vertices()))
print("NUmber of edges :  " + str(G.number_of_edges()))
t1=time.time()
kcg=cugraph.ktruss_subgraph(G,3)
t2=time.time()
print(t2-t1)
print("K-truss Graph")
print("Numberof Vertices:" +str(kcg.number_of_vertices()))
print("NUmber of edges"+str(kcg.number_of_edges()))


