fname = 'mbox.txt'
fh = open(fname)
count = 0
for line in fh:
    if not line.startswith("From "):
        continue
    else:
        line = line.rstrip()
        words = line.split()
        pieces = words[1].split('@')
        dns = pieces[1]
        print dns


