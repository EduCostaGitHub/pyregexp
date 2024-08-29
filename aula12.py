# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#regex-howto


# https://regex101.com/r/0OM1oz/1/

import re
from pprint import pprint

texto = '''
(21) 9 8852-5214
(11)9955-1231
(11)            9955-1231
(35) 9 9975-4521
(31) 3851-2587
9 8571-5213
1234-5647
'''

regexp = re.compile(r'^((\(\d{2}\)\s)(9\s)(\d{4}-\d{4}))$', flags=re.MULTILINE)

for tel in regexp.findall(texto):
    tel_completo, ddd, nove, num = tel
    print(tel_completo)
