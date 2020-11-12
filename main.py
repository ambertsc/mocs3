
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import pycxsimulator
import random as rd

def initialize_variables():
    got = pd.read_csv('stormofswords.csv')
    got = got.rename(columns={'Source': "source", 'Target': "target", 'Weight': "weight"})
    global network_got
    global nodes

    network_got= nx.from_pandas_edgelist(got, edge_attr='weight')
    nodes = network_got.nodes
    nodes = list(nodes)

    for node in nodes:
        network_got.nodes[node]['state'] = 1 if rd.random() < 0.5 else 0

def get_useful_stats():
    global network_got

    print(nx.info(network_got))

    print('average clustering ',nx.average_clustering(network_got))
    cluster = nx.clustering(network_got)
    print('largest cluster ', max(cluster.values()))
    print('largest cluster node ',max(cluster, key=cluster.get))

    centrality = nx.betweenness_centrality(network_got)
    print('largest centrality ',max(centrality.values()))
    print('largest centrality value ',max(centrality,key=centrality.get))


def observe():
    global network_got
    global nodes

    # nx.draw(network_got, cmap=plt.cm.binary, vmin=0, vmax=1,
    #         node_color=[network_got.node[node][’state’] for node in  nodes, pos = network_got.pos)

    color_map = []
    for node in nodes:
        if (network_got.nodes[node]['state'] == 1):
            color_map.append('blue')
        else:
            color_map.append('red')
    nx.draw(network_got, node_color=color_map, with_labels=True)
    plt.show()


# Press the green button in the gutter to run the script.

def update():
    global network_got

    listener = rd.choice(nodes)
    speaker = rd.choice(list(network_got.adj[listener]))

    network_got.nodes[listener]['state'] = network_got.nodes[speaker]['state']


if __name__ == '__main__':
    initialize_variables()
    get_useful_stats()
    pycxsimulator.GUI().start(func=[initialize_variables(), observe(), update()])
