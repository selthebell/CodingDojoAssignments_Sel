#listItems = ['magical unicorns',19,'hello',98.98,'world']
#listItems = [2,3,1,7,4,12]
listItems = ['magical','unicorns']
intCt=0
strCt=0
sum=0
newStr=""
for i in range(0,len(listItems)):
    #print listItems[i]
    if type(listItems[i]) is int or type(listItems[i]) is float:
        sum += listItems[i]
        intCt=1
    elif type(listItems[i]) is str:
        newStr += listItems[i]
        strCt=1
if strCt==1 and intCt==1:
    print "The array you entered is of mixed type"
    print "Sum is : ",sum
    print "New String is :", newStr
elif strCt==1 and intCt ==0:
    print "The array you entered is of string type"
    print "String: {}".format(newStr)
elif strCt==0 and intCt ==1:
    print "The array you entered is of integer type"
    print "Sum is {}".format(sum)
