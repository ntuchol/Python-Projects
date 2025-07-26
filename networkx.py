   import networkx as nx
   import matplotlib.pyplot as plt

   G = nx.Graph()

   adjectives = ["happy", "sad", "bright", "dark", "loud", "quiet"]
   G.add_nodes_from(adjectives)

   edges = [("happy", "bright"), ("happy", "loud"), ("sad", "dark"), ("sad", "quiet"), ("bright", "loud"), ("dark", "quiet")]
   G.add_edges_from(edges)
