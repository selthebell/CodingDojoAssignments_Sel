# input
l = ['hello','world','my','name','is','Anna']
char = 'o'
newStr = []
i=0
j=0
# output
#n = ['hello','world']
for i in range(0,len(l)):
    for j in range(0,len(l[i])):
        if(l[i][j] == char):
            newStr.append(l[i])
            break
print newStr
