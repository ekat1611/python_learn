string = input().lower().split()
total = {}
for i in string:
    if i not in total:
        total[i] = 1
    else:
        total[i] += 1

for value in total.items():
    print(*value)



# s=input().lower().split()
# [print(i, s.count(i)) for i in set(s)]



# text = input().lower().split()
# words = set(text)
# for word in words:
#     print(word, text.count(word))