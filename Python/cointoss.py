import random
# x = .23945593
# y = .798839238
# x_rounded = round(x)
# # x_rounded will be rounded down to 0
# y_rounded = round(y)
# y_rounded will be rounded up to 1
def cointoss(times):
    head=0
    tail=0
    #print "Attempt #{}: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far"
    for index in range(1,times):
        x=int(round(random.random()))
        print "Attemp #",index,": Throwing a coin",
        if x == 0:
            head +=1
            print " Its a head! ... Got ",head," head(s) so far and ",tail," tails(s) so far"
        else:
            tail +=1
            print " Its a tail! ... Got ",head," head(s) so far and ",tail," tails(s) so far"
    print "End of the program. Thank You"

cointoss(5001)
