def print_goods(*args,**kwargs):
    number = 1
    for i in args:
        if isinstance(i,str) and len(i) != 0:
            print(f'{number}. {i}')
            number += 1
        else:
            continue
    if number == 1:
        print('Нет товаров')


print_goods([], {}, 1, 2)



