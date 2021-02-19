a = int(input("first number:"))
b = int(input("second number:"))
c = int(input("third number:"))
 
if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)