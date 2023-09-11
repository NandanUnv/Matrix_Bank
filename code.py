
x = int(input("Enter rows:"))
y = int(input("Enter col:"))
mat=[]
for i in range(0,x):
    a=[]
    for j in range(0,y):
        c = int(input())
        a.append(c)
    mat.append(a)

for i in range(x):
    for j in range(y):
        print(mat[i][j], end=' ')
    print()

d = input("Do you want to hide money in matrix?(y/n):")

if d=='y' or d=='Y':
    ro = int(input("enter row:"))
    co = int(input("enter col:"))

    for i in range(x):
        for j in range(y):
            if(ro-1==i and co-1==j):
                mat[i][j]='x'
                print(mat[i][j],end=' ')
            else:
                print(mat[i][j],end=' ')
        print()
    print("your money is safe at 'x' in matrix")
else:
    print("fine, Thankyou")
