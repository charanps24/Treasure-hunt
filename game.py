print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a cross road where do you want to go? '
                'Type "left" or "right".\n').lower()
if choice1 == "left":
    choice2 = input('You\'ve come to this lake. there is an island.'
                'Type "wait" to wait for the boat or type "swim" to '
                'swim across\n').lower()
    if choice2 == "wait":
        choice3 = input("You have arrived at the island unharmed. "
              "There are house with 3 doors, which door you want to "
                        "choose 'red', 'yellow, 'blue'\n").lower()#game will continue
        if choice3 == "red":
            print("It's room full of fire, sorry game over.")
        elif choice3 == "yellow":
            print("You found the treasure you won!")
        elif choice3 == "blue":
            print("The room had Beasts, Game Over")
        else:
            print("You choose a door which does not exist")

    else:
        print("You got attacked by an angry trout. Game over")




# if choice1 == "Go" or choice1== "go":
#     print(input('Good Job, passed, Want to sail through '
#                 'the River? Type "Yes" or "No" ?'))

#

# else:
#     print("wrong input")
# print("Want to sail through the River?")
# river = input(' Type "Yes" or "No" ?')
# if river == "Yes":
#     if cave == "Go":
#      print("Good Job you have sailed through!")
# elif river == "No":
#     print("Game Over")
# print("Get out of this island to win this game?")
# airplane = input('Fly through airplane type "Yes" or type "No"')
# if airplane == "Yes":
#     if river == "Yes":
#      if cave == "Go":
#print("Congratulations you won the game! Bravo")
