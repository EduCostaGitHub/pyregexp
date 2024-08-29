# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#regex-howto

# re.A -> ASCII
# re.I -> IGNORECASE
# re.M -> Multiline
# re.S -> Dotall


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

# print(re.findall(r'[a-z0-9]+', text, flags=re.I))
# print(re.findall(r'[a-zA-Z0-9]+', text))
# print(re.findall(r'[a-zA-Z0-9À-ú]+', text))


text = """
131.768.460-53
055.123.060-50
955.123.060-90
"""

print(re.findall(r'\d{3}\.\d{3}\.\d{3}\-\d{2}', text))

print()

text2 = """
131.768.460-53 abc
055.123.060-50
955.123.060-90
"""

print(re.findall(r'\d{3}\.\d{3}\.\d{3}\-\d{2}$', text2, flags=re.M))

print()
text3 = """O João gosta de amar \n e adora ser amado"""

print(re.findall(r'^o.*o$', text3, flags=re.I))

print()
text4 = """O João gosta de amar
E adora ser amado"""

print(re.findall(r'^o.*o$', text4, flags=re.I | re.S))
