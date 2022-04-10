# put your python code here
dic = {}
name = []
count = int(input())
for i in range(count):
    name.append(input())

for k in range(len(name)):
    if name[k] not in dic:
        dic[name[k]] = 1
        print('OK')
    else:
        print(name[k],dic[name[k]],sep = '')
        dic[name[k]] += 1


print(dic)
print(name)