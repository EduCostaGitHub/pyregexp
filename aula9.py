# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#regex-howto


import re
from pprint import pp, pprint

texto = '''
ONLINE  192.168.0.1 GHIJK active
OFFLINE  192.168.0.2 GHIJK inactive
OFFLINE  192.168.0.3 GHIJK active
ONLINE  192.168.0.4 GHIJK active
ONLINE  192.168.0.5 GHIJK inactive
OFFLINE  192.168.0.6 GHIJK active
'''

pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(\w+)', texto))
# Positive lookahead
pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?=active)', texto))
# Negative lookahead
pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?!active)', texto))

pprint(re.findall(r'.+', texto))

pprint(re.findall(r'(?=.*[^in]active).+', texto))

print()
# Positive lookbehind
pprint(re.findall(r'(\w+)(?<=ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))
print()
# Negative lookbehind
pprint(re.findall(r'(\w+)(?<!ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))
