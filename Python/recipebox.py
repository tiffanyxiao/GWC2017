def main():
    # ingredients
    ingredients = ["peanut butter", "jelly", "2 slices of bread"]
    # instructions
    instructions = {1:"Place one slice of bread on a plate.",2:"Spread peanut butter on piece of bread",3:"Place other slice of bread on plate",4:"Spread jame on other piece of bread", 5:"Place other piece of bread on top of other bread"}
    #print out recipe
    print("RECIPE FOR PEANUT BUTTER JELLY SANDWICH:")
    print("----------------------------------------")
    print("Ingredients:")
    for i in range(len(ingredients)):
        if i == 2:
            print(ingredients[i])
        else:
            print(ingredients[i], end = ", ")
    print("----------------------------------------")
    print("Instructions:")
    for k in range(len(instructions)):
        k += 1
        print(str(k)+". "+instructions[k])

main()
