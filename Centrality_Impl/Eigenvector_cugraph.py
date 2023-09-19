import cugraph as cnx
import networkx as nx
import time
nodes=int(input())
edges=int(input())
t0=time.time()
G=nx.barabasi_albert_graph(nodes,edges)
t01=time.time()-t0
t1=time.time()
A=cnx.eigenvector_centrality(G,max_iter=1000)
t2=time.time()-t1
print(f"time tiken  for creating graph of{nodes} nodes and {edges} edges is {t01} milliseconds \n time to find eigenvector_centrality is{t2} milliseconds")
maxi=-1
maxkey= ''
for key in A.keys():
    if(A[key]>maxi):
        maxi=A[key]
        maxkey=key
print(maxi, maxkey)
