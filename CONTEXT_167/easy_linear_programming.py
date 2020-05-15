A, B, C, K = map(int,input().split())

def calculate(a,b,c,k):
    if k<= a+b:
        if k <= a:
            print(k)
        else:
            print(a)
    else:
        print(a - (k - (a+b)))

calculate(A,B,C,K)