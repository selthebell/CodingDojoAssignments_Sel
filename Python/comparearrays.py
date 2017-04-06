#list_one = ['celery','carrots','bread','milk']
#list_two = ['celery','carrots','bread','cream']
#list_one = [1,2,5,6,2]
#list_two = [1,2,5,6,2]
list_one = [1,2,5,6,5,9]
list_two = [1,2,5,6,5,9]
counter=0
if len(list_one) == len(list_two):
    for i in range(0,len(list_one)):
        if list_one[i] <> list_two[i]:
            counter += 1
            print "Not Equal"
            break
    if i==(len(list_one)-1) and counter==0:
        print "Equal"
else:
    print "Not Equal"
