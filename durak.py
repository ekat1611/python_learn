# Напишите программу, которая определяет, бьёт ли одна карта другую.
# Если встречаются две карты одной масти, то побеждает та, у которой выше значение;
# Если карты разных мастей, то карта, имеющая козырную масть, побеждает;
# Если карты разных мастей и нет козырных, то никто не побеждает.
# Формат ввода:
# На первой строке через пробел указываются две карты в формате <значение><масть>,
# а на следующей строке указывается козырная масть.
# Формат вывода:
# Программа должна вывести слово
# First, если первая карта бьёт вторую,
# Second, если вторая карта бьёт первую,
# Error, если ни одна из карт не может побить другую.

cards = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
input_cards = input().split()
current_cards = []
trump_card = input()
for i in range(2):
    for j in range(2):
        if '10' not in input_cards[i]:
            current_cards.append([input_cards[i][j],input_cards[i][-1]])
            break
        else:
            current_cards.append([input_cards[i][j] + input_cards[i][j+1], input_cards[i][-1]])
            break
if current_cards[0][1] == current_cards[1][1]:
    if cards.index(current_cards[0][0]) > cards.index(current_cards[1][0]):
        print('First')
    elif cards.index(current_cards[0][0]) < cards.index(current_cards[1][0]):
         print('Second')
    else:
         print("Error")
else:
     if current_cards[0][1] == trump_card:
         print("First")
     elif current_cards[1][1] == trump_card:
         print('Second')
     else:
         print('Error')


# cards = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# input_cards = input().split()
# current_cards = []
# trump_card = input()
# for i in range(2):
#     for j in range(2):
#         if '10' not in input_cards[i]:
#             current_cards.append([input_cards[i][j],input_cards[i][-1]])
#             break
#         else:
#             current_cards.append(['10', input_cards[i][-1]])
#             break
# if current_cards[0][1] == current_cards[1][1]:
#     if cards.index(current_cards[0][0]) > cards.index(current_cards[1][0]):
#         print('First')
#     elif cards.index(current_cards[0][0]) < cards.index(current_cards[1][0]):
#          print('Second')
#     else:
#          print("Error")
# else:
#      if current_cards[0][1] == trump_card:
#          print("First")
#      elif current_cards[1][1] == trump_card:
#          print('Second')
#      else:
#          print('Error')

print('29002412318224'*2)