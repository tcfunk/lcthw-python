i = 0
numbers = []

while i < 6:
  print "At the top i is %d" % i
  numbers.append(i)

  i = i + 1
  print "Numbers now: ", numbers
  print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
  print num

def make_numbers(list):
  if list[len(list)-1] < 5:
    return make_numbers(list + [list[len(list)-1] + 1])
  else:
    return list

print "\n\nRecursive approach:\n"

results = make_numbers([0])

for num in results:
  print num