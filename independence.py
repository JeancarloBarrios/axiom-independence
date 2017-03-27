import itertools
from rules import AND, EQUIVALENT, IMPLIES, NOT, OR, checkTaut

def proof():
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
                        notList = e
                        a = NOT(x, notList)
                        a = NOT(a, notList)
                        G10 = IMPLIES(a, x, impliesList)
                        a = IMPLIES(y, x, impliesList)
                        G1 = IMPLIES(x, a, impliesList)
                        a = AND(x, y, andList)
                        a = IMPLIES(y, a, impliesList)
                        G3 = IMPLIES(x, a, impliesList)
                        a = AND(x, y, andList)
                        G4 = IMPLIES(a, x, impliesList)
                        a = AND(x, y, andList)
                        G5 = IMPLIES(a, y, impliesList)
                        a = OR(x, y, orList)
                        G6 = IMPLIES(x, a, impliesList)
                        a = OR(x, y, orList)
                        G7 = IMPLIES(y, a, impliesList)
                        a = NOT(y, notList)
                        a = IMPLIES(x, a, impliesList)
                        b = NOT(x, notList)
                        a = IMPLIES(a, b, impliesList)
                        b = IMPLIES(x, y, impliesList)
                        G9 = IMPLIES(b, a, impliesList)
                        a = IMPLIES(x, y, impliesList)
                        b = IMPLIES(y, x, impliesList)
                        a = IMPLIES(a, b, impliesList)
                        b = EQUIVALENT(x, y, equivalentList)
                        G11 = IMPLIES(a, b, impliesList)
                        a = EQUIVALENT(x, y, equivalentList)
                        b = IMPLIES(x, y, impliesList)
                        G12 = IMPLIES(a, b, impliesList)
                        a = EQUIVALENT(x, y, equivalentList)
                        b = IMPLIES(y, x, impliesList)
                        G13 = IMPLIES(a, b, impliesList)

                        if not(checkTaut(G10)) and checkTaut(G1) and checkTaut(G3) and checkTaut(G4) and checkTaut(G4) and checkTaut(G6) and checkTaut(G7) and checkTaut(G9) and checkTaut(G10) and checkTaut(G11) and checkTaut(G12) and checkTaut(G13):
                            result = {
                                "G1": G1,
                                "G3": G3,
                                "G4": G4,
                                "G5": G5,
                                "G6": G6,
                                "G7": G7,
                                "G9": G9,
                                "G10": G10,
                                "G11": G11,
                                "G12": G12,
                                "G13": G13
                            }
                            return result
    return false

print proof()
