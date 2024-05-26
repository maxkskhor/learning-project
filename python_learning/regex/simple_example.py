import re


# pattern object -> method: match, search, findall, finditer
p = re.compile('[a-z]+')

# match object -> method: group, start, end, span
m = p.match('::: message')
m2 = p.search('::: message')

if m:
    print('Match found: ', m.group())
else:
    print('No match')

# findall example
p = re.compile(r'\d+')
p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')

# Module-level functions
print(re.match(r'From\s+', 'Fromage amk'))

# search and replace

p = re.compile('(blue|white|red)')
p.sub('colour', 'blue socks and red shoes')
