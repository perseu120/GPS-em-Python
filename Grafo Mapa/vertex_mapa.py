class Vertex:
    def __init__(self, chave, lat, lon):#as bolinha do grafo
        self.id = chave
        self.lat = lat
        self.lon = lon
        self.conexao = {}

    def addVizinho(self, vizinho, peso=0):#adiciona o visinho e o peso do vertice se nao coloca peso ele já vai com default por padrão
        self.conexao[vizinho] = peso

    def getConexao(self):
        return self.conexao.keys()#vai retorna todas as chaves das bolinhas

    def getId(self):# retorna o nome da bolinha
        return self.id

    def getPeso(self,vizinho):#retorna o peso do vizinho 
        return self.conexao[vizinho]

    def getLat(self, lat):
        return self.lat

    def getLon(self, lon):
        return self.lon
