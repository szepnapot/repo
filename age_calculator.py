import datetime


birthday_format = '%Y/%m/%d'
current = datetime.datetime.now()

print """Simple age calculator, just for fun.
Enter your birthday like 1999/10/12 and see the results.
Type in 'quit' to quit.
"""

while True:
    birthday = raw_input("\nEnter your birthday in YYYY/MM/DD format. <<:")
    try:
        bd_date = datetime.datetime.strptime(birthday, birthday_format)
    except ValueError:
        if birthday == 'QUIT':
            break
        print "Add your birthday in **YYYY/MM/DD** format, eg.: 2000/01/01", birthday
        continue
    else:
        difference = datetime.datetime.now() - bd_date
        day_s, seconds = difference.days, difference.seconds
        minutes = (seconds % 3600) // 60
        hours = day_s * 24 + seconds // 3600
        age = day_s/365
        bd_month, bd_day = bd_date.month, bd_date.day
        next_bd = datetime.datetime.strptime(
            str(current.year) + "/" + birthday[5:7] + "/" + birthday[8:], birthday_format) \
            - current

        if next_bd.days < 0:                        # correcting the output if birthday already passed in this year
            bd_days = int(next_bd.days) + 365
        else:
            bd_days = next_bd.days

        print "You're {} days, {} hours and {} minutes old.".format(
            day_s, hours-(day_s*24), minutes)

        print "You're {}th birthday will be in {} days {} hours and {} minutes later.".format(
            age+1, bd_days, next_bd.seconds/3600, next_bd.seconds/60)

        if age < 60:
            sixty_bd = datetime.datetime.strptime(
                str(current.year+(60-age)) + "/" + birthday[5:7] + "/" + birthday[8:], birthday_format) \
                - current
            print "You've going to be 60 in the year of {}".format(str(current.year+(60-age)))
            print "For your 60th birthday party you have {} days and {} hours left.".format(
                sixty_bd.days, next_bd.seconds/3600)
        else:
            print """\nEnjoy your life and try appreciate every moment of it, you're on a spiritual journey,  \
be grateful and happy,I wish you a lot of joy!"""

print "Bye!"





