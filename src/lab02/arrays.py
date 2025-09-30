def min_max(numlist):
    maxnum = max(numlist)
    minnum = min(numlist)
    minmax = (minnum, maxnum)
    return minmax

def unique_sorted(numlist):
    sortnumlist = sorted(set(numlist))
    return sortnumlist

def flatten(tuplenumlist):
    massivnumlist = []
    for numlist in tuplenumlist:
        if isinstance(numlist, (list, tuple)):
            for num in numlist:
                massivnumlist.append(num)
        else:
            raise TypeError
    return massivnumlist

n3 = [[1, 2], "ab"]
print(flatten(n3))

