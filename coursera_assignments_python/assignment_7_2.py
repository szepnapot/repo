fn=raw_input("Enter file name: ")
fh=open(fn)
listspam=[]
for line in fh:
    line=line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        listspam.append(line[20:26])
       
count=0
total=0
floatlist=[]
for spam in listspam:
    spam=spam.strip()
    floatlist.append(float(spam))
    count=count+1
    total=total+float(spam)

print "Average spam confidence:",total/count
fh.close()
  
    
    
    
    
