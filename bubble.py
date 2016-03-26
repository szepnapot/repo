import time
import random
import sys


def intro():
    print """Hy it's Bubble Sort time, as I heard.
Give me some numbers, the more you gave the harder for me to sort 'em
So please do so, I'm super depressed with so much free RAM.
Available calls: HELP, FAQ, RANDOM, MANUAL, QUIT.

**hint** try to generate a random list > 1000 to see the real power ;)"""


def reading():
    print """\nFor further reading about sorting algortithms:
http://tinyurl.com/zj2dxyo ------- Bubble-sort,
http://tinyurl.com/q5bu9ks ------- Basic algorithms in Python,
http://tinyurl.com/8z3h2wt ------- Timsort (.sort()) wikipedia
http://tinyurl.com/zx94guw ------- docs about the basics of sorting"""


def bubblesort(alist):
    """Bubble-algorithm"""

    start_time = time.clock()
    for passnum in range(len(alist)-1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
    total_time = time.clock() - start_time
    print "\nIt took me {} seconds to organize it via 'original' Bubble-sort algorithm".format(total_time)
    print alist


def short_bubble(alist):
    """Bubble-algorithm with some tuning.
    If no exchanges made the list is already sorted,
    get rid of wasted exchanges"""

    start_time = time.clock()
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                exchanges = True
                temp = alist[i]
                alist[i], alist[i+1] = alist[i+1], temp
                passnum -= 1
    total_time = time.clock() - start_time
    print "\nIt took me {} seconds to organize it via 'tuning' Bubble-sort algorithm".format(total_time)
    print alist


def simple_sort(alist):
    """simple sorting via python's .sort() method,
    which is based on the 'Timsort' algorithm.
    https://en.wikipedia.org/wiki/Timsort"""
    start_time = time.clock()
    alist.sort()
    total_time = time.clock() - start_time
    print "\nIt took me {} seconds to organize it via built-in .sort() method.".format(total_time)
    print alist

def manual():
    alist = []
    print "Enter whole numbers one-by-one, if you finished type DONE"
    while True:
        nums = raw_input(">>: ").upper()
        if nums == 'DONE':
            break
        else:
            try:
                nums = int(nums)
            except ValueError:
                print "Not a number, try again..", nums
            finally:
                alist.append(nums)
    return alist

def random_gen():
    print "\nKeep in mind that a very long list can take a lot of time to bubble sort."
    max_num = int(raw_input("Maximum range: "))
    alist = (random.sample(xrange(10000000), max_num))
    return alist

def menu():
    while True:
        inp = raw_input("\nRandom list or create manually? >>: ").upper()
        if inp == 'MANUAL':
            alist = manual()
            return alist
        elif inp == 'RANDOM':
            alist = random_gen()
            return alist
        elif inp == 'QUIT':
            sys.exit()
        elif inp == 'HELP':
            intro()
            continue
        elif inp == 'FAQ':
            reading()
            continue
        else:
            print "Invalid call, random mode choose for you."
            alist = random_gen()
            return alist

def compare():
    intro()
    alist = menu()
    start = raw_input("Press any key to begin...")
    bubblesort(alist)
    short_bubble(alist)
    simple_sort(alist)

compare()

