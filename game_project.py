import time
import random


def print_pause(string):
    print(string)
    time.sleep(1)


def intro():

    def Intro1():
        print_pause("You seem a little distraught."
                    " U rlly don't like this monster,")
        print_pause(" he doesn't like humans and"
                    " he entrapped them all into a portal")
        print_pause("You may be the chosen one that saves humankind. "
                    "Let's see if you have what it takes. 😈 😈")
        print_pause("Let's go, comrade! "
                    "You can see a weird static in the air ")
        print_pause("100 yards away from you and recognize "
                    "it as THE portal. You also see the cyclops")
        print_pause("near it laughing at you not even "
                    "taking you seriously 😆 😅.")

    def Intro2():
        print_pause("In an apocalyptic world where"
                    " you're the last person to exist, ")
        print_pause("you find out that the only way to "
                    "retreive humankind is to defeat the")
        print_pause("cyclops, for only the cyclops has "
                    "access to the portal in which all")
        print_pause("of humankind is trapped. "
                    "Let's see if you have what it takes. 😈 😈")
        print_pause("You can see a weird static in the air "
                    "100 yards away from you and recognize")
        print_pause("it as THE portal. You also see the cyclops "
                    "near it laughing at you not even")
        print_pause("taking you seriously 😆 😅.")

    differentChoices = [Intro1, Intro2]
    for i in range(1):
        random.choice(differentChoices)()


def monster_approach(abilities, quests):
    if "divinity" in abilities:
        print_pause("The monster sees you and looks strangely")
        print_pause("intimidated by your unusually powerful aura.")
        if "experienced fighting" in abilities:
            choice = input("Will you charge and attack?(1) "
                           "Or run like a coward?(2)")
            if choice == '1':
                print_pause("Your years of experience and "
                            "harnessing your energy properly "
                            "leads you to a victory.")
                print_pause("You defeat the no-good cyclops "
                            "and he hands you over the keys to "
                            "the portal machine")
                print_pause("Humankind restores. And now, a new problem "
                            "arises What do we do with these billions "
                            "of humans.")
                print_pause("You won. 'Til next time!")
                while True:
                    play_again = input("Would you like to play again?yes(1) "
                                       "or no(2)")
                    if play_again == "1":
                        print_pause("Awesome! Let's go!")
                        play_game()
                    elif play_again == "2":
                        print_pause("Aight... Peace!")
                        quests.append("Exit-game")
                        break
                    else:
                        print_pause("sorry, I don't understand")

            if choice == '2':
                def get_lucky():
                    print_pause("You walk away without an issue... "
                                "I guess, even in the face of immentent "
                                "victory, we see who's born a winner "
                                "and who's not.")
                    take_initiative(abilities, quests)

                def monster_runs_after_you():
                    print_pause("Heck! The monster chases after you "
                                "and eats you.")
                    print_pause("This leads you to your own demise and "
                                "you... lose")
                    while True:
                        play_again = input("Would you like to play again? "
                                           "yes(1) or no(2)")
                        if play_again == "1":
                            print_pause("Awesome! Let's go!")
                            play_game()
                        elif play_again == "2":
                            print_pause("Aight... Peace!")
                            quests.append("Exit-game")
                            break
                chances = [get_lucky, monster_runs_after_you]
                for i in range(1):
                    random.choice(chances)()

        else:
            print_pause("You're way too inexperienced and haven't "
                        "trained to control your newfound abilities.")
            while True:
                charge_anyways = input("continue charging at the evil monster "
                                       "anyways? yes(1) or no(2)?")
                if charge_anyways == '1':
                    print_pause("You lost and were defeated! Haha")
                    while True:
                        play_again = input("Would you like to play again? "
                                           "yes(1) or no(2)")
                        if play_again == "1":
                            print_pause("Awesome! Let's go!")
                            play_game()
                        elif play_again == "2":
                            print_pause("Aight... Peace!")
                            quests.append("Exit-game")
                            break
                    break
                elif charge_anyways == '2':
                    print_pause("You assess the potential risks and decide "
                                "to run away.")
                    quests.append("after_running_away")
                    break
                else:
                    print_pause("sorry, I don't understand")

    else:
        print_pause("You approach the monster as he looks at you like")
        print_pause("you're insane, laughing at you")
        print_pause("and as you get closer, he realizes he's a little "
                    "hungry and...")
        print_pause("eats you. 'That's some good protein! Just like mama"
                    " made it.'")
        print_pause("...")
        print_pause("you lost")
        while True:
            play_again = input("Would you like to play again?yes(1) or no(2)")
            if play_again == "1":
                print_pause("Awesome! Let's go!")
                play_game()
            elif play_again == "2":
                print_pause("Aight... Peace!")
                quests.append("Exit-game")
                break
            else:
                print_pause("sorry, I don't understand")


