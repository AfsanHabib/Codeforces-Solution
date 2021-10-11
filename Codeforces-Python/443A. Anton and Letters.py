# solved

set_of_letters = str(input())

new_set=set()

char_to_replace = {' ': '',
                   ',': '',
                   '}': '',
                   '{': ''}

for key, value in char_to_replace.items():
    set_of_letters = set_of_letters.replace(key, value)

for i in set_of_letters:
	new_set.add(i)

print(len(new_set))