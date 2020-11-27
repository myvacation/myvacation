#This is a simple program where user inputs the number of dice and how many sides the dice have in order to
#to get randomized rolls of the dice

print ("Welcome to dice roller, you can enter the number of dice and the number of sides and you"
       "will be given the outcome of each die and the total of the roll, then a chance to start"
       "over and roll again or to choose a different amount of dice or sides of die")


def rolldie(dice,sides):
    import random
    total = 0
    dice_chosen=dice
    while dice_chosen >0:
        dice_chosen -=1
        roll = random.randint(1,sides)
        print (roll)
        total += roll
    print ("Your total roll is  " + str(total))
    print("Would you like to roll again with the same dice and sides?")
    again_or_not = input("Enter yes for  again and no to start over or q to quit   ")
    if again_or_not == "yes":
        rolldie(dice,sides)
    elif again_or_not == "no":
        dice = int(input("Please input the number of dice you want rolled   "))
        sides = int(input("Please input the number of sides you want the dice to have   "))
        rolldie(dice,sides)
    else:
        print ("Thanks for playing")

dice= int(input("Please input the number of dice you want rolled   "))
sides= int(input("Please input the number of sides you want the dice to have   "))

rolldie(dice,sides)


