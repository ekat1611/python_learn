import os.path
lst = [current_dir for current_dir, dirs, files in os.walk('main') for file in files if '.py' in file]

with open('answer.txt', 'w') as answer:
    for i in sorted(set(lst)):
        answer.write(i + '\n')

