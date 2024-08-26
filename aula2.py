# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#regex-howto

# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# | OU
# . Qualquer caractere (com exceção da quebra de linha)
# [] conjunto de caracteres

import re

text = """
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
"""
print(re.findall('João|Maria',text))
print(re.findall('João|Maria|ad.ltos',text)) # . Qualquer coisa
print(re.findall('[Jj]oão|[Mm]aria',text)) # J ou j
print(re.findall('[a-z]aria',text)) # Qualquer letra de a-z
print(re.findall('[a-zA-Z]aria',text)) # Qualquer letra de a-z ou de A-Z
print(re.findall('[a-zA-Z0-9]aria',text)) # Qualquer letra de a-z ou de A-Z ou 0-9
print(re.findall('[a-zA-Z0-9]oão',text)) # Qualquer letra de a-z ou de A-Z ou 0-9
print(re.findall('joÃO| mAriA',text, flags=re.IGNORECASE)) # flag Ignore cae
