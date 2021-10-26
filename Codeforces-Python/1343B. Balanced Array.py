# Solved

test_case=int(input())

for i in range(test_case):
    num=int(input())

    if (num//2)%2==1:
        print('NO')

    else:
        print('YES')

        for j in range(num//2):
            print(2*(j+1))

        for j in range(num//2-1):
            print(2*(j+1)-1)

        print(num-1+num//2)