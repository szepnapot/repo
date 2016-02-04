fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
for line in fh:
    if not line.startswith("From "):
        continue
    else:
        count=count+1
        words=line.split()
        addr=words[1]
        print addr

print "There were", count, "lines in the file with From as the first word"
