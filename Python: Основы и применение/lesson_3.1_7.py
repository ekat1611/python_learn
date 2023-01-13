s, t = input(), input()
count = 0
while len(s) > 0:
    if s.startswith(t):
        count += 1
    s = s[1:]
print(count)
