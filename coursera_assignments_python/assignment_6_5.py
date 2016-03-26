text = "X-DSPAM-Confidence:    0.8475";
start=text.find("0")
num=text[start:50]
num=float(num)
print num