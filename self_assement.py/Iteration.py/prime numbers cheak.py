num = 7
flag = True

for i in range(2, num):
    if num % i == 0:
        flag = False
        break

if flag and num > 1:
    print("Prime Number")
else:
    print("Not a Prime Number")


   # output: prime number
