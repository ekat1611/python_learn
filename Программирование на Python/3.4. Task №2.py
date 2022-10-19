original_list = []
all_strings = dict()

with open("/Users/user/Downloads/dataset_3363_3 (1).txt", 'r') as original_file:
    text_original = original_file.readlines()
    for line in text_original:
        original_list.append(line.split())
    for lst in range(len(original_list)):
        for wrd in range(len(original_list[lst])):
            if original_list[lst][wrd].lower() in all_strings:
                all_strings[original_list[lst][wrd].lower()] += 1
            else:
                all_strings[original_list[lst][wrd].lower()] = 1


with open("/Users/user/Downloads/dataset_3363_3 (1).txt", 'w') as new_file:
    total_lst = []
    mx = 0
    for key in all_strings:
        if all_strings[key] > mx:
            mx = all_strings[key]
    for key in all_strings:
        if all_strings[key] == mx:
            total_lst.append(key)
    for key in total_lst:
        new_file.write(key + ' ' + str(mx) + '\n')