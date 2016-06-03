import sys
from LinkedListInit import LinkedList, Node


def write_to(savedRList):
    file_name = open("Recipe_List.txt", 'w')
    if savedRList == None:
        return
    else:
        thestring = savedRList.dataToFile()
        file_name.write(thestring)

def get_recipes():
    input_stream = ''
    file_name = open("Recipe_List.txt", 'r')
    input_stream = file_name.read()
    input_stream = input_stream.tokenize()

get_recipes()
