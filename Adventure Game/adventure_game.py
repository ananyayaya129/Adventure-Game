import time
import random


def print_pause(line):
    print(line)
    time.sleep(2)


def intro(option):
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause("Rumour has it that a " + option +
                " is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.")


def house(option):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens "
                "and out steps a " + option + ".")
    print_pause("Eep! This is the " + option + "'s house!")
    print_pause("Then the " + option + " attacks you!")
    print_pause("You feel a bit under-prepared for this, "
                "what with only having a tiny dagger.")


def cave(items):
    if "sword" in items:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, "
                    "and gotten all the good stuff. "
                    "It's just an empty cave now.")
        print_pause("You walk back out to the field.\n")
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger "
                    "and take the sword with you.")
        print_pause("You walk back out to the field.")
        items.append("sword")


def fight(items, option):
    if "sword" in items:
        print_pause("As the " + option + " moves to attack, "
                    "you unsheath your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand "
                    "as you brace yourself for the attack.")
        print_pause("But the " + option +
                    " takes one look at your shiny new toy "
                    "and runs away!")
        print_pause("You have rid the town of the " + option +
                    ". You are victorious!")
        print_pause("YOU WON!")
        play_again()
    else:
        print_pause("You do your best...")
        print_pause("but your dagger is no match for the " + option + ".")
        print_pause("You have been defeated!")
        print_pause("YOU LOSE!")
        play_again()


def runaway():
    print_pause("You run back into the field. Luckily, "
                "you don't seem to have been followed.")


def play_again():
    while True:
        response3 = input("Would you like to play again? (y/n)\n")
        if response3 == "y":
            print_pause("Excellent restarting the game...")
            adventure_game()
        elif response3 == "n":
            print_pause("Thanks for playing! See you next time.")
            exit()


def play_game(items, option):
    while True:
        print_pause("\nEnter 1 to knock on the door of the house.")
        print_pause("Enter 2 to peer into the cave.")
        response = input("What would you like to do?\n"
                         "(Please enter 1 or 2.)\n")
        if response == "1":
            house(option)
            while True:
                response2 = input("Would you like to\n"
                                  "(1) fight or\n(2) run away?\n")
                if response2 == "1":
                    fight(items, option)
                    break
                elif response2 == "2":
                    runaway()
                    break
        elif response == "2":
            cave(items)


def adventure_game():
    items = []
    option = random.choice(['dragon', 'wicked fairie', 'pirate',
                            'troll', 'gorgon', 'devil', 'vampire', 'demon'])
    intro(option)
    play_game(items, option)


adventure_game()
