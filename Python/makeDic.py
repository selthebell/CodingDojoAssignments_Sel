name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas","dog"]
def make_dict(arr1, arr2):
  new_dict = {}
  lenArr1=len(arr1)
  lenArr2=len(arr2)
  if lenArr1 > lenArr2:
      iterate=lenAarr1
      big=arr1
      small=arr2
  else:
      iterate=lenArr2
      big=arr2
      small=arr1
  for ind in range(iterate):
      try:
          new_dict[big[ind]]=small[ind]
      except IndexError:
          new_dict[big[ind]]="None"
  # your code here
  return new_dict
dt=make_dict(name,favorite_animal)
print dt
