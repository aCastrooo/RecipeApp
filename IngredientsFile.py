import sys
import re

def write_to_ing(ingList):
    file_name = open('Ing_List.txt', 'w')
    thestring = dataToFile(ingList)
    file_name.write(thestring)

def get_ing(ingList):
    file_name = open('Ing_List.txt', 'r')
    input_stream = file_name.readlines()
    for ing in input_stream:
        match_name = re.search(r'Ing:\s(\w+\s*\w*)\s', ing)
        match_quant = re.search(r'Quant:\s(\w+\s\w*)', ing)
        if match_name and match_quant:
            ingredient = match_name.group(1)
            quantity = match_quant.group(1)
            ingList[ingredient] = quantity

    file_name.close()
    return ingList

def delete_ing(ingList, ingredient):
    newList = {}
    localList = ingList
    for ings in localList:
        if ings != ingredient:
            newList[ings] = localList[ings]
    write_to_ing(newList)
    return newList

def dataToFile(ingList):
    end_string = ''
    for ingredients in ingList:
        end_string = end_string + 'Ing: ' + ingredients + ' Quant: ' + ingList[ingredients] + '\n'

    return end_string
