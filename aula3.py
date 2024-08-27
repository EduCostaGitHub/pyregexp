# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#regex-howto

# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# | OU
# . Qualquer caractere (com exceção da quebra de linha)
# [] conjunto de caracteres

# Meta caracteres: ^ $ ( )
# * 0 ou n
# + 1 ou n {1,}
# ? 0 ou 1
# {n}
# {min, max}
# {10,} 10 ou mais
# {,10} De zero a 10
# {10} Especificamente 10
# {5,10} De 5 a 10
# ()+ [a-zA-Z0-9]+

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

print(re.findall(r'jo+ão',text, flags=re.I))
print(re.findall(r'jo+ão+',text, flags=re.I))
print(re.sub(r'jo+ão+','Eduardo',text, flags=re.I))

print(re.findall(r'jo?ão+',text, flags=re.I))
print(re.findall(r'jo{1,}ão{1,}',text, flags=re.I))

print(re.findall(r've{3}m{1,2}',text, flags=re.I))

text2 = "João ama ser amado"
print(re.findall(r'ama[do]*',text2,flags=re.I))
print(re.findall(r'ama[do]{0,2}',text2,flags=re.I))



