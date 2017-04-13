def findPrimeSq():
    arr=[]
    divisible=0
    for ind1 in range(100,300):
        arr=[]
        divisible=0
        perfectsq=0
        prime=0
        for i in range(2,ind1):
            if(ind1%i==0):
                divisible=1
                arr.append(i)
        if divisible==0:
            prime=1
            #print "Its prime number",ind1
        #print ind1," ",arr
        l=len(arr)-1
        if l>=0:
            for k in range(0,len(arr)):
                sq=(arr[k] * arr[k])
                #print sq
                if(sq == ind1):
                    perfectsq=1
                    #print "Its perfect sq of ",arr[k],ind1
                    break
        if prime==1:
            print "Foo"
        elif perfectsq==1:
            print "Bar"
        else:
            print "FooBar"
findPrimeSq()
