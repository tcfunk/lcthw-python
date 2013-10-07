def print_barrier():
  print '-' * 10

# create a mapping of state to abbreviation
states = {
  'Orgeon'    : 'OR',
  'Florida'   : 'FL',
  'California': 'CA',
  'New York'  : 'NY',
  'Michigan'  : 'MI'
}

# create a basic set of states and some cities in them
cities = {
  'CA': 'San Francisco',
  'MI': 'Detroit',
  'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print_barrier()
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print_barrier()
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbrevation is: ", states['Florida']

# do it by using the state then cities dict
print_barrier()
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print eery state abbreviation
print_barrier()
for state, abbrev in states.items():
  print "%s is abbrevated %s" % (state, abbrev)

# print every city in state
print_barrier()
for abbrev, city in cities.items():
  print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print_barrier()
for state, abbrev in states.items():
  print "%s state is abbreviated %s and has city %s" % (
    state, abbrev, cities[abbrev])

# safeley get an abbreviation by state that might not be there
print_barrier()
state = states.get('Texas', None)
if not state:
  print "Sorry, no Texas"

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city