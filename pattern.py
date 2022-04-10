# с символами
# letters=input()
# count_max_letter=[0,0]
# max_letter=[letters[0],letters[0]]
# for letter in letters:
#    if letter==max_letter[1]:
#       count_max_letter[1]+=1
#       if count_max_letter[1]>count_max_letter[0]:
#          count_max_letter[0]=count_max_letter[1]
#          max_letter[0]=max_letter[1]
#    else:
#       count_max_letter[1]=1
#       max_letter[1]=letter
# print(count_max_letter[0],max_letter[0])

# hhhhhhhgggggggfhhhh



# со словами
input = 'I love you I love you'
start_list = input + ' '
list_test = input.split()

for i in range(len(list_test)):
    list_test[i] = list_test[i] + ' '

total_count = 1
total_pattern = ''

def test(index):
    global total_pattern
    global total_count
    pattern = list_test[index]
    count = 1
    for i in list_test[index+1:]:
        count = start_list.count(pattern+i)
        if count > 1:
            pattern += i
        else:
            break
    if len(pattern) > len(total_pattern) and start_list.count(pattern) > total_count:
        total_count = start_list.count(pattern)
        total_pattern = pattern

for i in range(len(list_test)):
    test(i)

for j in set(list_test):
    if list_test.count(j) > total_count:
        total_count = list_test.count(j)
        total_pattern = j
print(total_count)
print(total_pattern)