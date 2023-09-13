import cugraph as cnx
import networkx as nx
import time

G = nx.read_edgelist("../Data/facebook_combined.tar")
t1=time.time()
A = cnx.leiden(G)
t2=time.time() - t1
print(t2)
