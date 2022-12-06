n, k = map(int, input().split())


def x(n, k):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return x(n - 1, k) + x(n - 1, k - 1)
        # x(2,2) + (2,1)
        # x(1,2) + (1,1) + (1,1) + (1,0)
        # 0 + (0,1) + (0,0) + (0,1) + (0,0) + 1
        # 0 + 0 + 1 + 1 + 0 + 1 = 3


print(x(n, k))