input_string = input()
n = input_string.split()

sum_even = 0
sum_odd = 0
for i in n:
    if n(i)%2==0:
        sum_even = sum_even+int(i)
    else:
        sum_odd= sum_odd+int(i)
print(sum_even,sum_odd)
