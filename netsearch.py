# -*- coding: utf-8 -*-

"""
Dado un fichero con una ip por línea, busca posibles coincidencias de pertenencia a la misma subred.
"""

import sys
from repitedLines import read



def search_net(input_file, line:str, line_number:int,passed_net:str):
    lista_16 = []
    lista_24 = []
    i = 0
    vbytes = line.rsplit('.')
    net_16 = vbytes[0] + "." + vbytes[1] + "."
    net_24 = net_16 + vbytes[2] + "."
    if passed_net.find(net_16) == -1 and passed_net.find(net_24) == -1:
        #if line.find("159.203") != -1:
        #    print(net_16, " ", net_24, " ", line, " - ")       
        #print(passed_net)
        for other_line in read(input_file):
            if i != line_number and i > line_number:   
                if other_line.find(net_16) == 0:
                    lista_16.append(other_line)
                    #print(other_line, " ", lista_16)
                    
                elif other_line.find(net_24) == 0:
                    lista_24.append(other_line)
            i+=1
    
        if len(lista_24) > 0: 
            lista_24.append(line) # añadimos la ip original
            #print("line",line_number,":",net_24+"0/24 in ",i,":",lista_24)
            print(net_24+"0/24")
        if len(lista_16) > 0:
            lista_16.append(line)
            print(net_16+"0.0/16")
            ##print("line",line_number,":",net_16+"0.0/16 in ",i,":",lista_16)
    passed_net = passed_net + net_24+"0/24\n"+net_16+"0.0/16\n"
    #if line.find("159.203") != -1:
    #    print("----",passed_net,"----")
    return passed_net

if __name__== "__main__":
    if len(sys.argv) == 1:
        print("usage:")
        print("     ","python"," ", sys.argv[0]," ","input_file")
        exit(85)
    passed_net = ""
    input_file = sys.argv[1]
    i = 0
    passed_lines = ""
    for line in read(input_file):  
        if line.find('/') != -1:
            passed_net+=line
        elif passed_lines.find(line) == -1:    
            passed_net = search_net(input_file, line, i,passed_net)
            passed_lines+=line
        i+=1