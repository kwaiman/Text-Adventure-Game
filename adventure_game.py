import time
import random


def print_pause(message, seconds):
    print(message)
    time.sleep(seconds)


def choose():
    while True:
        action_choice = input("Enter 1 or 2\n")
        if action_choice != "1" and action_choice != "2":
            print_pause("Please type a valid response: EITHER 1 or 2.", 1)
        else:
            return action_choice


def home(gadget):
    print_pause("You are now at home", 1)
    if gadget != "":
        print_pause("Doraemon noticed that you have one of his gadgets,"
                    " and is taking " f"{gadget}" " back!", 1)
        gadget = ""
    gadgets_list = ["What-if Phone Booth", "useless gadget",
                    "Anything Controller"]
    print_pause("Doraemon's asleep. Do you want to 1) steal a gadget"
                " from his pocket; or 2) wake him up and talk to him?", 1)
    action_choice = choose()
    if action_choice == "1":
        print_pause("You're trying to steal from his pocket, but you can't"
                    " see through what's inside!", 1)
        print_pause("So you just picked one randomly.", 1)
        gadget = random.choice(gadgets_list)
        print_pause(f"You get {gadget}!!", 1)
    elif action_choice == "2":
        print_pause("Doreamon's awake now!", 1)
        print_pause("Do you want to 1) ask for his gadget; or 2) tell "
                    "him you will buy him favorite pastry?", 1)
        action_choice = choose()
        if action_choice == "1":
            gadget = gadgets_list[1]
            print_pause("Since you waked him up during a good sleep, he was"
                        " very pissed and decided only to give "
                        "you a useless gadget. Pity!", 1)
        elif action_choice == "2":
            print_pause("He was overjoyed to hear that you will buy"
                        " him his favorite pastry, Dorayaki!", 1)
            gadget = gadgets_list[0]
            print_pause("To return this favor, he decided to lend you the"
                        " most powerful gadget, the What-if Phone Booth!", 1)
    print_pause("Now you have to decide to go to 1) school or 2) "
                "playground.", 1)
    action_choice = choose()
    if action_choice == "1":
        school(gadget)
    elif action_choice == "2":
        playground(gadget)


def school(gadget):
    print_pause("You are now at school", 1)
    print_pause("You've met Shizuka, your long-time crush! But she's "
                "talking to Dekisugi, the prince-charming and genius! Do "
                "you want to 1) confess; or 2) shy away from her?", 1)
    action_choice = choose()
    if action_choice == "1":
        print_pause("You did it! You just told her you wanna marry her when"
                    " both of you become adults!", 3)
        print_pause("BUT!!", 2)
        print_pause("......\n......", 2)
        print_pause("She rejected you! And she said she wouldn't like a"
                    " loser like you!", 1)
        print_pause("What should you do? Do you 1) use the gadget you now"
                    " have; or 2) just run away?", 1)
        action_choice = choose()
        if action_choice == "1":
            print_pause(f"Let's see what you have! You have {gadget}!", 1)
            if gadget == "What-if Phone Booth":
                print_pause("You can use the What-if Phone Booth to make any"
                            " what-if come true!", 1)
                print_pause("Now that you wished: what if I will "
                            "marry Shizuka?", 1)
                print_pause("Time immediately leaps to 20 years later;", 3)
                print_pause("Shizuka has become your wife, and then happily"
                            " ever after!", 1)
                play_again("won")
                return
            elif gadget == "Anything Controller":
                print_pause("Great! Let's use it to control Shizuka so that"
                            " she'll marry me!", 3)
                print_pause("Oh no! Turns out it can't be used on females! "
                            "now she is very mad about you trying to "
                            "manipulate her!!", 1)
                print_pause("She will NEVER see you again! You lost!!", 1)
                play_again("lost")
                return
            elif gadget == "useless gadget":
                print_pause("No way! With this worthless piece of garbage,"
                            " there is nothing you can do:(", 1)
                print_pause("The only thing you can do is run away...", 1)
    elif action_choice == "2":
        print_pause("She seems so happy talking to Dekisugi:(", 1)
        print_pause("Let's get out of here.", 1)
    print_pause("Now you have to decide to go to 1) home or 2) playground.", 1)
    action_choice = choose()
    if action_choice == "1":
        home(gadget)
    elif action_choice == "2":
        playground(gadget)


