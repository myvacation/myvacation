#This is a madlibs generator just getting user input to make a funny sentence

print ("Hello, thanks for using the mad libs generator, hopefully you can have some fun " \
      "and get some laughs!")

def madlib(noun,verb1, verb2, adj1, adj2):
    print ("The {} was {} thru the forrest {} when a bear was {} {}.".format(noun,verb1,adj1,verb2,adj2))


game_on= input("would you like to play the game? Enter \"Y\" for yes and \"N\" for no  ")
while game_on== "Y":
    noun= input("Enter a noun ")
    verb1=input("Enter a verb ")
    verb2=input("Enter a verb ")
    adj1=input("Enter an adjective ")
    adj2=input("Enter an adjective ")
    madlib(noun,verb1,verb2,adj1,adj2)
    game_on = input("would you like to play the game? Enter \"Y\" for yes and \"N\" for no   ")

if game_on== "N":
    print("Thanks for checking out the game!")
