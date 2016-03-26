def computepay(h,r):
    if h>40:
        return (h-40)*(1.5*r)+40*r
    else:
        return h*r

h = float(raw_input("Enter Hours:"))
r =float(raw_input("Enter Hours:"))
p = computepay(h,r)
print p