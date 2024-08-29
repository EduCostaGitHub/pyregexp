# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#regex-howto

# Meta caracteres: ^ $ ( )
# * 0 ou n
# + 1 ou n {1,}
# ? 0 ou 1

# ()    \1
# () () \1 \2
# (())() \1 \2 \3

# Meta caracteres:
# ^ -> Começa com
# $ -> Termina com
# [^a-z] -> Negação

import re
from pprint import pp, pprint

print()
cpf = '147.852.963-12'
print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf))
print(re.findall(r'[^a-z]+', cpf))
print(re.findall(r'[^0-9]+', cpf))
