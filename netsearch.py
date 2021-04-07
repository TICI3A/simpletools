# -*- coding: utf-8 -*-

"""
Dado un fichero con una ip por línea, busca posibles coincidencias de pertenencia a la misma subred.
"""

import sys
from .repitedLines import read


def search_net(input_file, line:str, line_number:int):
    i = 0
    vbytes = line.rsplit('.')
    net_16 = vbytes[0] + "." + vbytes[1] + "."
    net_24 = net_16 + vbytes[2] + "."
    for other_line in read(input_file):
        if i != line_number and i > line_number:   
            if other_line.find(net_24) == 0:
                print("line ",line_number,":",net_24," in ",i,":",other_line)
            elif other_line.find(net_16) == 0:
                print("line ",line_number,":",net_16," in ",i,":",other_line)
        i+=1


if __name__== "__main__":
    if len(sys.argv) == 1:
        print("usage:")
        print("     ",sys.argv[0]," ","input_file")
        exit(85)

    input_file = sys.argv[1]
    i = 0
    for line in read(input_file):
        search_net(input_file, line, i)
        i+=1