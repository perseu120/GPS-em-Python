import matplotlib.pyplot as plt
from queue import Queue
from collections import defaultdict
from vertex_mapa import Vertex
from haversine import haversine
import re
from matplotlib.widgets import Cursor, Button
from grafo_mapa import Graph

cont = 0
bolotax1,bolotay1 = 0,0
bolotax2,bolotay2 = 0,0
g = Graph()
g.pegaCoord() #adiciona todos os itens no grafo com id e as cordenadas
g.addArestas()

class Plot:
    
    fig, ax = plt.subplots()
    
    file_name = "lafaiete_map.osm.txt"
    x = list()
    y = list()
    with open(file_name) as fp:
        for line in fp:
            points = re.findall(r'[-+]?\d+.\d+', line)
            x.append(float(points[1]))
            y.append(float(points[2]))
        
    plt.plot(x, y, 'o')
        
    cursor = Cursor(ax, horizOn = True, vertOn = True, color = 'pink', linewidth = 0.5)

    
    

    def on_click(event):
        global cont
        global bolotax1,bolotay1
        global bolotax2,bolotay2
        global g
        if cont < 2:
            if cont == 0:
                bolotax1,bolotay1 = event.xdata, event.ydata
                
            if cont == 1:
                bolotax2,bolotay2 = event.xdata, event.ydata
                ver = g.getVertices()
                menor = 1000
                menor2 = 1000
                index = -1
                index1 = -1
        
                for i,v in enumerate(ver):
                    menor_valor2 = haversine((bolotax2,bolotay2), (v.lat,v.lon))
                    if menor2 > menor_valor2:
                        index1, menor2 = i, menor_valor2
        
                    menor_valor = haversine((bolotax1,bolotay1), (v.lat,v.lon))
                    if menor > menor_valor:
                        index, menor = i, menor_valor
        
                caminho = g.dijkstra(ver[index].id, ver[index1].id)
                
                x = []
                y = []    
                for i in caminho:
                    x = g.getVertex(i).lat
                    y = g.getVertex(i).lon

                    plt.plot(x,y, 'og--')
                    
                plt.title('Mapa de Lafaiete')
                
                plt.show()
                
                cont=0
        cont+=1
    fig.canvas.mpl_connect("button_press_event",on_click)
    plt.title('Mapa de Lafaiete')
    plt.show()
