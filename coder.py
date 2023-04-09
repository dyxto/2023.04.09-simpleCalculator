# 2023-04-09 DYxTO calculator version 1

x = '<first term>'
y = '<second term>'
o = '<operation>'
z = '<solution>'
print(f'\nExpression: {x} {o} {y} = {z}')

x = int(input('Enter first number: '))
y = int(input('Enter second number: '))

o = int(input('Operations:\n \
      (1) addition\n \
      (2) subtraction\n \
      (3) multiplication\n \
      (4) division\n \
    Choose an action: '))

# print(f'*** type of o variable : {type(o)}')

while o not in range(1,4+1):
    o = int(input('Choose an operation: '))

if o == 1:
    o = '+'
    z = x + y
elif o == 2:
    o = '-'
    z = x - y
elif o == 3:
    o = '*'
    z = x * y
elif o == 4:
    o = '÷'
    z = round(x / y, 4)

# print(f'Operation chosen: {o}')
print(f'Expression: {x} {o} {y} = {z}')