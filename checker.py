from random import randint
n=int(raw_input("Enter the size of the checker board : "))
d = [[]]*(n)
d = [[0]*(n) for x in d]
p = [[]]*(n)
p = [[0]*(n) for x in p]
w = [[]]*(n)
w = [[0]*(n) for x in w]
for i in range(0,n-1):
    for j in range(0,n):
        p[i][j]=randint(-5,5)
for i in range(n-2,-1,-1):
    for j in range(0,n):
        if j == 0:
            val1=p[i][j]+d[i+1][j]
            val2=p[i][j]+d[i+1][j+1]
            if val1>val2:
                d[i][j]=val1
                w[i][j]=j
            else:
                d[i][j]=val2
                w[i][j]=j+1
        elif j == n-1:
            val1=p[i][j]+d[i+1][j-1]
            val2=p[i][j]+d[i+1][j]
            if val1>val2:
                d[i][j]=val1
                w[i][j]=j-1
            else:
                d[i][j]=val2
                w[i][j]=j
        else:
            val1=p[i][j]+d[i+1][j]
            val2=p[i][j]+d[i+1][j-1]
            val3=p[i][j]+d[i+1][j+1]
            if val1>val2 and val1>val3:
                d[i][j]=val1
                w[i][j]=j
            elif val2>val1 and val2>val3:
                d[i][j]=val2
                w[i][j]=j-1
            else:
                d[i][j]=val3
                w[i][j]=j+1

s=int(raw_input("Enter the cell to find max. profit : "))
for i in p:
    print i
print ""
print ""
for i in d:
    print i
print ""
print ""
for i in w:
    print i
print ""
print ""
print "Max Profit of that cell is : "
print d[0][s]
def parent(w,i,j):
    if i!=n-1:
        print w[i][j],
        print '<-----',
        parent(w,i+1,w[i][j])
    else:
        exit
print "The path for that cell is : "
parent(w,0,s)
