import itertools
from rules import AND, EQUIVALENT, IMPLIES, NOT, OR

combinations = itertools.product('012', repeat=9)
comb = []
for c in combinations:
    comb.append(list(c))
# print comb/

x = ('0', '0', '0', '1', '1', '1', '2', '2', '2')
y = ('0', '1', '2', '0', '1', '2', '0', '1', '2')

notCombinations = itertools.product('012', repeat=3)
nc = []
for n in notCombinations:
    nc.append(list(n))

for i in comb:
    equivalentList = i
    # print "i"
    # print i
    for j in comb:
        # print "j"
        orList = j
        for k in comb:
            # print "k"
            andList = k
            for l in comb:
                # print "l"
                impliesList = l
                for e in nc:
                    print "e"
                    notList = e
                    a = NOT(x, notList)
                    b = NOT(a, notList)
                    g10 = IMPLIES(a, x, impliesList)
                    print g10
