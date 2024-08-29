# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#regex-howto

# Meta caracteres: ^ $ ( )
# * 0 ou n
# + 1 ou n {1,}
# ? 0 ou 1

# ()    \1
# () () \1 \2
# (())() \1 \2 \3

import re
from pprint import pp, pprint


text = """
<p> Phrase 1 </p><p> Phrase 2 </p><p> Phrase 3 </p><div> Phrase 4 </div>
"""
print(re.findall(r'<[dpiv]{1,3}>.*?<\/[dpiv]{1,3}>', text))  # non greedy /lazy
print()

tags = re.findall(r'(<([dpiv]{1,3})>(.*?)<\/\2>)', text)  # non greedy /lazy

for tag in tags:
    um, dois, tres = tag
    print(um, dois, tres)

print()
tags = re.findall(r'<([dpiv]{1,3})>(.*?)<\/\1>', text)  # non greedy /lazy
pprint(tags)

print()
tags = re.findall(r'<([dpiv]{1,3})>(?:.*?)<\/\1>', text)  # non greedy /lazy
# non greedy /lazy
tags2 = re.findall(r'<(?P<tag>[dpiv]{1,3})>(?:.*?)<\/(?P=tag)>', text)
pprint(tags)
pprint(tags2)

print()
cpf = '147.852.963-12'
pprint(re.findall(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}', cpf))

print()
cpf = '147.852.963-12'
pprint(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))

print()
print(re.sub(r'(<(.+?)>)(.+?)(<\/\2)', r'\1"""\3"""\4', text))
