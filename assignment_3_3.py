#assignment 3.3
score=raw_input("Enter a score:")
try:
    s=float(score)
except:
    print "Error. The input must be between 0.0 and 1.0."
    quit()

if s>= 0.9:
    print "A"
elif s>=0.8:
    print "B"
elif s>=0.7:
    print "C"
elif s>=0.6:
    print "D"
elif s<0.6:
    print "F"