import unirest
import sys
from RecipeFile import write_to, get_recipes
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
            InputSearchRecipe()
        else:
            selectOptionRecipe()
    else:
        print '\n\n'
        print 'What would you like to do now?\n1) Search Again\n2) Go Back'
        whatnow = raw_input()
        if whatnow == '1':
            InputSearchRecipe()
        else:
            selectOptionRecipe()



def SearchViaIngredient():
    print 'this function is not implemented'

def selectOptionIng():
    print 'this function is not implemented'




'''Returns the list of saved recipes'''

def RecipeList():
    write_to(savedRList)
    print '\n\nYour Recipes:\n'
    if savedRList.front == None:
        print 'No saved recipes :(\nGo add some!'
        enter = raw_input()
        selectOptionRecipe()
    else:
        savedRList.printData()
        enter = raw_input()
        selectOptionRecipe()




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
