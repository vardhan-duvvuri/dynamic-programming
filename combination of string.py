def string(a,b,d):
    m=len(a)
    n=len(b)
    k=len(d)
    c = [[]]*(n+1)
    c = [[0]*(m+1) for x in c]
    if k != m+n:
        return 0
    for i in range(0,n+1):
        for j in range(0,m+1):
            if i == 0 and j == 0:
                c[i][j] = 1
            elif i == 0 and a[j-1] == d[i+j-1]:
                c[i][j] = c[i][j-1]
            elif j == 0 and b[i-1] == d[i+j-1]:
                c[i][j] = c[i-1][j]
            elif a[j-1] != d[i+j-1] and b[i-1] != d[i+j-1]:
                c[i][j] =0
            elif a[j-1] == d[i+j-1] and b[i-1] != d[i+j-1]:
                c[i][j]=c[i][j-1]
            elif a[j-1] != d[i+j-1] and b[i-1] == d[i+j-1]:
                c[i][j]=c[i-1][j]
            elif a[j-1] == d[i+j-1] and b[i-1] == d[i+j-1]:
                c[i][j]=c[i-1][j] or c[i][j-1]
    print c
    return c[n][m]
if __name__ == "__main__":
    s1=raw_input("Enter String X : ")
    s2=raw_input("Enter String Y : ")
    s3=raw_input("Enter String z : ")
    p = string(s1,s2,s3)
    if p == 0:
        print "Invalid String"
    else:
        print "Valid String"
