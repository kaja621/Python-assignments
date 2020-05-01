x=int(input("enter first number :"))
y=int(input("Enter last number :"))
if x>=1 and y<=1000000000 and y-x<=100000:
    m=x
    l=y
    n=l+1
    lst=[]
    lst1=[]
    lst2=[]
    count=0
    for i in range(m,n):
        lst.append(i)
    if 2 in lst:
        print("The list starts with 2")
    else:
        for l in lst:
            for i in range(2,m):
                v=l%i
                if v==0:
                    lst1.append(l)
    for p in lst:
        n=int(l/p)+1
        for i in range(2,n):
            if p*i <=l and p*i not in lst1:
                lst1.append(p*i)

    print("lst",lst)
    for i in lst:
        if i not in lst1:
            lst2.append(i)
    print("prime numbers =",lst2)
else:
    print("wrong input range!")
