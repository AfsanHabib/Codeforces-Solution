word = input()

upper=0
lower=0


for i in range(len(word)):
      #to lower case letter
      if(word[i]>='a' and word[i]<='z'):
          lower+=1
      #to upper case letter
      elif(word[i]>='A' and word[i]<='Z'):
          upper+=1

          
if(upper>lower):
    #The upper() method converts all uppercase characters in a string into Uppercase 
    print(word.upper())
else:
    #The lower() method converts all uppercase characters in a string into lowercase 
    print(word.lower())
    




