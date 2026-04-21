#print multiplication Tables
a=0
c=int(input("Enter a starting number:"))
d=int(input("Enter a ending number:"))
for i in range(c,d):
    for j in range(1,11):
        print(i,"x",j,"=",j*i)
        a+=1



