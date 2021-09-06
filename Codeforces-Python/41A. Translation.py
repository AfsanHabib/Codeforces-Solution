
#Solved

word=input()
r_word=input()

length=len(word) 
#Strings reversed using Slicing Method
reverse_word=word[length::-1]

if r_word == reverse_word:
    print("YES")
else:
    print("NO") 