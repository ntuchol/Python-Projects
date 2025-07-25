import networkx as nx
import matplotlib.pyplot as plt

nutrients = ['Vitamin A', 'Vitamin C', 'Iron', 'Calcium', 'Protein']
relationships = [('Vitamin A', 'Vitamin C', 0.5), ('Vitamin A', 'Protein', 0.8), ('Iron', 'Calcium', 0.7), ('Iron', 'Protein', 0.9)]

G = nx.Graph()

G.add_nodes_from(nutrients)


G.add_weighted_edges_from(relationships)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=1500, node_color="skyblue", font_size=10, font_weight="bold")
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
plt.show()

degree_centrality = nx.degree_centrality(G)
print("Degree Centrality:", degree_centrality)
