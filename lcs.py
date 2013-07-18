def lcs(x1,y1):
    for i in range(1,n+1):
        c[i][0] = 0
    for j in range(0,m+1):
        c[0][j] = 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if y1[i-1] == x1[j-1]:
                c[i][j] = c[i-1][j-1]+1
                cfrom[i][j]="c"
            else:
                val1=c[i-1][j]
                val2=c[i][j-1]
                if val1 > val2:
                    c[i][j] = val1
                    cfrom[i][j]="u"
                else:
                    c[i][j] = val2
                    cfrom[i][j]="l"
    print "The longest common subsequence size is : "
    print c[n][m]
def lcs_string(cfrom,y1,j,i):
    global k
    if cfrom[j][i] == 'c':
        k+=(y1[j-1])
        lcs_string(cfrom,y1,j-1,i-1)
    elif cfrom[j][i] == 'u':
        lcs_string(cfrom,y1,j-1,i)
    elif cfrom[j][i] == 'l':
        lcs_string(cfrom,y1,j,i-1)
    else:
        exit
    return k
if __name__ == "__main__":
    x1=raw_input("Enter string X : ")
    y1=raw_input("Enter string Y : ")
    m=len(x1)
    n=len(y1)
    c=[[]]*(n+1)
    c=[[0] * (m+1) for x in c]
    cfrom=[[]]*(n+1)
    cfrom=[[0] * (m+1) for x in c]
    lcs(x1,y1)
    global k
    k=""
    print "Longest common subsequence is : "
    p=lcs_string(cfrom,y1,n,m)
    print p[::-1]
