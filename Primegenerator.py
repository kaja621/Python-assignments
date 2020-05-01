"""Peter wants to generate some prime numbers for his cryptosystem. Help him! Your task is to generate all prime numbers between two given numbers!

Input Format
The input begins with the number t of test cases in a single line (t<=10). In each of the next t lines, there are two numbers m and n separated by a space.

Constraints
1 <= m <= n <= 1000000000 n-m<=100000

Output Format
For every test case print all prime numbers p such that m <= p <= n, all primes per line, test cases separated by an empty line.

Sample Input
2
1 10
3 5
Sample Output
2 3 5 7
3 5
Hint:
The basic idea of the program is to put a loop starting from the lower limit till the upper limit of the input and check if the number is prime, if yes print the number. That's the brute force algorithm but this approach will give time limit exceed.

An Efficient algorithm is SOE(Sieve of Eratosthenes)

Create a list of consecutive integers from 2 to n: (2, 3, 4, …, n).
Initially, let p equal 2, the first prime number.
Starting from p, count up in increments of p and mark each of these numbers greater than p itself in the list. These numbers will be 2p, 3p, 4p, etc.; note that some of them may have already been marked.
Find the first number greater than p in the list that is not marked. If there was no such number, stop. Otherwise, let p now equal this number (which is the next prime), and repeat from step 3.
"""
t=int(input("Enter the number of test case :"))
if t<=10:
    for i in range(0,t):
        x=int(input("enter first number :"))
        y=int(input("Enter last number :"))
        if x>=1 and y<=1000000000 and y-x<=100000:
            if x==1:
                m=2
            else:
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
                print(" ")
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
            for i in lst:
                if i not in lst1:
                    lst2.append(i)
                    print(i)
        else:
            print("wrong input range!")

else:
    print("Enter test case number <=10!")
