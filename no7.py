def consecutiveLst(lst):
    flags="True"
    lst=sorted(lst)
    for i in range (len(lst)-1):
        if not lst[i]+1 == lst[i+1]:
            flags="False"
            break
    print(flags)


lst1=eval(input())
lst2=eval(input())
lst1.extend(lst2)
consecutiveLst(lst1)