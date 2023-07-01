from random import choice


def rolltheDice():
    the_options = [1, 2, 3, 4, 5, 6]
    thechoice = choice(the_options)
    print(thechoice)
    if thechoice == 6:
        print("you have Got 6,lets Roll again")
        thechoice = choice(the_options)
        print(thechoice)


rolltheDice()
