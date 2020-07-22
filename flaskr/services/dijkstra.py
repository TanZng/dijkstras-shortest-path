from services.grafo import Grafo

def dijkstra(G, u, v):
    '''
    Recibe una gráfica G y dos vértices u y v de G, que encuentra el camino más corto desde u hasta v
    utilizando el algoritmo de Dijkstra. Esta función devuelve, un arreglo, con los pares de nodos
    para formar el camino más corto desde u hasta v y su costo: [(nodo0, nodo1), (nodo1, nodo2), ..., costo]
    Si es imposible llegar de u a v, regresa None
    '''
    distancias =  [float("inf")] * (G.vertices())  # Pone todas las distancias en None
    previos =   [None] * (G.vertices()) # El vertice anterior de todos en None
    Q = [ [float("inf"),i] for i in range(G.vertices())] # Cola con todos los vertices con formato: [distancia, vertice]

    Q[u-1][0] = 0 # En Q, ponemos la distancia del vertice u en 0: [0, u]
    distancias[u-1] = 0 # Ponemos la distancia del vertice u en 0

    while Q: # mientras haya elementos en Q

        smallest = min(Q)       # Sacamos de Q el vertice con menor distancia
        Q.remove(smallest)      # Eliminar el vertice con menor distancia de la cola
        smallest = smallest[1]  # Obtenemos el vertice

        # Si el nodo smalles es el destino, hemos terminado, se regresa la ruta
        if smallest == v-1:
            path = []
            path.append( distancias[smallest] )
            while previos[smallest] is not None:   # Se detiene hasta que llega al nodo que no tiene predecesor
                path.append( ( previos[smallest] + 1, smallest+1 ) )
                smallest = previos[smallest]
            path.reverse()
            return path

        # Todos los vértices restantes son inaccesibles desde u
        if distancias[smallest] == float("inf"):
            break

        # Analizamos los vertices adyacentes a smallest
        for adyacente in range(G.vertices()):  # Mire todos los nodos a los que esta unido small
            if 0 < G.costo(smallest + 1, adyacente + 1) < float("inf"):
                alt = distancias[smallest] + G.costo(smallest + 1, adyacente + 1)
                # Si hay un camino más cortos,
                # se actualiza  distancias, previos y Q
                if alt < distancias[adyacente]:
                    distancias[adyacente] = alt
                    previos[adyacente] = smallest
                    # Actualiza la distancia en Q: [distancia, vertice]
                    for n in Q:
                        if n[1] == adyacente:
                            n[0] = alt
                            break
    return [None]

def leerGrafo(nombre_archivo):
    '''
    lee del archivo de texto nombre_archivo, que es la información de un grafo
    y devuelve el objeto correspondiente
    '''
    f = open(nombre_archivo, "r")

    x = f.readline()
    x = int(x)
    g = Grafo(x)

    x = f.readline()

    while x != "":
        y = x.split()
        origen = int(y[0])
        destino = int(y[1])
        costo = float(y[2])
        # Asigna los valores al grafo
        g.agregarArco(origen, destino, costo)
        x = f.readline()

    f.close()
    return g

def get_short_path(archivo, u, v):
    '''
    Recibe el nombre del archivo donde se encuentra el grafo a analizar.
    Recibe el nodo u de donde partir y el nodo v al que llegar.
    '''
    valores = [u,v]
    g = leerGrafo(archivo)
    x = None

    if 0 < u <= g.vertices() and 0 < v <= g.vertices(): 
        # valores contiene un arreglo: [origen, destino]
        #print("Recorrido más corto desde {} hasta {}:".format(valores[0], valores[1]))
        x = dijkstra(g, valores[0], valores[1])
        #print(type(x))
        #print(dijkstra(g, valores[0], valores[1]))
        #print("\n")
    return x
