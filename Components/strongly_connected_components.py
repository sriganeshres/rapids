import cugraph as cnx
import networkx as nx
import cudf
import time
import cupy as cp
nodes = int(input())
edges = int(input())
t0 = time.time()
G = nx.barabasi_albert_graph(nodes, edges)
G1 = nx.read_edgelist("../Data/facebook_combined.tar")
t01 = time.time() - t0
t1 = time.time()
components_cupy = cnx.strongly_connected_components(G1)
t2 = time.time()-t1
components_df = cudf.DataFrame({'vertex': list(components_cupy.keys())})
components_df['labels'] = components_df.index
label_gpy = components_df.groupby('vertex')
label_count = label_gpy.count()
print('Total no of components ', len(label_count))
largest_components = label_count.nlargest(n = 10, columns= 'labels')
print(largest_components)
print(t01, ' s ',  t2 , 's ')
