name   = 'Tyler C. Funk'
age    = 25
height = 71  #inches
weight = 160 #lbs
eyes   = 'Brown'
teeth  = 'Not so white...'
hair   = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He weighs %d pounds." % weight
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
  age, height, weight, age + height + weight)