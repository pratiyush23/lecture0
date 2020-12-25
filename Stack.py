from stack_usingLL import stack
s = stack()
s.push(40)
s.push(50)
s.push(60)
s.push(70)
s.push(80)

while s.isEmpty() is not True:
    print(s.pop())

s.top()
