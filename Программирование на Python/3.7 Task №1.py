results = {}


def add_result(dct, player, own_points, contribute_points):
    if player not in dct:
        dct[player] = [0, 0, 0, 0, 0]
    dct[player][0] += 1
    dct[player][1] += own_points > contribute_points
    dct[player][2] += own_points == contribute_points
    dct[player][3] += own_points < contribute_points
    dct[player][4] += 3 * (own_points > contribute_points) + (own_points == contribute_points)


for i in range(int(input())):
    result = input().split(';')
    add_result(results, result[0], int(result[1]), int(result[3]))
    add_result(results, result[2], int(result[3]), int(result[1]))

for result in results:
    print(result.join(':'), *results[result])
