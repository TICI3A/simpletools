# -*- coding: utf-8 -*-

import sys



def read(file_route:str):
    return open(file_route, encoding="utf-8")
     


def search_match(input_file, line:str, line_number:int):
    i = 0
    for other_line in read(input_file):
        if other_line == line and i != line_number and i > line_number:
            print("line ",line_number,":",line," == ",i,":",other_line)
        i+=1


if __name__== "__main__":
    if len(sys.argv) == 1:
        print("usage:")
        print("     ",sys.argv[0]," ","input_file")
        exit(85)

    input_file = sys.argv[1]
    i = 0
    for line in read(input_file):
        search_match(input_file, line, i)
        i+=1
