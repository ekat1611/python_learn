with open("/Users/user/Downloads/dataset_24465_4.txt", "r") as start_file, open("text.txt", "a") as finish_file:
    for line in reversed(list(start_file)):
        finish_file.write(line)


# with open("/Users/user/Downloads/dataset_24465_4.txt", "r") as start_file, open("text.txt", "a") as finish_file:
#     file_lines = []
#     for line in start_file.readlines():
#         file_lines.append(line)
#     for i in range(len(file_lines)):
#         finish_file.write(file_lines[-i-1])
