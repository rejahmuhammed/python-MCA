list1=[]
size=int(input("Enter number of words : "))
for i in range(size):
    words=input(f"Enter word {i+1} : ")
    list1.append(words)
longest_word=max(list1,key=len)
print("word list : ",list1)
print("Longest word : ",longest_word)
