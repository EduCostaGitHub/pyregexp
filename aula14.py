# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#regex-howto

# https://regex101.com/r/wjfSus/1/

import re
from pprint import pprint


string = '''
Válidos
0.0
00.00
000.000
+0.0
-00.00
+000.000
10
50
8.5
-8.5
+10.5005412136
1231345458.54654564
-133215646589.6543215648978977
+1.11123123
-0.154987
1.121654987
10.123
10.1
-1.1

Inválidos
10..2
++1213
--1235050
.124546
-.1231324
10.
.1
.10
10.
+10.
-10.
5a
b5
'''

def is_float(value) -> bool:
    return bool(re.search(r'^[+-]?\d+(?:\.\d+)?$',value)) # (?:) -> Não grava o grupo

def is_int_(value) -> bool:
    return bool(re.search(r'^[+-]?\d+$',value)) # (?:) -> Não grava o grupo

#print(is_float('10.5'))

while True:    
    num: str = input('Introduza um valor:')
    print(is_int_(num))
    print(is_float(num))

    if is_int_(num):
        num = int(num) 
        print(f'O Número {num} foi convertido para int')
        continue

    if is_float(num):
        num = float(num)
        print(f'O Númeoro {num} foi convertido para float')
        continue

