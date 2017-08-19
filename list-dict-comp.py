import types

a_list = [1, "4", 9, "a", 0, 4]

doubled = [ e**2 for e in a_list if type(e) == types.IntType ]

print "    ### doubled", doubled

people = [{'name': 'Mary', 'height': 160}, {'name': 'Isla', 'height': 80}, {'name': 'Sam'}]

first = people[0]

print "    ### first", first

heights = [{key for key, value in people}]

print "    ### heights: ", heights
