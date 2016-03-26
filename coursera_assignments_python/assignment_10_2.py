fname=raw_input("Enter file name: ")
try:
    fh=open(fname)
except:
    print "Error! File not found."
    exit()

d=dict()
lst=list()
lst1=list()
for line in fh:
    if not line.startswith("From "):
        continue
    line=line.strip().split()
    date=line[5].split(":")
    hour=date[0]
    lst.append(hour)
    for count in lst:
        d[count]=d.get(count,0)+1
for k,v in d.items():
    lst1.append((k,v))
lst1.sort
print lst1