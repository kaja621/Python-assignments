"""Given an array S of size N , check if it is possible to split sequence into two sequences -
s1 to si and si+1 to sN such that first sequence is strictly decreasing and second is strictly increasing. Print true/false as output.

Input Format:
First line contains a single integer N denoting the size of the input.
Next N lines contain a single integer each denoting the elements of the array S.

Constraints
0 < N < 1000 Each number in sequence S is > 0 and < 1000000000"""
from array import*
n=int(input("Enter the number of elements:"))
if 0<n<1000:
    N=n
    S=array('i',[])
    for i in range(N):
        x=int(input())
        if x<1000000000 and x>0:
            S.append(x)
        else:continue
    print(S)
    l=len(S)
    p=array("i",[])
    q=array("i",[])
    cnt=0
    cnt0=0
    if S[0]>S[1]:
        print("True")
        for i in range(l):
            if i+1<l:
                if S[i]>S[i+1]:
                    p.append(S[i])
                elif S[i]<S[i+1]:
                    if cnt==0:
                        p.append(S[i])
                        q.append(S[i])
                    else:
                        q.append(S[i])
                    cnt=cnt+1
            elif i+1==l:
                if S[i-1]>S[i]:
                    p.append(S[i])
                elif S[i-1]<S[i]:
                    q.append(S[i])
        print("decreasing sequence 1",p)
        print("increasing sequence 2",q)
    elif q==[]:
            print("True")
            print("decreasing sequence 1",p)
            print("increasing sequence 2",q)
    elif S[0]<S[1]:
        for i in range(l):
            if i+1<l and S[i]<S[i+1]:
                q.append(S[i])
                if cnt0==0:
                    print("True")
                    cnt0=cnt0+1

            elif i+1==l and S[i-1]<S[i]:
                q.append(S[i])
            elif i+1<l and S[i]>S[i+1]:
                print("False")
            elif i+1==l and S[i]>S[i+1]:
                print("False")

        print("decreasing sequence 1",p)
        print("increasing sequence 2",q)
    else:
        print("False")

else:
    print("please enter a number between 1 to 1000!")
