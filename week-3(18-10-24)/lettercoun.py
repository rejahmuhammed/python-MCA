lst=[]
sum=0
len= int(input("Enter the size of the list:"))
print(f"Enter {len} First names:")
for i in range(len):
    temp=input()
    lst.append(temp)
for j in lst:
    temp1=j.count('a')
    temp2=j.count('A')
    temp=temp1+temp2
    sum+=temp
print(f"Total no. of 'a'/'A' in the list: {sum}")
