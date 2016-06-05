import unirest
import sys
from RecipeFile import write_to_recipe, get_recipes
from IngredientsFile import write_to_ing, get_ing, delete_ing
from urllib2 import urlopen, URLError
from LinkedListInit import LinkedList, Node



###API KEY
the_api = 'cFrJEjM4VAmshZFucBaxzF9hZHRXp1Ci8QijsneXnvwuFmzRFb'

###Initialize the linked lists
rList = LinkedList(None)
savedRList = LinkedList(None)
ingList = {}




'''Takes the data from the generated list of recipes and organizes it
   into a linked list of recipes'''

def putInRList(theTitle, theTime):
    curr = rList.front
    newNode = Node(theTitle, theTime, None)
    tempNode = Node(None, None, None)
    if rList.front == None:
        rList.front = newNode
    else:
        while curr.nextNode != None:
            curr = curr.nextNode
        curr.set_next(newNode)




'''User inputs the ingredient they wish to save and the quantity of that ingredient'''

def AddIng():
    print '\nWhat ingredient would you like to add?'
    add = raw_input()
    print '\nHow much of the ingredient do you have?'
    quant = raw_input()
    ingList[add] = quant
    write_to_ing(ingList)
    print '\n' + add + ' was added with quantity: ' + quant + '\n'
    print 'Would you like to add another?\n(Y/N)'
    yorn = raw_input()
    if yorn == 'y' or yorn == 'Y':
        AddIng()
    elif yorn == 'n' or yorn == 'N':
        selectOptionIng()




'''User inputs the ingredient to be deleted, then it gets deleted'''

def deleteIng():
    global ingList
    print '\nWhich ingredient do you want to delete?'
    delete = raw_input()
    for ingredients in ingList:
        if delete == ingredients:
            ingList = delete_ing(ingList, delete)
            print '\n' + delete + ' has been deleted!'
            enter = raw_input()
            selectOptionIng()
    print '\nIngredient not found.'
    enter = raw_input()
    selectOptionIng()



'''Takes in user input to generate a list of ten recipes using the API
   Calls "putInRList()" to organize the data'''

def InputSearchRecipe():
    rList.front = None
    c = 1
    url = 'https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/search'
    api_key = the_api
    print('\n')
    input_query = raw_input('What recipe are you searching for? ')
    print('\n')
    query = input_query.replace(' ', '+')
    final_url = url + '?query='+ query
    response = unirest.get(final_url, headers={'X-Mashape-Key':api_key})
    for result in response.body['results']:
        print str(c) + ') ' + result['title'].encode('utf-8')
        print "Time to cook:", result['readyInMinutes'], "minutes\n"
        putInRList(result['title'], result['readyInMinutes'])
        c = c + 1
    pickfromRecipeMenu()




'''User decides which recipe they wish to save
   Returns success of the added recipe'''

def PickRecipe(num):
    newFront = rList.front
    count = int(num) - 1
    while count != 0:
        newFront = newFront.nextNode
        count = int(count) - 1

    print 'You want to save: ' + str(newFront.return_title()) + '?'
    print '(Type Y/N)'
    yorn = raw_input()
    print '\n'
    if yorn == 'Y' or yorn == 'y':
        savedRList.insert(newFront.title, newFront.time)
        print str(savedRList.front.return_title()) + ' has been saved!'
        print '\n\n'
        print 'What would you like to do now?\n1) Search Again\n2) Go Back'
        whatnow = raw_input()
        if whatnow == '1':
            write_to_recipe(savedRList)
            InputSearchRecipe()
        else:
            write_to_recipe(savedRList)
            selectOptionRecipe()
    else:
        print '\n\n'
        print 'What would you like to do now?\n1) Search Again\n2) Go Back'
        whatnow = raw_input()
        if whatnow == '1':
            write_to_recipe(savedRList)
            InputSearchRecipe()
        else:
            write_to_recipe(savedRList)
            selectOptionRecipe()



def SearchViaIngredient():
    print 'this function is not implemented'




'''Returns the list of saved recipes'''

def RecipeList():
    newsavedRList = get_recipes(savedRList)
    print '\n\nYour Recipes:\n'
    if newsavedRList.front == None:
        print 'No saved recipes :(\nGo add some!'
        enter = raw_input()
        selectOptionRecipe()
    else:
        newsavedRList.printData()
        enter = raw_input()
        selectOptionRecipe()




'''Returns the list of ingredients'''

def IngredientsList(ingList):
    ingList = get_ing(ingList)
    print '\nYour Ingredients:'
    if not ingList:
        print '\nYou have no ingredients :(\nYou can add some!'
        enter = raw_input()
        selectOptionIng()
    else:
        for ingredients in ingList:
            print '\nIngredient: ' + ingredients + '\nQuantity: ' + ingList[ingredients]
        enter = raw_input()
        selectOptionIng()





###
###The following functions print out the menus
###
'''Asks the user for input regarding if they wish to save a recipe or not'''

def pickfromRecipeMenu():
    print('\n')
    print('What would you like to do?')
    print('1) Save a recipe\n2) Go Back')
    pick = raw_input()
    if pick == '1':
        print('\n')
        print('Which recipe would you like to save?\n(You must select the cooresponding number)')
        recipePick = raw_input()
        print '\n'
        PickRecipe(recipePick)
    if pick == '2':
        selectOptionRecipe()




def printLines():
    n = 0
    while n < 2:
        print('--------------------------------------------------------------')
        n = n + 1




'''Prints the ingredients menu'''
def selectOptionIng():
    n = 0
    while n < 26:
        print('\n')
        n += 1
    printLines()
    print('INGREDIENTS')
    printLines()
    print('1) View Your Ingredients\n2) Add An Ingredient\n3) Delete An Ingredient\n4) Go Back')
    ioption = raw_input()
    if ioption == '1':
        IngredientsList(ingList)
    if ioption == '2':
        AddIng()
    if ioption == '3':
        deleteIng()
    if ioption == '4':
        selectOptionMain()




'''Prints the main recipe menu'''

def selectOptionRecipe():
    n = 0
    while n < 26:
        print('\n')
        n += 1
    printLines()
    print('RECIPES')
    printLines()
    print('1) View Saved Recipes\n2) Search New Recipes\n3) Search Via Saved Ingredients\n4) Go Back')
    roption = raw_input()
    if roption == '1':
        RecipeList()
    if roption == '2':
        InputSearchRecipe()
    if roption == '3':
        SearchViaIngredient()
    if roption == '4':
        selectOptionMain()




'''Prints the main menu'''

def selectOptionMain():
    n = 0
    while n < 26:
        print('\n')
        n += 1
    printLines()
    print('MAIN MENU')
    printLines()
    print('1) View Ingredients\n2) View Recipes\n3) Quit')
    option = raw_input()
    if option == '1':
        selectOptionIng()
    if option == '2':
        selectOptionRecipe()
    if option == '3':
        print('\n')
        print('\n')
        print('\n')
        print('Thanks for using "app name"!')
        sys.exit(0)



selectOptionMain()
###InputSearchRecipe()
