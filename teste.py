import re

sentance = 'Most Popular Covers | \ / Boyce Avenue'

res = re.sub('[!,*)@#%(&$_?.^|/\\\]', '', sentance)

print(res)