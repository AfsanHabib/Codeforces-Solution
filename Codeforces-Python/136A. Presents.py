

friends=int(input())
gifts=input().split()
 
for i in range(friends):
    print(gifts.index(str(i+1))+1)