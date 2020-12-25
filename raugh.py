# if True or True:
#     if False and True or False:
#         print('A')
#     elif False and False or True and True:
#        print('B')
#     else:
#       print('C')
# else:
#      print('D')

# i=1
# while i<3:
#     j=1
#     while j<5:
#         if j==3:
#             break
#         print(j,end="")
#         j = j + 1
#     i = i + 1

# i=1
# while i<5:
#     if i == 6:
#         break
#     print(i,end=" ")
#     i = i + 1
# else:
#     print("else will also be printed")

# i=1
# while i<5:
#     if i == 3:
#         break
#     print(i,end="")
#     i = i + 1
# else:
#     print("Else is also printed")

# i=1
# while i<5:
#     if i==3:
#             continue
#     print(i,end=" ")
#     i = i + 1

i=1
while i<3:
    j=0
    while j<5:
        j = j +1
        if j==3:
            continue
        print(j,end=" ")
    i = i +1