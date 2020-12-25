start= int(input())
end = int(input())
stepsize = int(input())

for i in range(start,end+1,stepsize):
    c = (i-32)*(5/9)
    print(i," ",int(c))
