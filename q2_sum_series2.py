def sum_series2(i):
    a=1
    b=3
    c=0
    for i in range(1,m+1):
        c=c+a/b
        a=a+1
        b=b+2
    print(c)
m=int(input())
sum_series2(m)
