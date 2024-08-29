# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#regex-howto

# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# | OU
# . Qualquer caractere (com exceção da quebra de linha)
# [] conjunto de caracteres

# \w -> [a-zA-Z0-9À-ú_]
# \w -> [a-zA-Z0-9_] -> re.A
# \W -> [^a-zA-Z0-9Á-ú_]
# \w -> [^a-zA-Z0-9_] -> re.A
# \d -> [0-9]
# \D -> [^0-9]
# \s -> [ \r\n\f\t]
# \b -> borda
# \B -> não borda


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
print(re.findall(r'\w+', text))
print(re.findall(r'\w+', text, flags=re.A))

print(re.findall(r'\W+', text))
print(re.findall(r'\W+', text, flags=re.A))

print(re.findall(r'\d+', text, flags=re.I))
print(re.findall(r'\D+', text, flags=re.I))

print(re.findall(r'\s+', text, flags=re.I))
print(re.findall(r'\S+', text, flags=re.I))

print(re.findall(r'\bflo\w+', text, flags=re.I))
print(re.findall(r'\w+e\b', text, flags=re.I))

print(re.findall(r'\b\w{4}\b', text, flags=re.I))
