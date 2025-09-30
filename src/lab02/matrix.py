def transpose(numlist):
    finalresult = []
    for num in range(len(numlist) - 1):
        if len(numlist[num]) != len(numlist[num + 1]):
            raise ValueError
    if numlist == []:
        return []
    cols = len(numlist)
    rows = len(numlist[0])
    for i in range(rows):
        interresult = []
        for j in range(cols):
            interresult.append(numlist[j][i])
        finalresult.append(interresult)
    return finalresult

def unique_sorted(numlist):
    finalresult = []
    for num in range(len(numlist) - 1):
        if len(numlist[num]) == len(numlist[num + 1]):
            finalresult.append(sum(numlist[num]))
        else:
            raise ValueError
    finalresult.append(sum(numlist[-1]))
    return finalresult

def col_sums(numlist):
    finalresult = []
    altfinalresult = []
    if len(numlist) == 1:
        altfinalresult.append(numlist[0][0])
        return altfinalresult
    else:
        for num in range(len(numlist) - 1):
            if len(numlist[num]) == len(numlist[num + 1]):
                for i in range(len(numlist[0])):
                    finalresult.append(numlist[num][i] + numlist[num + 1][i])
            else:
                raise ValueError
        return finalresult

n1 = [[1, 2], [3, 4]]
n2 = [[1, 2, 3], [4, 5, 6]]
n3 = [[1, 2, 3], [4, 5, 6]]

print(transpose(n1))
print(unique_sorted(n2))
print(col_sums(n3))
        