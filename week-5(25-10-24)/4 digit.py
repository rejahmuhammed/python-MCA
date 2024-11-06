import math
list1=[]
for i in range(1000,2000):
    if math.ceil(math.sqrt(i)) == math.floor(math.sqrt(i)) and i%2==0:
        list1.append(i)
print("List of  even perfect squares : ",list1)
