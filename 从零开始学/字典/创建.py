d1={'name':'Mike'}
print(d1)
print(d1['name'])
d2=dict(name='jack')
print(d2)
print(d2['name'])

d1.clear()
print(d1)

d3=d2.copy()
print(d3)

seq=('name','value')
d4=dict.fromkeys(seq)
print(d4)

d5=dict.fromkeys(seq,10)
print(d5)

print(d5.get('name'))

print('name' in d5)

print(d5.items())

print(d5.keys())
print(d5.values())


