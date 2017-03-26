import itertools
from rules import AND, EQUIVALENT, IMPLIES, NOT, OR

combinations = itertools.product('012', repeat=9)

x = ('0', '0', '0', '1', '1', '1', '2', '2', '2')
y = (0, 1, 2, 0, 1, 2, 0, 1, 2)

notCombinations = itertools.product('012', repeat=3)


for i in combinations:
    equivalentList = i
    # print "i"
    # print i
    for j in combinations:
        # print "j"
        orList = j
        for k in combinations:
            # print "k"
            andList = k
            for l in combinations:
                # print "l"
                impliesList = l
                for e in notCombinations:
                    print "e"
                    notList = e
                    a = NOT(x, notList)
                    # print "a"
                    # print a
                    b = NOT(a, notList)
                    #  print "b"
                    # print b
                    # print notList
                    g10 = IMPLIES(a, x, impliesList)
                    print g10
