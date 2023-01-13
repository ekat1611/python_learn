s, a, b = input(), input(), input()
count = 0
while count < 1000 and a in s:
    s = s.replace(a, b)
    count += 1

print(count) if count < 1000 else print("Impossible")