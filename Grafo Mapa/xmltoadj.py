from gistfile1 import *

G = read_osm("lafaiete_map.osm.xml")
networkx.write_adjlist(G, "LAFA.adjlist")

