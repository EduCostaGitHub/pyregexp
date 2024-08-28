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
from pprint import pprint


text = """
<p> Phrase 1 </p><p> Phrase 2 </p><p> Phrase 3 </p><div> Phrase 4 </div>
"""
print(re.findall(r'<[dpiv]{1,3}>.*?<\/[dpiv]{1,3}>', text))  # non greedy /lazy
print()
tags = re.findall(r'(<([dpiv]{1,3})>.*?<\/\2>)', text)  # non greedy /lazy

for tag in tags:
    um, dois = tag
    print(um)
    print(dois)
