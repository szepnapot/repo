while True:
        x = float(raw_input("Mennyi az annyi teso?"))
        if x < 10.0:
                print "Kisebb"
                continue
        if x == 10.0:
                print "Bingo!"
                break
	
        if x > 10.0:
                print "Nagyobb!"
                continue
        
print "Ennyi voltam, puszi!"
ext = raw_input("Press any key to exit..")
quit()
