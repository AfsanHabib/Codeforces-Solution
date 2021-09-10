# Solved

string = input()

string_len = len(string)
no_count = 0


for i in string:
    if i == 'H' or i == 'Q' or i == '9':
        print("YES")
        break
    else:
        no_count=no_count+1

if(no_count==string_len):
    print("NO")
