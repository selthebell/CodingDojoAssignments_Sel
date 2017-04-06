x = [19,2,54,-2,7,12,98,32,10,-3,6,9]
x.sort()
newList=[]
print x
for item in range(len(x)/2):
    newList.append(x[item])
finalList=[]
finalList.append(newList)
for item in range(len(x)/2,len(x)):
    finalList.append(x[item])
print finalList
