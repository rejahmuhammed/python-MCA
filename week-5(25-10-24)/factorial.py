num=int(input("enter a number "))

factorial=1

if num < 0:
    print("factorial does not exsist for negative number")
elif num ==0:
    print("the factorial of 0 is 1")
else:
    for i in range(1,num + 1):
        factorial = factorial*i
    print(f"the factorail of {num} is {factorial}")
    
        
