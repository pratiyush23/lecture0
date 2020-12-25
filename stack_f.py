from stack_using_array2 import stack
s = stack
s.push(20)
s.push(10)
s.push(30)
s.push(50)

while s.isEmpty() is False:
    print(s.pop())

print(s.top())