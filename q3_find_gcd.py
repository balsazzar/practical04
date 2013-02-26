def gcd(m, n):
    if m%n==0:
        print(n)
    else:
        print(gcd(n, m%n))

m=int(input())
n=int(input())
gcd(m,n)
