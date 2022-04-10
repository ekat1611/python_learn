def fact(n):
    pr = 1
    for i in range(1,n+1):
        pr *= i
        yield pr
        print(pr**2)

for i in fact(2):
    print(i,end = ' ')


# def fact(n):
#     pr = 1
#     a = []
#     for i in range(1,n+1):
#         pr *= i
#         a.append(pr)
#     return a
# print(fact(10))