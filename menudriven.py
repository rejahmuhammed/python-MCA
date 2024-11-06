n=int(input("Enter the size of list :"))
list=[]
for i in range(1,n+1):
    num=int(input(f"Enter the element {i} : "))
    list.append(num)
print('list = ',list)
while True:
    print("\nMenu:")
    print("1. Find the greatest and lowest number")
    print("2. Sort the list in ascending order")
    print("3. Create a list of even numbers")
    print("4. Exit")
 
    choice = input("Enter your choice from 1 to 4 : ")
 
    if choice == '1':
        print("Greatest number:", max(list))
        print("Lowest number:", min(list))
 
    elif choice == '2':
        print("Sorted list:", sorted(list))
 
    elif choice == '3':
        even_numbers = []
        for num in list:
            if num % 2 == 0:
                even_numbers.append(num)
n=int(input("Enter the size of list :"))
list=[]
for i in range(1,n+1):
    num=int(input(f"Enter the element {i} : "))
    list.append(num)
print('list = ',list)
while True:
    print("\nMenu:")
    print("1. Find the greatest and lowest number")
    print("2. Sort the list in ascending order")
    print("3. Create a list of even numbers")
    print("4. Exit")
 
    choice = input("Enter your choice from 1 to 4 : ")
 
    if choice == '1':
        print("Greatest number:", max(list))
        print("Lowest number:", min(list))
 
    elif choice == '2':
        print("Sorted list:", sorted(list))
 
    elif choice == '3':
        even_numbers = []
        for num in list:
            if num % 2 == 0:
                even_numbers.append(num)
        print("List of even numbers:", even_numbers)
 
    elif choice == '4':
        break
 
    else:
        print("Invalid choice. Please choose a number from 1 to 4.")

