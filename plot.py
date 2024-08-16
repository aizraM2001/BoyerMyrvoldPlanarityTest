import matplotlib.pyplot as plt
import networkx as nx
import GraphV2 

def printGrafo(H):
        # Disegna il grafo
        pos = nx.spring_layout(H)
        labels = nx.get_node_attributes(H, 'name')
        nx.draw(H, pos, with_labels=True, labels=labels,
                node_size=500, node_color="skyblue", font_size=12,
                font_color="black", font_weight="bold", edge_color="black")
        
        for nodo, (x, y) in pos.items():
            parametro = H.nodes[nodo]["DFI"]
            plt.text(x, y + 0.05, f'{parametro}', fontsize=12,
                      ha='center', va='center', color='green')
     

        #Legenda
        """ plt.scatter([], [], c='green', label='DFI')
        plt.legend(scatterpoints=1, frameon=False, labelspacing=1, loc='upper right') """
        # Mostra il grafo
        plt.show()