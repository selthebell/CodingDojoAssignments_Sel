testV=[1,2,3,9,9,9,9,9,0,0,0,]
print type(testV)
if type(testV) is int:
    if testV >= 100:
        print "That's a big number!"
    else:
        print  "That's a small number"
elif type(testV) is str:
    if len(testV) >= 50:
        print "Long sentence."
    else:
        print "Short sentence."
elif type(testV) is list:
    if len(testV) >= 10:
        print "Big list!"
    else:
        print "short list!"
