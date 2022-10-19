# commands = [input().split() for i in range(int(input()))]
# start_point = [0, 0]
#
# for command in commands:
#     if command[0] == 'юг':
#         start_point[1] -= int(command[1])
#     if command[0] == 'север':
#         start_point[1] += int(command[1])
#     if command[0] == 'запад':
#         start_point[0] -= int(command[1])
#     if command[0] == 'восток':
#         start_point[0] += int(command[1])
#
# print(*start_point)


x, y = 0, 0
moves = {
	'север'  : lambda d: (x, y + d),
	'юг'     : lambda d: (x, y - d),
	'запад'  : lambda d: (x - d, y),
	'восток' : lambda d: (x + d, y)
}

n = int(input())
for _ in range(n):
	direction, step = input().split()
	x, y = moves[direction](int(step))

print(x, y)