def forest(abilities, quests):
    if "divinity" in abilities:
        print_pause("The spirits are guiding you out of this forest,"
                    " telling you that")
        print_pause("you've fulfilled your purpose here.")
    else:
        print_pause("Woah! You're in the forest and see a huge light.")
        print_pause("You approach it and have visions and prophecies that "
                    "YOU are humanity's last hope.")
        print_pause("The spirits have granted you insane, divine powers "
                    "and you feel ready to do what")
        print_pause("needs to be done.")
        abilities.append("divinity")
        quests.append("after-acheiving-divinity")
        take_initiative(abilities, quests)


def mountains(abilities, quests):
    if "experienced fighting" in abilities:
        print_pause("You have a flashback of your previous five years in "
                    "these mountains.")
        print_pause("'Gotta save humankind', you say. And then you hurry "
                    "back.")
    else:
        print_pause("The air is thin, crisp and you feel an inner peace.")
        print_pause("The spirits give you an urge to practice your newfound")
        print_pause("strength. You spend five years training nonstop and go "
                    "back")
        abilities.append("experienced fighting")
        quests.append("post-mountain-training")
        take_initiative(abilities, quests)


def take_initiative(abilities, quests):
    while True:
        if "Exit-game" in quests:
            break
        elif "after_running_away" in quests:
            print_pause("Makin' smart moves. Now... where were we? ")
            choice = input("Would you like to go back to the no good"
                           "cyclops(1) Or would you like to go back "
                           "to the forest?(2)\n")
            if choice == '1':
                monster_approach(abilities, quests)
            if choice == '2':
                forest(abilities, quests)
        elif "post-mountain-training" in quests:
            print_pause("You have this harnessed energy that you feel "
                        "within your veins.\nThe spirits tell you you're "
                        "ready to fight the no-good cyclops.")
            choice = input("Fight the cyclops for humankind?(1) Stall time "
                           "and take a stroll through the forest?(2)\nMaybe "
                           "hike on those good 'ol mountains?(3)")
            if choice == '1':
                monster_approach(abilities, quests)
            if choice == '2':
                forest(abilities, quests)
            if choice == '3':
                mountains(abilities, quests)
        elif "after-acheiving-divinity" in quests:
            print_pause("You breathe in your newfound, divine aura and "
                        "some smog clears up. You see mountains and "
                        "your spirits are giving you a sense of urgency")
            choice = input("Would you like to go back to the no good cyclops "
                           "(1) Or would you like to go back to the forest? "
                           "(2)\nMaybe you'd like to go to those mysterious "
                           "mountains?(3)")
            if choice == '1':
                monster_approach(abilities, quests)
            if choice == '2':
                forest(abilities, quests)
            if choice == '3':
                mountains(abilities, quests)
        else:
            choice = input("Approach and attack him with the lack of muscle "
                           "you have.(1) or do you walk away to the forest🌲"
                           "(2)?")
            if choice == '1':
                monster_approach(abilities, quests)

            elif choice == '2':
                forest(abilities, quests)

            else:
                print_pause("Please enter the numbers 1 or 2.")


def play_game():
    abilities = []
    quests = []
    intro()
    take_initiative(abilities, quests)


play_game()
