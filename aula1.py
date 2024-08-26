# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#regex-howto
import re

# findall search sub
# compile

my_string = "This is a regular expression test"
print(re.search(r'test',my_string))
print(re.findall(r'test',my_string))
print(re.sub(r'test','testing',my_string,count=1))

regexp = re.compile(r'test')
print(regexp.search(my_string))
print(regexp.findall(my_string))
print(regexp.sub('testing ok',my_string))

