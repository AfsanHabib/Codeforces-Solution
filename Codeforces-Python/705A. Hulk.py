#Solved

number = int(input())

word = ['I hate', 'I love']
add_word = ['it', 'that']

answer = list()

for i in range(number):
    if i%2==0:
        answer.append(word[0])
        if number - 1 == i:
            answer.append(add_word[0])
        else:
            answer.append(add_word[1])

    if i%2!=0:
        answer.append(word[1])
        if number - 1 == i:
            answer.append(add_word[0])
        else:
            answer.append(add_word[1])

# print(answer)
print(' '.join(answer))
# print(*answer)
