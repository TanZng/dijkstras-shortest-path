import plotly.graph_objects as go
import plotly.express as px
import networkx as nx

import random

def leer_grafo(file_name):
    '''
    Recibe el nombre del archivo de txt a leer
    y regresa el grafo contenido en el.
    '''

    # Leer el archivo del que se desea crear el grafo
    f = open(file_name, "r")

    #La primera linea contiene el número de vértices que contiene el grafo
    n = int(f.readline())

    # Crear Grafo
    G = nx.DiGraph()

    pos = {i: [random.gauss(0, 2), random.gauss(0, 2)] for i in range(1, n+1)}
    G.add_nodes_from(pos.keys())

    for n, p in pos.items():
        G.nodes[n]['pos'] = p

    # A partir de la segunda linea nos encontramos
    # origen, destino, costo
    x = f.readline()

    while x != "":
        y = x.split()
        origen = int(y[0])
        destino = int(y[1])
        costo = float(y[2])

        G.add_edge(origen, destino, weigth=costo)

        x = f.readline()
    return G
'''
G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(2,4)
G.add_edge(1,5)
'''

# Create Edges / vertices
def get_plot(G):
    edge_x = []
    edge_y = []
    for edge in G.edges():
        #print(G.nodes(data = True))
        x0, y0 = G.nodes[edge[0]]['pos']
        x1, y1 = G.nodes[edge[1]]["pos"]
        edge_x.append(x0)
        edge_x.append(x1)
        edge_x.append(None)
        edge_y.append(y0)
        edge_y.append(y1)
        edge_y.append(None)

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=0.5, color='#888'),
        hoverinfo='none',
        mode='lines')

    camino_x = []
    camino_y = []
    for edge in G.edges():
        #print("edge: ", edge)
        #print(edge == (0, 1))
        if edge == (0, 1):
            x0, y0 = G.nodes[edge[0]]['pos']
            x1, y1 = G.nodes[edge[1]]["pos"]
            edge_x.append(x0)
            edge_x.append(x1)
            edge_x.append(None)
            edge_y.append(y0)
            edge_y.append(y1)
            edge_y.append(None)

    short_edge = go.Scatter(
        x=camino_x, y=camino_y,
        line=dict(width=2, color='#888'),
        hoverinfo='none',
        mode='lines')

    node_x = []
    node_y = []
    for node in G.nodes():
        x, y = G.nodes[node]['pos']
        node_x.append(x)
        node_y.append(y)

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        hoverinfo='text',
        marker=dict(
            showscale=True,
            # colorscale options
            # 'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
            # 'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
            # 'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
            colorscale='YlGnBu',
            reversescale=True,
            color=[],
            size=10,
            colorbar=dict(
                thickness=15,
                title='Node Connections',
                xanchor='left',
                titleside='right'
            ),
            line_width=2))

    # Color Node Points

    node_adjacencies = []
    node_text = []
    for node, adjacencies in enumerate(G.adjacency()):
        conect = len(adjacencies[1])
        node_adjacencies.append(conect)

        # Obtiene las conexiones y el pesos de las mismas
        #conex = ""
        #for i in adjacencies[1]:
        #    conex += "(" + str(i) + ", w=" + str(adjacencies[1][i]["weigth"]) + ") "
        #node_text.append("Node " + str(node+1) + ', Connected with: ' + conex)

        # Get number of connections
        node_text.append("Node " + str(node + 1) + ', # of connections: ' + str(conect))
        #print("Nodo ", node)
        #print("Adjacencies ", adjacencies)

    node_trace.marker.color = node_adjacencies
    node_trace.text = node_text

    # Create Network Graph

    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=20, l=5, r=5, t=40),
                        annotations=[dict(
                            text="Python code: <a href='https://tanx.dev/'> tanx.dev</a>",
                            showarrow=False,
                            xref="paper", yref="paper",
                            x=0.005, y=-0.002)],
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                    )

    #fig.show()
    #fig.update_layout(
    #    autosize=True,
    #    width=800,
    #    height=400
    #)
    config = {'toImageButtonOptions': # for responsive
          {'width': 1000,
           'height': 400,
           'format': 'svg',
           'filename': 'bar_chart'}}

    fig.write_html("templates/file.html", include_plotlyjs='cdn', full_html = True, config=config)

def run(nombre_archivo):
    G = leer_grafo(nombre_archivo)
    get_plot(G)
