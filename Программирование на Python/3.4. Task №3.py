original_lst = []

with open('/Users/user/Downloads/dataset_3363_4 (2).txt', 'r') as original_file:
    original = original_file.readlines()
    for line in original:
        original_lst.append(line.split(';'))

with open('/Users/user/Downloads/dataset_3363_4 (2).txt', 'w') as result_file:
    total_math, total_ph, total_rus = 0, 0, 0
    for string in original_lst:
        result_file.write(str((int(string[1]) + int(string[2]) + int(string[3]))/3) + '\n')
        total_math += int(string[1])
        total_ph += int(string[2])
        total_rus += int(string[3])
    result_file.write(str(total_math/len(original_lst)) + ' ' + str(total_ph/len(original_lst)) + ' ' + str(total_rus/len(original_lst)))