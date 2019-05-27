#Enter ingredients to get a list of links to recipes with those ingredients. 
#Enter 'Surprise me' to get the top ranked recipes

import requests
import json
import sys

#set up function

def get_recipe(argv):
    #ingredients = sys.argv
    #print("Test 'get_recipe())'")
    if argv[1].lower() == "surprise me":
        ingredients = ""
    else:
        inputs = argv
        inputs.pop(0)
        ingredients = ','.join(str(x) for x in inputs)
    
    #for testing
    #recipe = ingredients
    
    #build url:
    recipe_url = "https://www.food2fork.com/api/search?key=8129aaa609bb65d948303c37013647f9&q=" + ingredients
    #check the url
    #print(recipe_url)
    
    #send the request:
    recipe_request = requests.get(recipe_url)

    #put the output to text to read
    recipe=recipe_request.text 

    return recipe,ingredients
    
def instructions():
    print("Enter an ingredient or multiple ingredients you want the recipe to include. ") 
    print("If you want a list of the top rated recipes, enter SUPRISE ME. ")

#main program
 
while True:    
    if len(sys.argv) < 2:
        #print("Enter at least one ingredient to get a recipe or 'surprise' for a top trending recipe.")
        instructions()
        break
    #elif ingredients_input.lower() == "surprise me":
    elif sys.argv[1] == "surprise me":
        #print("test 'surprise'.")
        recipe = get_recipe(sys.argv)
        with open ("top_recipes", "w") as recipe_out:
            json.dump(recipe, recipe_out)
        break
    else:
        recipe, ingredients = get_recipe(sys.argv)
        #print(recipe)
        with open ("recipe_"+ingredients, "w") as recipe_out:
            json.dump(recipe, recipe_out)
        break
