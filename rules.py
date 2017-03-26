

def NOT(a, list):
    result = []
    for i in range(0, 9, 1):
        if a[i] == '0':
            result.append(list[0])
        elif a[i] == '1':
            result.append(list[1])
        elif a[i] == '2':
            result.append(list[2])
    return result


def IMPLIES(a, b, list):
    # print list
    # print len(list)
    result = []
    for i in range(0, 9, 1):
        if a[i] == '1' and b[i] == '1':
            result.append(list[0])
        elif a[i] == '1' and b[i]=='0':
            result.append(list[1])
        elif a[i] == '0' and b[i] == '1':
            result.append(list[2])
        elif a[i] == '0' and b[i] == '0':
            result.append(list[3])
        elif a[i] == '0' and b[i] == '2':
            result.append(list[4])
        elif a[i] == '2' and b[i] == '0':
            result.append(list[5])
        elif a[i] == '1' and b[i] == '2':
            result.append(list[6])
        elif a[i] == '2' and b[i] == '1':
             result.append(list[7])
        elif a[i] =='2' and b[i] == '2':
            result.append(list[8])
    return result


def EQUIVALENT(a, b, list):
    result = []
    for i in range(0, 9, 1):
        if a[i] == '1' and b[i] == '1':
            result.append(list[0])
        elif a[i] == '1' and b[i]=='0':
            result.append(list[1])
        elif a[i] == '0' and b[i] == '1':
            result.append(list[2])
        elif a[i] == '0' and b[i] == '0':
            result.append(list[3])
        elif a[i] == '0' and b[i] == '2':
            result.append(list[4])
        elif a[i] == '2' and b[i] == '0':
            result.append(list[5])
        elif a[i] == '1' and b[i] == '2':
            result.append(list[6])
        elif a[i] == '2' and b[i] == '1':
             result.append(list[7])
        elif a[i] =='2' and b[i] == '2':
            result.append(list[8])
    return result


def AND(a, b, list):
    result = []
    for i in range(0, 9, 1):
        if a[i] == '1' and b[i] == '1':
            result.append(list[0])
        elif a[i] == '1' and b[i]=='0':
            result.append(list[1])
        elif a[i] == '0' and b[i] == '1':
            result.append(list[2])
        elif a[i] == '0' and b[i] == '0':
            result.append(list[3])
        elif a[i] == '0' and b[i] == '2':
            result.append(list[4])
        elif a[i] == '2' and b[i] == '0':
            result.append(list[5])
        elif a[i] == '1' and b[i] == '2':
            result.append(list[6])
        elif a[i] == '2' and b[i] == '1':
             result.append(list[7])
        elif a[i] =='2' and b[i] == '2':
            result.append(list[8])
    return result
'0'

def OR(a, b, list):
    result = []
    for i in range(0, 9, 1):
        if a[i] == '1' and b[i] == '1':
            result.append(list[0])
        elif a[i] == '1' and b[i]=='0':
            result.append(list[1])
        elif a[i] == '0' and b[i] == '1':
            result.append(list[2])
        elif a[i] == '0' and b[i] == '0':
            result.append(list[3])
        elif a[i] == '0' and b[i] == '2':
            result.append(list[4])
        elif a[i] == '2' and b[i] == '0':
            result.append(list[5])
        elif a[i] == '1' and b[i] == '2':
            result.append(list[6])
        elif a[i] == '2' and b[i] == '1':
             result.append(list[7])
        elif a[i] =='2' and b[i] == '2':
            result.append(list[8])
    return result
