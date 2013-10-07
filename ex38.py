ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
more_stuff = ['Day', 'Night', 'Song', 'Frisbee', 'Corn', 'Banana', 'Girl', 'Boy']

while len(stuff) != 10:
  next_one = more_stuff.pop(0)
  print 'Adding ', next_one, '...'
  stuff.append(next_one)
  print "There're %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do somet things with stuff"

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:5])