
integer = input()
money = list(map(int,input().split()))

length = 1
arr = []

if len(money)> 1:
    for i in range(len(money)-1):
        if money[i] <= money[i+1]:
            length += 1
            if i == len(money)-2:
                arr.append(length)
        else:
            arr.append(length)
            length = 1
    print(max(arr))
else:
    print(length)

