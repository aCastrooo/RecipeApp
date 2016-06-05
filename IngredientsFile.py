import sys
import re

def write_to_ing(key, quantity):
    file_name = open('Ing_List.txt', 'w')
    file_name.write('Ing: ' + key + ' Quant: ' + quantity + '\n')

def get_ing(ingList):
    file_name = open('Ing_List.txt', 'r')
    input_stream = file_name.readlines()
    for ing in input_stream:
        match_name = re.search(r'Ing:\s(\w+)\s', ing)
        match_quant = re.search(r'Quant:\s(\w+\s\w*)', ing)
        if match_name and match_quant:
            ingredient = match_name.group(1)
            quantity = match_quant.group(1)
            ingList[ingredient] = quantity

    file_name.close()
    return ingList
