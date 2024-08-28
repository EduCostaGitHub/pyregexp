# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#regex-howto

# Meta caracteres: ^ $ ( )
# * 0 ou n
# + 1 ou n {1,}
# ? 0 ou 1

import re

text = """
<p> Phrase 1 </p><p> Phrase 2 </p><p> Phrase 3 </p><div> Phrase 4 </div>
"""

print(re.findall(r'<[dpiv]{1,3}>.*<\/[dpiv]{1,3}>',text)) #greedy
print(re.findall(r'<[dpiv]{1,3}>.*?<\/[dpiv]{1,3}>',text)) #non greedy




