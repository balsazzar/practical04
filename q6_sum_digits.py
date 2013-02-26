def sum_digits(n):
    m=10
    a=0
    while n/m>=1:
        b=n%m
        a=a+((b-(n%(m/10)))/(m/10))
        m=m*10
    c=(n-n%(m/10))/(m/10)
    print(a+c)

n=int(input("Enter number: "))
sum_digits(n)
    
