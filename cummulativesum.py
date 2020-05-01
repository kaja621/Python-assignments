noofele=int(input("enter no of elements between -1000 to 1000 = "))
lst=[]
for i in range(0,noofele):
    ele=int(input())
    lst.append(ele)
    if ele>-1000 and ele<1000:
        print(lst)
    else:
        lst.remove(ele)
        noofele-=1
        
lst1=[lst[0]]
print(lst1)
for i in range(0,noofele):
    if i<(noofele-1):
         sum=lst1[i]+lst[i+1]
         if sum>=0:
             lst1.append(sum)
             print(lst1)
             
         else:
             print("further sum is negative")
    else:
        print("program completed")
    
    
  
  
        
