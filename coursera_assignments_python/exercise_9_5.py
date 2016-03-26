fname=raw_input("Enter file name: ")
try:
    fh=open(fname)
except:
    print "Error! File not found."
    exit()

add=dict()
lst=list()
for line in fh:
    if not line.startswith("From "):
        continue
    line=line.strip().split()
    email=line[1]
    address=email.split('@')
    lst.append(address[1])


for count in lst:
    add[count]=add.get(count,0)+1

print add

