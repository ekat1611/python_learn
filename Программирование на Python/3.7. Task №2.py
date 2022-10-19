start_symbols, finish_symbols = [i for i in input()], [i for i in input()]
dct_for_encode, dct_for_decode = {}, {}
encode_string = input()
decode_string = input()

for i in range(len(start_symbols)):
    dct_for_encode[start_symbols[i]] = finish_symbols[i]
    dct_for_decode[finish_symbols[i]] = start_symbols[i]

for symbol in encode_string:
    print(dct_for_encode[symbol], end='')

print()

for symbol in decode_string:
    print(dct_for_decode[symbol], end='')