def playground(gadget):
    print_pause("You are now at playground", 1)
    print_pause("You've met Gian, your long-time nemesis! He seems furious"
                " right now, and he spotted you. Do you want to"
                " 1) talk to him; or 2) run away?", 1)
    action_choice = choose()
    if action_choice == "1":
        print_pause("After you greeted him, he said he's incensed as he"
                    " just lost a baseball match.", 1)
        print_pause("Because of that, he really wanna beat up someone"
                    " so badly!!", 1)
        print_pause("What should you do? Do you 1) fight him with the "
                    "gadget you have; or 2) just run away?", 1)
        action_choice = choose()
        if action_choice == "1":
            print_pause(f"Let's see what you have! You have {gadget}!", 1)
            if gadget == "What-if Phone Booth":
                print_pause("You can use the What-if Phone Booth to make any"
                            " what-if come true!", 1)
                print_pause("Let's kick his ass! Now that you wished: what if"
                            " I am a kungfu master?", 1)
                print_pause("You've used your kungfu skills to beat Gian!! "
                            "He's now begging for mercy!!", 2)
                play_again("won")
                return
            elif gadget == "Anything Controller":
                print_pause("Great! Let's use it to control Gian!", 1)
                print_pause("Now that he's your slave! He'll do whatever you"
                            " want!!", 1)
                print_pause("\"Stand there still and let me PUNCH you in the"
                            " FACE!\", You won!", 1)
                play_again("won")
                return
            elif gadget == "useless gadget":
                print_pause("Come on! Now you have no choice but to fight him"
                            " in a hand-to-hand combat!", 1)
                print_pause("He's hit you so hard that you can barely stand"
                            " up. But you NEVER give up!", 1)
                print_pause("You've hit him back!", 1)
                damage = random.randint(0, 1000)
                if damage > 750:
                    print_pause("You are very lucky! You accidentally hit"
                                " his groin, and now he's in anguish!", 3)
                    print_pause("You defeated him!", 2)
                    play_again("won")
                    return
                else:
                    print_pause("Your hit was too weak, and he continued"
                                " to beat you up!", 1)
                    print_pause("Gian's just way too strong! He finished you"
                                " using his favorite wrestler, Randy Orton's"
                                " finishing move:", 2)
                    print_pause("R !!", 2)
                    print_pause("K !!", 2)
                    print_pause("O !!", 2)
                    print_pause("You're now lying on the ground, hopelessly"
                                " staring at Gian...", 2)
                    play_again("lost")
                    return
        elif action_choice == "2":
            print_pause("He's chasing after you! But fortunately he didn't"
                        " catch you.", 1)
    elif action_choice == "2":
        print_pause("Luckily, he didn't chase after you.", 1)
    print_pause("Now you have to decide to go to 1) home or 2) school.", 1)
    action_choice = choose()
    if action_choice == "1":
        home(gadget)
    elif action_choice == "2":
        school(gadget)


def play_again(result):
    if result == "won":
        print_pause("Congrats!! You've won the game.", 1)
    elif result == "lost":
        print_pause("Sorry:( You've lost.", 1)
    print_pause("Do you wanna start again? Choose 1) for Yes; 2) for No", 1)
    action_choice = choose()
    if action_choice == "1":
        print_pause("Great! We will start again.", 1)
        start_game()
    print_pause("Thank you for playing! I know this game is far from perfect"
                " but hope you enjoyed it:)", 1)
    print_pause("Bye! Have a nice day.", 1)


def start_game():
    gadget = ""
    print_pause("Welcome!", 1)
    print_pause("You are now in the world of Doraemon!!, one of the most"
                " well-known Japanese manga!", 1)
    print_pause("You will now become the protagonist of this manga,"
                " Nobita!!", 1)
    print_pause("You are now inside : Your mission is to either defeat"
                " Gian in a fight,"
                " who's been bullying you, with Doraemon's gadgets;", 1)
    print_pause("OR win the heart of Shizuka,"
                " your long-time crush, and marry her (but again, with"
                " Doraemon's gadgets).", 1)
    print_pause("You'll first begin your journey at home...", 2)
    home(gadget)


start_game()
