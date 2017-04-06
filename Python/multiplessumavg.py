#to print odd numbers
for x in range(1,1000):
    if(x%2 != 0):
        print x
#to print multiples
#for x in range(5,1000000):
#    if(x%5 == 0):
#        print x
#sum of list
sum=0
a = [1, 2, 5, 10, 255, 3]
for l in range(0,len(a)):
    sum += a[l]
print "Sum: ",sum
print "Avg: ",sum/len(a)
