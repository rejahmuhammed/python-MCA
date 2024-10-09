str=(input("Enter a String"))
a=[]
vowels=['A','a','E','e','I','i','O','o','U','u']
for i in str:
    if(i in vowels):
            a.append(i)
print("The Vowels are",a)
