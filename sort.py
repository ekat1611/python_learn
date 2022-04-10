array = [5,2,6,8,3,7,10]


# быстрая сортировка
def quicksort(list):
    if len(list) < 2:
        return list

    curr = list[0]

    min = [i for i in list[1:] if i < curr]
    max = [i for i in list[1:] if i >= curr]

    return quicksort(min) + [curr] + quicksort(max)


# сортировка поиском наименьшего элемента
def findSmallest(list):
    index = 0
    for i in range(len(list)):
        if list[i] < list[index]:
            index = i
    return index

def selectsort(list):
    res_list = []
    for i in range(len(list)):
        smallest = findSmallest(list)
        res_list.append(list.pop(smallest))
    return res_list


# сортировка вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
for i in range(len(arr)):
    print (arr[i],end=' ')


# сортировка пузырьком
n = int(input())
m = list(map(int,input().split()))
count = 0
for i in range(n-1):
    for j in range(n-i-1):
        if m[j] > m[j+1]:
            count+=1
            m[j],m[j+1] = m[j+1],m[j]
print(*m)
print(count)