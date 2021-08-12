from queue import Queue
from collections import defaultdict
from vertex_mapa import Vertex
from haversine import haversine
import re 


class Graph:
    def __init__(self):
        self.vertList = {}#cria o dicionario para por os vertices

    def addVertex(self, ID, lat, lon):
        newVertex = Vertex(ID, lat, lon) #cria o vertice
        self.vertList[ID] = newVertex  #adiciono as coisas dentro do vertice        
        return newVertex
        
    def getVertex(self, key):#retorna o que tem dentro do vertex  
        return self.vertList[key]
        #tem que ter as cordenadas 
    
    def addArestas(self):#adiciona a aresta e o peso
        arquivo = open('LAFA.adjlist', 'r')
        
        for line in arquivo:
            line = line.replace('\n', '')
            adjList = line.split(" ")
                #adj = re.findall(r'[-+]?\d+.\d+', line) 
            de = adjList[0]
            
            for i in range(1, len(adjList)):                    
                para = adjList[i]          
                self.vertList[de].addVizinho(self.vertList[para], self.getHaversine(de, para))        
            
                    
        arquivo.close()
        #Pega uma bolinha e faz a ligação com outra bolinha vizinha e coloca o peso da ligação
        
        
    def getHaversine(self,de,para):
        vertice1 = self.getVertex(de)    
        vertice2 = self.getVertex(para)
        return haversine((vertice1.lat,vertice1.lon),(vertice2.lat,vertice2.lon))
    #Calcula a distância entre dois vertices usando lat e lon
    
          
        
    def getVertices(self):
        return list(self.vertList.values())#vai retorna o valor das posicoes do dicionario, esse metodo é da classe dicionario
        
    def getArestas(self):
        aresta = set()
        for nome, vertice in self.vertList.items():
            for j in vertice.conexao: #essa função ta dando erro
                aresta.add((nome, j.id, vertice.getPeso(j)))
        return list(aresta)
    

        
    #def bfs(self, start):

    #def dfs(self, start): #busca em progundidade, usar pilha
        

    def dijkstra(self, start, end): 
        info = {}
        naoVisitados = []
        predecessor = {}
        path = []
        infinito = 1e309
        info[start] = 0
        for key in self.vertList.keys(): # Inicializa todos como não visitados
            if key != start:
                info[key] = infinito
            naoVisitados.append(key)
        iteracao = 0
        while naoVisitados:
            if iteracao == 0:
                vertice = start
                iteracao = 1
            else:
                vertice = None
            for node in naoVisitados:
                if vertice is None:
                    vertice = node
                elif info[node] < info[vertice]:
                        vertice = node
            for neighbor in self.vertList[vertice].getConexao():    
                nbr = neighbor.id
                cost = self.vertList[vertice].conexao.get(neighbor)
                total = info[vertice] + cost
                if total < info[nbr]:
                    predecessor[nbr] = vertice
                    info[nbr] = total
            naoVisitados.remove(vertice)
            node = end
            while node != start:
                try:        
                    path.insert(0, node)        
                    node = predecessor[node]        
                except KeyError:        
                    print("erro")        
                    break
            path.insert(0, start)
            if info[end] != infinito:
                print("Menor Caminho encontrado: " + str(info[end]) + "m")
                return path
    
    
    def lerArquivo(self):     #Separa cada linha do arquivo
        
        arquivo = open('lafaiete_map.osm.txt', 'r')
        
        listaPontos = arquivo.readlines()
        
        #print(listaPontos)
                
        arquivo.close()
        
        return listaPontos
        


    def pegaCoord(self):           #Quebra cada linha em 3 e chama o addVertex
        
        for line in self.lerArquivo():
            ponto = re.findall(r'[-+]?\d+.\d+', line)
    
            ID = ponto[0]
            lat = float(ponto[1])
            lon = float(ponto[2])
            
            self.addVertex(ID, lat, lon)

            

#if __name__ == "__main__":

 #   g = Graph() #cria o dicionario que vai ser o grafo
    
  #  g.pegaCoord() #adiciona todos os itens no grafo com id e as cordenadas

  #  g.addArestas()
    
   # todas = g.getVertices()
    
  
    

    #grafo.dijkstra(todas[1].id, todas[0].id)

    
