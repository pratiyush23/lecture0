def pallindrome(n):
    sum = 0
    while (n > 0):
        rem = n % 10
        sum = sum * 10 + rem
        n = n // 10
    return sum

num = int(input())

if(num == pallindrome(num)):
    print('true')
else:
    print('false')