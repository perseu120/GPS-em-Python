import xml.etree.ElementTree as ET
import sys

file_name = "lafaiete_map.osm.xml"

tree = ET.parse(file_name)

root = tree.getroot()

f=open("lafaiete_map.osm.txt", "w")
for node in root.iter('node'):
    ident = node.attrib['id']
    lat = node.attrib['lat']
    lon = node.attrib['lon']
    f.write("{} {} {}\n".format(ident,lat,lon))
f.close()



