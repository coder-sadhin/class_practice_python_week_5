def common_elements(lst1, lst2):
    newLst=[]
    for i in lst1:
        for j in lst2:
            if i==j:
                if not i in newLst:
                    newLst.append(i)
    return newLst


lst1 = eval(input())
lst2 = eval(input())
print(common_elements(lst1, lst2))