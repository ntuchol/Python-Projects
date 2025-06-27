   import networkx as nx
   import matplotlib.pyplot as plt

   # Create a graph object
   G = nx.Graph()

   # Add nodes (adjectives)
   adjectives = ["happy", "sad", "bright", "dark", "loud", "quiet"]
   G.add_nodes_from(adjectives)

   # Add edges (connections between adjectives)
   edges = [("happy", "bright"), ("happy", "loud"), ("sad", "dark"), ("sad", "quiet"), ("bright", "loud"), ("dark", "quiet")]
   G.add_edges_from(edges)