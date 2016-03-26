import random
import os
import sys


words = [
    'apple',
    'orange',
    'banana',
    'pearl',
    'peach',
    'lemon',
    'melon',
    'thunder',
    'mango',
    'papaya',
    'kiwi',
    'grapefruit',
    'blueberry'
]

def welcome():
    start = raw_input("Press enter/return to start or Q to quit ").lower()
    if start == 'q':
        print "Bye!"
        sys.exit()
    else:
        return True

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def draw(bad_guesses,good_guesses, secret):
    clear()
    print "Strikes: {}/7".format(len(bad_guesses))
    print ""

    for letter in bad_guesses:
        print letter,
    print "\n\n"

    for letter in secret:
            if letter in good_guesses:
                print letter,
            else:
                print "'_'",
    print ""


def get_guess(bad_guesses,good_guesses):
    while True:
        guess = raw_input("Guess a letter: ").lower()

        if len(guess) !=1:
            print "You can only guess a single letter !"
        elif guess in bad_guesses or guess in good_guesses:
            print "You've already guess that letter!"
        elif not guess.isalpha():
            print "You can only guess letters!"
        else:
            return guess

def play(done):
    clear()
    secret = random.choice(words)
    bad_guesses = []
    good_guesses = []

    while True:
        draw(bad_guesses,good_guesses,secret)
        guess = get_guess(bad_guesses,good_guesses)

        if guess in secret:
            good_guesses.append(guess)
            found = True
            for letter in secret:
                if letter not in good_guesses:
                    found = False
            if found:
                print "You win!"
                print "The secret word was {}".format(secret)
                done = True
        else:
            bad_guesses.append(guess)
            if len(bad_guesses) == 7:
                draw(bad_guesses,good_guesses,secret)
                print "You lost!"
                print "The secret word was {}".format(secret)
                done = True
        if done:
            play_again = raw_input("Play again? Y/n").lower()
            if play_again != 'n':
                return play(done=False)
            else:
                sys.exit()

print "Welcome to Letter Guess!"

done = False

while True:
    clear()
    welcome()
    play(done)