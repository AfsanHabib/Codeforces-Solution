#Solved

for i in range(int(input())):
    
    x=0
    y=0
    

    a=input()
    
    if int(a)%2==0:
        print(0)
    
    elif (int(a[::-1])%2==0):
        print(1)
    
    else:
        ev=0
        odd=0
        for j in range(len(a)):
            
            if (int(a[j]))%2==0:
                ev+=1
            else:
                odd +=1
                
        if ev>=1:
            print(2)
        else:
            print(-1)