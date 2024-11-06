num=int(input("Enter Number : "))
list1=[]             
for i in range(1,num+1):
    if num%i==0:
        list1.append(i)              
print("factors are : ",list1)
