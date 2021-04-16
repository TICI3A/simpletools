# -*- coding: utf-8 -*-

"""
Dado un fichero con una ip por línea, busca posibles coincidencias de pertenencia a la misma subred.
"""

import sys
from repitedLines import read


def search_net(input_file, line:str, line_number:int):
    lista_16 = []
    lista_24 = []
    i = 0
    vbytes = line.rsplit('.')
    net_16 = vbytes[0] + "." + vbytes[1] + "."
    net_24 = net_16 + vbytes[2] + "."
    for other_line in read(input_file):
        if i != line_number and i > line_number:   
            if other_line.find(net_16) == 0:
                if other_line.find('/') != -1 : 
                    #si ya está la subred borramos y salimos
                    lista_16 = []
                    lista_24 = []
                    break
                lista_16.append(other_line)
                
                
            elif other_line.find(net_24) == 0:
                if other_line.find('/') != -1 :  
                    #si ya está la subred borramos y salimos
                    lista_16 = []
                    lista_24 = []
                    break
                lista_24.append(other_line)

                
        i+=1
    if len(lista_24) > 0: 
        lista_24.append(line) # añadimos la ip original
        #print("line",line_number,":",net_24+"0/24 in ",i,":",lista_24)
        print(net_24+"0/24")
    if len(lista_16) > 0:
        lista_16.append(line)
        print(net_16+"0.0/16")
        #print("line",line_number,":",net_16+"0.0/16 in ",i,":",lista_16)


if __name__== "__main__":
    if len(sys.argv) == 1:
        print("usage:")
        print("     ","python"," ", sys.argv[0]," ","input_file")
        exit(85)

    input_file = sys.argv[1]
    i = 0
    for line in read(input_file):  
        if line.find('/') == -1:    
            search_net(input_file, line, i)
        i+=1