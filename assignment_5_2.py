largest = -1
smallest = None
while True:
    num = raw_input("Enter a number: ")
    try:
        num=int(num)
    except:
        print "Invalid input"
    if num == "done" : break
    elif largest<num:
        largest=num
        continue
    if smallest is None:
        smallest=num
    elif smallest>num:
        smallest=num

print "Maximum is", largest
print "Minimum is", smallest