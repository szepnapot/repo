fn=raw_input("Enter file name: ")
fo=open(fn)
for line in fo:
    line=line.rstrip()
    print line.upper()

