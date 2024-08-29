# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#regex-howto

# 0.0.0.0 255.255.255.255
# 025.258.963-10 02525896310

import re
from pprint import pprint

cpf = '025.258.963-10'
cpf_reg_exp = re.compile(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$')
# print(cpf_reg_exp.search(cpf))

ip_reg_exp = re.compile(r'''
    ^
    (?:
        (?:
            25[0-5]| # 250-255
            2[0-4][0-9]| # 200-249
            1[0-9]{2}| # 100-199
            [1-9][0-9]| # 10-99
            [0-9] # 0-9                        
        )
        \.?
    ){4}
    \b
    $            
''', flags=re.X)


for i in range(301):
    ip = f'{i}.{i}.{i}.{i}'
    print(ip, ip_reg_exp.findall(ip))
