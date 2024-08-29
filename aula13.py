# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#regex-howto


# https://regex101.com/r/W4kRV2/2/
# https://en.wikipedia.org/wiki/List_of_Unicode_characters

import re
from pprint import pprint

senha_forte_regexp = re.compile(
    r'^'
    r'(?=.*[a-z])'
    r'(?=.*[A-Z])'
    r'(?=.*[0-9])'
    r'(?=.*[ -\/:-@[-`{-~])'
    r'.{12,}'
    r'$',
    flags=re.M
)

string = '''
VÁLIDAS
P{H7ta8Z.e{8
[F48ouc-+ZI6
1Q4j}7RbxH]@
3Be6_[s^1NLw
3lC2tXu\Y^0(

SEM MINÚSCULAS
0E\0F4 9A[]A
[3`05E2SA$V!
BI74\1=CX:=9
K3YE5I`0=0`?
3FA>0OV##_40

SEM MINÚSCULAS E NÚMEROS
L{|<JTZ~@|TS
OK\:O_/-P~VZ
[@E-}Z<NQ`YV
`J/{BGYYZ~%`
:?.NJ>}[SRFT

SEM NÚMEROS CARACTERES E MINÚSCULAS
FYOWZKHBWUUG
MQHVZOBVHYXO
GIFSJUFLIHFB
TAUBVONSTAEU
IXLFPXFPFPAA

QUANTIDADE INVÁLIDA (6)
9p\1Ot
_i21Dd
3}rpA2
4D2)hx
3iDg?1
'''
pprint(senha_forte_regexp.findall(string))
