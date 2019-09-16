import random

import pickle

import os

import sys
 
from decimal import Decimal
 

class saved_game():

    def __init__(user, name):

        user.tie = 0

        user.playerWon = 0

        user.botwon = 0

        user.name = name

 

    def get_round(user):

        return user.tie + user.playerWon + user.botwon 


def main():

    print ("Welcome to Rock, Paper, Scissors!")

    print  ("")

    stat_save = menu()

    while True:

        play(stat_save)

        menu2(stat_save)

 

def menu():

    while True:

        print ("1: Start New Game")

        print ("2: Load Game")

        print ("3: Quit")

        print ("")

        menuchoice = input("Enter choice: ")

 

        if menuchoice == "1":

            global name

            name = input("What is your name?: ")

            print ("Hello %s. Let's play!" % name)

            with open("%s.rps" % name, 'wb') as f:

                pickle.dump(saved_game, f)

                f.close()

            stat_save = saved_game(name)

        elif menuchoice == "2":

            while True:

                name = input("What is your name?: ")


                try:
                    save = open('%s.rps' % name, 'rb')

                    print ("Welcome back %s. Let's play!" % name)


                    stat_save = pickle.load(save)

                    return stat_save

                except IOError:

                    print ("%s, your game could not be found." % name)

                    continue

                break

                
        elif menuchoice == "3":

            exit()

            return
        else:

            print ("The number you typed is invalid.")

            continue

        return stat_save


def play(stat_save):

    playerChoice = int(playerMenu())

    bot = bot_random()

    outcome = determine(playerChoice, bot)

    statupdate(outcome, stat_save)


def playerMenu():

    print ("\n1: Rock \n2: Paper \n3: Scissors\n")

    menuchoice = input("What will it be? ")

    while not menu_true(menuchoice):

        invalidChoice(menuchoice)

        menuchoice = input("Enter a correct value: ")

    return menuchoice

 

 

def menu_true(menuchoice):

    if menuchoice == "1":

        return True
    if menuchoice == "2":

        return True
    if menuchoice == "3":

        return True

    else:

        return False

 

 

def bot_random():

    bot = random.randint(1,3)

    return bot


def determine(playerChoice, bot):

    rps = ['Rock', 'Paper', 'Scissors']

    win_status = (playerChoice - bot % 3)

    print ("You chose %s." % rps[playerChoice - 1])

    feedback = ("The computer chose %s." % rps[bot - 1])

    if win_status == 0:

        feedback += (" You tie!")

    elif win_status == 1:

        feedback += (" You win!")

    else:

        feedback += (" You lose!")

    print (feedback)

    return win_status



def statupdate(outcome, stat_save):

    if outcome == 0:

        stat_save.tie += 1

    elif outcome == 1:

        stat_save.playerWon += 1

    else:

        stat_save.botwon += 1


def invalidChoice(menuchoice):

    print ("Invalid Choice.")


def stat_screen(stat_save):

    print ("")

    print ("%s, here are your game play statistics..." % name)

    print ("Wins: %d" % stat_save.playerWon)

    print ("Losses: %d" % stat_save.botwon)

    print ("Ties: %d" % stat_save.tie)

    print ("Rounds: %d" % stat_save.get_round())

    if stat_save.botwon > 0:

        x = Decimal(stat_save.playerWon / stat_save.botwon)
        output = round(x,2)
        print ("Win/Loss Ratio", output)

    else:

        print ("Win/Loss Ratio: Only Wins")
        
    


 

def menu2(stat_save):

    print ("")

    print ("1: Play again")

    print ("2: Show Statistics")

    print ("3: Quit")

    print ("")

    while True:

        menuchoice = input("Enter choice: ")

        if menuchoice == "1":

            break
        if menuchoice == "2":

            break
        if menuchoice == "3":

            break

        else:

            print ("The number you typed is invalid.")

 

    if menuchoice == "2":

        stat_screen(stat_save)

        menu2(stat_save)


    elif menuchoice == "3":

        save = open("%s.rps" % name, 'wb')

        pickle.dump(stat_save, save)

        save.close()

        print(" %s, your game is saved successfully." % name)

        exit()

main()
