fname=raw_input("Enter file name: ")
try:
    fh=open(fname)
except:
    print "Error! File not found."
    exit()

dates=dict()
lst=list()
for line in fh:
    if not line.startswith("From") or line.startswith("From:"):
        continue
    line=line.strip().split()
    date=line[2]
    lst.append(date)

for count in lst:
    dates[count]=dates.get(count,0)+1
print dates
