a=str(input("Enter a String"))
splited=a.split(" ")
counted=[]
for i in splited:
    if i not in counted:
        count=splited.count(i)
        print(f'count of {i} is {count}')
        counted.append(i)
