dct = {
    "1": [0, 0], "2": [0, 0], "3": [0, 0], "4": [0, 0], "5": [0, 0],
    "6": [0, 0], "7": [0, 0], "8": [0, 0], "9": [0, 0], "10": [0, 0], "11": [0, 0]
}
original_lst = []


def avg_growth(lst):
        dct[lst[0]][0] += int(lst[2])
        dct[lst[0]][1] += 1


with open('/Users/user/Downloads/dataset_3380_5 (3).txt', 'r') as file:
    text_original = file.readlines()
    for line in text_original:
        original_lst.append(line.split('\t'))
    for lst in original_lst:
        avg_growth(lst)

with open('/Users/user/Downloads/dataset_3380_5 (3).txt', 'w') as file:
    for key in dct:
        file.write(key + ' ' + str(dct[key][0] / dct[key][1]))
        file.write('\n')