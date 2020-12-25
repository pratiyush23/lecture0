num = int(input())
d = 2
flag = False
while d<num:
    if num%d==0:
        flag = True
        # break
    d = d+1

if flag==True:
    print("Not prime")
else:
    print("Prime")