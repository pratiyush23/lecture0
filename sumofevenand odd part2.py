def pallindrome(n):
    sum = 0
    even = 0
    odd = 0
    while (n > 0):
        rem = n % 10
        if(rem%2==0):
            even = even+rem
        else:
            odd = odd + rem
        n = n // 10
    print(even,"",odd)

num = int(input())
pallindrome(num)

