test_cese = int(input())
for i in range(test_cese):
    des = input()
    word = input()
    ans = 0
    for j in range(len(word)-1):
        ans += abs(des.index(word[j])-des.index(word[j+1]))
    	# print([j])
    print(ans)
