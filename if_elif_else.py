#find the largest number of three
a=10
b=20
c=30
if a>b and a>c:
    print(f"{a} is largest number")
elif b>c:
    print(f"{b} is largest number")
else:
    print(f"{c} is largest number")
#check whether leep year or not
year=int(input("Enter a Year:"))
if (year % 4 ==0) and (year % 100!=0):
    print(f"{year} is leep year")
elif (year % 400==0):
    print(f"{year} is leep Year")
else:
    print(f"{year} is not a leep year")


