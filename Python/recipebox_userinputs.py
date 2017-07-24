class Recipe:
    ''' A recipe class'''

    def __init__(self, name, ingredients, instructions):
        '''function to establish recipe'''
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

def printRecipe(recipe):
    print("Recipe for: "+recipe.name+" :")
    print("Ingredients: ", end = "")
    for ingredient in recipe.ingredients:
        print(ingredient, end =", ")
    print()
    for instruction in recipe.instructions:
        print(str(instruction)+". "+recipe.instructions[instruction])
    print("-----------------------------")

def main():
    ''' function to print recipe'''
    pb_recipe = Recipe("Peanut Butter Jelly Sandwich", ["peanut butter", "jelly", "2 slices of bread"],{1:"Place one slice of bread on a plate.",2:"Spread peanut butter on piece of bread",3:"Place other slice of bread on plate",4:"Spread jame on other piece of bread", 5:"Place other piece of bread on top of other bread"} )
    ch_recipe = Recipe("Grilled Cheese Sandwich", ["2 slices of bread", "1 slice cheddar cheese", "1.5 tablespoons butter"], {1:"Preheat skillet over medium heat",2:"Place slice of bread on skillet",3:"Place cheese on skillet",4:"Place other slice of bread on skillet",5:"Grill until cheese is melted"})
    he_recipe = Recipe("Ham and Egg Sandwich", ["2 slices of bread", "1 slice of ham", "1 egg"], {1:"Place one slice on plate", 2:"Place ham on bread", 3:"Cook egg",4:"Place egg on bread",5:"Place bread on top"})

    #create list holding all recipes
    recipes = [pb_recipe, ch_recipe, he_recipe]

    rInput = input("What recipe would you like? ")

    #create variable to keep track if recipe is found
    found = False 

    for recipe in recipes:
        if rInput == recipe.name:
            printRecipe(recipe)
            found = True

    if found == False:
        response = input("Recipe not found. Would you like to create a new one? ")
        if response == "yes":
            ingredients = input("Please list the ingredients (separated by commas): ").split(",")
            num_instructions = eval(input("Please enter the number of instructions."))
            entered_instructions = input("Now input instructions in order separated by commas: ").split(",")
            instructions = {}
            for i in range(num_instructions):
                k=+1
                instructions[k] = entered_instructions[ientered_instructions]
            new_recipe = Recipe(rInput, ingredients, instructions)
            printRecipe(new_recipe)
            
main()
