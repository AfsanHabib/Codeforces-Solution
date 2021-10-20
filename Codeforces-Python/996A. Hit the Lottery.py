# Solved


num=int(input())

ans=num//100
rem=num%100

ans+=rem//20
rem=rem%20

ans+=rem//10
rem=rem%10

ans+=rem//5
rem=rem%5

ans+=rem//1
rem=rem%1

print(ans)