import cugraph as cnx
import cudf
import networkx as nx
import time
t1=time.time()
G=nx.barabasi_albert_graph(1000000,500)
t2=time.time()
triangles_per_vertex = cnx.triangle_count(G)
t3=time.time()
result = triangles_per_vertex["counts"].sum()
print(t2-t1)
print(t3-t2)
print(result)
