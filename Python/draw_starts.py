#takes a list of numbers and prints out * and for string with lower case of first letter of the length
def draw_stars(list):
  for index in range(len(list)):
      if type(list[index]) == int:
          print "*" * list[index]
      elif type(list[index]) == str:
          #low=list[index].lower()
          print (list[index][0].lower())*len(list[index])
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(x)
