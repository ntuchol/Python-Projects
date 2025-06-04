import networkx as nx
import matplotlib.pyplot as plt

# Example data (replace with your actual data)
nutrients = ['Vitamin A', 'Vitamin C', 'Iron', 'Calcium', 'Protein']
relationships = [('Vitamin A', 'Vitamin C', 0.5), ('Vitamin A', 'Protein', 0.8), ('Iron', 'Calcium', 0.7), ('Iron', 'Protein', 0.9)]

# Create a graph
G = nx.Graph()

# Add nodes
G.add_nodes_from(nutrients)

# Add edges with weights
G.add_weighted_edges_from(relationships)

# Visualize the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=1500, node_color="skyblue", font_size=10, font_weight="bold")
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))
plt.show()

# Perform analysis (e.g., centrality)
degree_centrality = nx.degree_centrality(G)
print("Degree Centrality:", degree_centrality)