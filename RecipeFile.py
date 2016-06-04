import sys
import re
import tokenize
from LinkedListInit import LinkedList, Node


def write_to(savedRList):
    file_name = open("Recipe_List.txt", 'w')
    if savedRList == None:
        return
    else:
        thestring = savedRList.dataToFile()
        file_name.write(thestring)

def get_recipes(savedRList):
    input_stream = ''
    file_name = open("Recipe_List.txt", 'r')
    input_stream = file_name.readlines()
    for find_recipes in input_stream:
        match_recipe = re.search(r'(\w+)\s(\d+)', find_recipes)
        match_name = match_recipe.group(1)
        match_time = match_recipe.group(2)
        insert_in_list(match_name, match_time, savedRList)

    return savedRList

def insert_in_list(theTitle, theTime, savedRList):
    curr = savedRList.front
    newNode = Node(theTitle, theTime, None)
    tempNode = Node(None, None, None)
    if savedRList.front == None:
        savedRList.front = newNode
    else:
        while curr.nextNode != None:
            curr = curr.nextNode
        curr.set_next(newNode)
