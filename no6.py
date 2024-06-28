def datefor(a):
    s=a.split("/")
    ans=''
    for i in s:
        ans= i + ans
    print(ans)
a=input()
datefor(a)