import random

# limit the number of guesses
# catch when someone submits a non_intiger
# print 'too low' and 'too high'
# let people play again
print """Heyya Friend! I think a number between 1 and 10, try and guess it! \
\nYou have 4 lifes! Good Luck!"""

def game():
    secret = random.randint(1,10)
    guesses = []
    while len(guesses) < 4:
        try:
            guess = int(raw_input("Guess a number between 1 and 10: "))
        except ValueError:
            print "Oppy, {} is not a valid number.".format(guess)
            continue
        else:
            if secret == guess:
                print "Woah! Nice! {} is my secret number :)".format(secret)
                break
            elif secret > guess:
                print "My number is bigger."
            else:
                print "My number is smaller."
            guesses.append(guess)
    else:
        print "You didn't get it. My number was {}.".format(secret)

    play_again = raw_input("Do you want to play again? Y/n ")
    if play_again.lower() != "n":
        game()
    else:
        print "Bye!"


game()