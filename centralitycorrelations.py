import networkx as nx
import pandas as pd

# Create a sample graph
graph = nx.karate_club_graph()

# Calculate centrality measures
degree_centrality = nx.degree_centrality(graph)
betweenness_centrality = nx.betweenness_centrality(graph)
closeness_centrality = nx.closeness_centrality(graph)

# Store in a DataFrame
centrality_df = pd.DataFrame({
    'degree': degree_centrality,
    'betweenness': betweenness_centrality,
    'closeness': closeness_centrality
}).T

centrality_df.columns = ['node_' + str(i) for i in range(centrality_df.shape[1])]

# Calculate correlations
correlations = centrality_df.corr()

print(correlations)