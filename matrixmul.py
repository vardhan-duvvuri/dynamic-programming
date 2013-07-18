n=int(raw_input("Enter how many matrices do u want to multiply : "))
print "Enter dimensions for %s matrices : "%n
p=[]
for i in range(0,n+1):
    x=int(raw_input())
    p.append(x)
n = len(p)-1
c = [[]]*(n)
c = [[0]*(n) for x in c]
m = [[]] * (n)
m = [[-1]*(n) for x in m ]
for i in xrange(0, n):
    c[i][i] = 0
for l in range(1,n):
    for i in range(0,n-l):
        j=i+l
        m[i][j]=i
        c[i][j]=99999999999
        if j == i+1:
            c[i][j]=p[i]*p[i+1]*p[i+2]
        else:
            for k in range(i,j):
                value=c[i][k]+c[k+1][j]+p[i]*p[k+1]*p[j+1]
                if value < c[i][j]:
                    c[i][j]=value
                    m[i][j]=k
print "minimum no.of operaations are : "
print c[0][n-1]
def parent(m,s,e):
    if s == e:
        print "A%d"%s,
    else:
        print "(",
        parent(m,s,m[s][e])
        print ".",
        parent(m,m[s][e]+1,e)
        print ")",
print "The paranthesizations : ",
parent(m,0,n-1)
