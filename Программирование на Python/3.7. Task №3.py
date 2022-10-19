words = [input().lower() for i in range(int(input()))]
test = set()
total_errors = [[test.add(word.lower()) for word in string if word.lower() not in words] for string in [input().split() for j in range(int(input()))]]
print(*test, sep='\n')