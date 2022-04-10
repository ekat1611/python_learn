def gen():
    count = 10
    while count != 0:
        count -= 1
        yield count


# a = gen()
# for i in a:
#     print(i)


b = (i for i in range(10,-1 ,-1))
for i in b:
    print(i)