numbers = [1,2,3,4,5]

doubled_odds = []
for n in numbers:
    if n % 2 == 1:
        doubled_odds.append(n * 2)

print "    ### doubled_odds: ", doubled_odds


doubled_odds_comprehension = [n * 2 for n in numbers if n % 2 == 1]

print "    ### doubled_odds_comprehension: ", doubled_odds_comprehension

matrix = [[1,2,3], [4,5,6]]

flattened = []
for row in matrix:
    for n in row:
        flattened.append(n)

print "    ### flattened: ", flattened

flattened_comprehension = [n for row in matrix for n in row]

print "    ### flattened_comprehension: ", flattened_comprehension
