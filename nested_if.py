#find Largest of three numbers
a=10
b=15
c=20
if a>b:
    if a>c:
        print(f"{a} is largest number")
    else:
        print(f"{c} is largest number")
else:
    if b>c:
        print(f"{b} is largest number")
    else:
        print(f"{c} is largest number")