def multiply(rows,cols):
    print "x  ",
    for i in range(1,rows+1):
        if i >=10:
            print i," ",
        else:
            print i,"  ",
    print ""
    for ind in range(1,rows+1):
        print ind," ",
        for ind1 in range(1,cols+1):
            res=ind*ind1
            if(res<=9):
                print res,"  ",
            elif (res>9 and res<=99):
                print res," ",
            else:
                print res," ",

        print " "
multiply(12,12)
