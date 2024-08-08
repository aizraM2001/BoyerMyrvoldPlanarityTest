import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout
import numpy as np
from collections import deque


class Graph():
    def __init__(self):
        self.G= nx.Graph()
        #Numero Nodi
        self.V= 0
        #Numero Archi
        self.E= 0
        self.palmTree = nx.Graph()
        self.DFStree = nx.Graph()
        self.componentiG = []
        self.subgraphComponentiDFS = []
        self.componentiDFS = []
        self.DFI = 1

    def addNode(self, v):
        self.G.add_node(str(v), dfi=0, visited = False)
        self.V+=1
    
    def setDFI(self, v, dfi):
        #self.palmTree.nodes[v]['dfi'] = dfi
        self.G.nodes[v]['dfi'] = dfi
        
    def getDFI(self, v):
        if type(v) == int and v in self.palmTree.nodes():
            return self.palmTree.nodes[v]['dfi']
        elif v!=0:
            return self.G.nodes[v]['dfi']
        else:
            return 0

    def setName(self, v, name):
        #self.palmTree.nodes[v]['dfi'] = dfi
        self.G.nodes[v]['name'] = name
        
    def getName(self, v):
        if type(v) == int:
            return self.palmTree.nodes[v]['name']
        else:
            self.G.nodes[v]['name']

    def addEdge(self, v, w):
        self.addNode(v)
        self.addNode(w)
        self.G.add_edge(str(v), str(w), backedge = False, color = 'black')
        self.E+=1

    def addEdgeDFS(self, v, w):
        v=self.getDFI(v)
        w=self.getDFI(w)
        self.addNode(v)
        self.addNode(w)
        self.G.add_edge(v, w, backedge = False, color = 'black')
           
    def add_edges_from(self, edges):
        for i in edges:
            x, y = i
            self.addEdge(x,y)

    def printGrafo(self, H):
        edge_colors = [H[u][v]['color'] for u, v in H.edges()]
        # Disegna il grafo
        pos = nx.spring_layout(H)
        nx.draw(H, pos, with_labels=True,
                node_size=500, node_color="skyblue", font_size=12,
                font_color="black", font_weight="bold", edge_color=edge_colors)
        
        for nodo, (x, y) in pos.items():
            parametro = self.getDFI(nodo)
            plt.text(x, y + 0.05, f'{parametro}', fontsize=12,
                      ha='center', va='center', color='green')

        #Legenda
        plt.scatter([], [], c='green', label='DFI')
        plt.legend(scatterpoints=1, frameon=False, labelspacing=1, loc='upper right')
        # Mostra il grafo
        plt.show()
    
    def stampa_attributi_nodo(self,grafo, nodo):
        attributi = grafo.nodes[nodo]
        print(f"Attributi del nodo {nodo}:")
        for chiave, valore in attributi.items():
            print(f"  {chiave}: {valore}")
        
    def stampa_attributi_arco(self, grafo, nodo1, nodo2):
        attributi = grafo[nodo1][nodo2]
        print(f"Attributi dell'arco {nodo1}-{nodo2}:")
        for chiave, valore in attributi.items():
            print(f"  {chiave}: {valore}")

    def getLowpoint(self, v):
           v = self.getDFI(v)
           return self.palmTree.nodes[v]['lowpoint']
    
    def setLowpoint(self, v, value):
            self.palmTree.nodes[v]['lowpoint'] = value
      
    def printLowpoint(self):
        for v in list(self.G.nodes()):
            print(v,"--> DFI: ", self.getDFI(v), " Lopt1: ", self.getLowpoint(v))        

    #H= albero da stampare b = Tru voglio i backEdge /False NON voglio i backEdge
    def printAlbero(self, H, b):
        edge_colors = [H[u][v]['color'] for u, v in H.edges()]
        #print(edge_colors)
        if b == False:
            for i in range(0, len(edge_colors)):
                if edge_colors[i] == 'red': 
                    edge_colors[i] = 'white'
                    #print(edge_colors[i])

        """ for i in list(H.nodes()):
            self.stampa_attributi_nodo(H, i)
        
        for i in list(H.edges()):
            x,y = i
            self.stampa_attributi_arco(H, x, y) """

        pos = nx.spring_layout(H)
        # Imposta la posizione della radice (nodo 0) in un punto specifico
        #pos[0] = (0, 0)  # posiziona la radice al centro in alto
        # Crea un dizionario di etichette con controllo della chiave 'name'
        labels = {x: self.palmTree.nodes[x]['name'] for x in self.palmTree.nodes()}
        nx.draw(H, pos, labels=labels, with_labels=True, node_size=500, 
                node_color="skyblue", font_size=12, font_color="black", 
                font_weight="bold", edge_color = edge_colors)
        
        for nodo, (x, y) in pos.items():
            parametro = self.getDFI(nodo)
            plt.text(x, y + 0.05, f'{parametro}', fontsize=12,
                      ha='center', va='center', color='green')
        
        #Legenda
        plt.scatter([], [], c='green', label='DFI')
        plt.legend(scatterpoints=1, frameon=False, labelspacing=1, loc='upper right')    
        plt.show()
       
    def __str__(self):
        print("Numero Nodi: ", self.V)
        print("Numero Archi: ", self.E)
        #self.printGrafo(self.G)
        for v in list(self.G.nodes()):
            print(v, ":", list(self.G.neighbors(v)))
        return ""
  
    def printDFStree(self):
        if self.palmTree.number_of_nodes() > 0:
            self.printAlbero(self.palmTree , True)
        else:
            self.DFS(list(self.G.nodes())[0], 0)
            print("# len palm tree", len(self.palmTree.edges()))
            for i in self.palmTree.edges():
                x, y = i
                if self.palmTree[x][y]['backedge'] == False:
                    self.DFStree.add_edge(x, y, color = 'black')
            self.printAlbero(self.palmTree , True)

    def printComponentiDFS(self):
        if len(self.subgraphComponentiDFS) > 0:
            for i in self.subgraphComponentiDFS:
                self.printGrafo(i)
        else:
            # Crea i sottografi biconnessi
            for i in self.DFStree.edges():
                subgraph = self.DFStree.subgraph(i).copy()
                self.subgraphComponentiDFS.append(subgraph)
                #self.printGrafo(subgraph)
            print("Qta componenti: ",len(self.subgraphComponentiDFS))
            for i in self.subgraphComponentiDFS:
                print(i)
                #self.printGrafo(subgraph)      

    def DFS(self, s, u):
         #self.palmTree.add_node(s, dfi=self.DFI)
         #self.DFStree.add_node(s, dfi=self.DFI)
         self.palmTree.add_node(self.DFI, name = s, dfi = self.DFI)
         self.DFStree.add_node(self.DFI, name = s, dfi = self.DFI, adjacencyList = [])
         self.G.add_node(s, dfi=self.DFI)
         oldS=s
         s = self.DFI
         self.palmTree.nodes[s]['visited'] = True
         self.setLowpoint(s, self.DFI)
         self.DFI+=1
         if u != 0:
            #Cre un arco padre e nodo attuale (Così ho il DFI di tutti e due)
            self.palmTree.add_edge(self.getDFI(u), self.getDFI(s), A=self.getName(u), B=self.getName(s), backedge = False, color = 'black')
            self.DFStree.add_edge(self.getDFI(u), self.getDFI(s), A=self.getName(u), B=self.getName(s), backedge = False, color = 'black')
            #stack.append((u,w))
         for w in list(self.G.neighbors(oldS)):
            #if self.palmTree.nodes[self.getDFI(w)]['visited'] == False or self.palmTree.nodes[self.getDFI(w)] not in  self.palmTree:
            if not self.getDFI(w) in self.palmTree:
                 #self.palmTree.add_edge(s, w, backedge = False, color = 'black')
                 #self.DFStree.add_edge(s, w, backedge = False, color = 'black')
                 #stack.append((s,w))
                 #Funzione ricorsiva
                 self.DFS(w, s)
                 self.setLowpoint(s, min(self.getLowpoint(s), self.getLowpoint(w)))
            #elif self.getDFI(w)< self.getDFI(s) and self.palmTree.nodes[self.getDFI(w)] != self.palmTree.nodes[u]:
            elif u!=0 and self.palmTree.nodes[self.getDFI(w)] != self.palmTree.nodes[u]:
                self.setLowpoint(s, min(self.getLowpoint(s), self.getDFI(w)))
                if self.palmTree.has_edge(self.getDFI(w), s) == False:
                    #self.palmTree.add_edge(s, w, backedge = True, color = 'red')
                    self.palmTree.add_edge(self.getDFI(s), self.getDFI(w), A=self.getName(s), B=w, backedge = True, color = 'red')
      
    #bucketSort O(#archi+#nodi)
    def ordinaLowpoint(self):
        
        # Inizializziamo i bucket come liste vuote
        bucket = [[] for _ in range(0, len(list(self.DFStree.nodes()))+1)]

        # Aggiungiamo w ai bucket corretti
        for i in list(self.DFStree.edges()):
            v, w = i
            lowpoint = self.getLowpoint(self.getDFI(w))
            bucket[lowpoint].append((v, self.getDFI(w)))

        # Aggiorniamo la lista di adiacenza di v con i valori di w dai bucket
        #adjacency_list = {v: [] for v in self.G.nodes()}

        
        for lowpoint in range(len(bucket)):
            for v, w in bucket[lowpoint]:
                self.DFStree.nodes[v]["adjacencyList"].append(w)

        # Stampa per verificare la lista di adiacenza
        print("Lista di adiacenza:")
        for v in  self.DFStree.nodes():
            print(f"{v}: {self.DFStree.nodes[v]["adjacencyList"]}")
      
        
        