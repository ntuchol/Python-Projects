import networkx as nx
    import pandas as pd

    G = nx.Graph()
    G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4)])

    nodes_df = pd.DataFrame(G.nodes(data=True), columns=['Id', 'Attributes'])
    edges_df = pd.DataFrame(G.edges(), columns=['Source', 'Target'])

    nodes_df.to_csv('nodes.csv', index=False)
    edges_df.to_csv('edges.csv', index=False)
