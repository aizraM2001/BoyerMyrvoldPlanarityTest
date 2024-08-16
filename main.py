import networkx as nx
import GraphV2 
from inputV2 import g
import plot 

#print(g)

gt = nx.Graph()
#reale = 1

for i in range(g.DFI-1, 0,-1):
    #print(i)

    for j in g.DFStree.neighbors(i):
        if j>i:
            #print("Arco:", i, j)
            cb= nx.Graph()
            cb.add_node(i, DFI = g.getDFI(i), name = g.getName(i))
            cb.add_node(j, DFI = g.getDFI(j), name = g.getName(j))
            cb.add_edge(i, j)
            cb.nodes[j]["reale"] = True
            cb.nodes[i]["reale"] = i
            cb.nodes[i]["root"] = True
            #sd = g.creaStrutturaListe(cb,i,[])
            nx.set_node_attributes(cb, str(i) + str(j), 'graph_id')
            gt = nx.disjoint_union(gt, cb)
            #print(gt)
            #plot.printGrafo(gt)

    for e in g.G.nodes[g.getName(i)]["backEdgeList"]:
        print(f"nodo: {i}, backedge: {e}")
        v, w = e
        #print("sd: ", sd)
        g.walkup(gt, v, w)
            

        
