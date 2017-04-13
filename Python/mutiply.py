def multiply(list,num):
    b=[]
    for i in range(len(list)):
        b.append(list[i]*num)
    return b
res = multiply([2,4,10,16], 5)
print res
#hacker chanllenge
def layered_multiples(arr):
  # your code here
  item=0
  index=0
  new_array=[]
  array=[]
  for item in range(0,len(arr)):
      array=[]
      for index in range(arr[item]):
          array.append(1)
      new_array.append(array)
  return new_array
mul=multiply([2,4,5],3)
print mul
x = layered_multiples(mul)
print x
# output
#[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
