class Grafo:

    def __init__ (self, n):
        """
        Crea un Grafo vacio con numVertices.
        """
        
        # El numero de vertices que contiene el Grafo
        self.__n = n
        
        # La matriz de ponderaciones
        self.__costo = [[float("inf") for i in range(n)] for j in range(n)]
        for v in range(n):
            self.__costo[v][v] = 0
        
        # El número de arcos que contiene el Grafo
        self.__arcos = 0



    def __nodoValido(self, nodo):
        """
        Verifica que nodo es válido.
        """
        
        valido = False
        if nodo >= 1 and nodo <= self.__n:
            valido = True
        return valido



    def agregarArco(self, origen, destino, costo):
        """
        Agrega un arco que va del vértice origen al vertice
        destino con un costo.
        
        Regresa True si el arco se pudo agregar y False en caso contrario.
        """
        
        valido = False
        if self.__nodoValido(origen) and self.__nodoValido(destino) \
                and origen != destino and costo >= 0:
                
            # Si no existe el arco (origen,destino), se incrementa
            # la cuenta de arcos
            if self.__costo[origen-1][destino-1] == float("inf"):
                self.__arcos += 1
                
            # Si el costo que se quiere asignar es inf, se decrementa
            # el numero de arcos
            if costo == float("inf"):
                self.__arcos -= 1

            self.__costo[origen-1][destino-1] = costo
            valido = True
        return valido



    def costo(self, origen, destino):
        """
        Devuelve el costo del arco que va del vertice origen al vertice destino.
        """
        
        costo = -1
        if self.__nodoValido(origen) and self.__nodoValido(destino):
            costo = self.__costo[origen-1][destino-1]
        return costo



    def arcos(self):
        """
        Devuelve el número de arcos contenidos en el Grafo.
        """
        
        return self.__arcos



    def vertices(self):
        """
        Devuelve el número de vértices contenidos en el Grafo.
        """

        return self.__n



    def aCadena(self):
        """
        Devuelve un String con el conjunto de vértices y el conjunto de arcos
        que forman el Grafo.
        """
        
        vertices = "V = {"
        arcos = "A = {"
        for i in range(self.__n):
            vertices += str(i+1)
            for j in range(self.__n):
                if ((i != j) and (self.__costo[i][j] < float("inf"))):
                    arcos += "(" + str(i+1) + "," + str(j+1) + "):" + str(self.__costo[i][j]) + ", "
            if i < self.__n:
                vertices += ", "
        vertices = vertices[:len(vertices)-2] + "}"
        arcos = arcos[:len(arcos)-2] + "}"
        return vertices + "\n" + arcos
