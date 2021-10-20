
word_length=int(input())
word=str(input())

word_upper=word.upper()
word_set = set(word_upper)
word_set_len=len(word_set)


if word_set_len>=26:
	print("YES")
else:
	print("NO")

# print(word_lower)
# print(word_upper)

# word_length=int(input())
# word=str(input())

# # word_lower = word.lower()
# word_set = set(word)
# # print(word_set)
# word_set_len=len(word_set)
# # for i in word:
# # 	for j in word_upper:
# # 		if

# if word_set_len>=26:
# 	print("YES")
# else:
# 	print("NO")

# # print(word_lower)
# # print(word_upper)

