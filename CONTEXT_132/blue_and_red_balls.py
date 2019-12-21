from scipy import misc

def cnk(n,k):
    return misc.comb(n,k,exact=True)


# import scipy.special
# def cnk(n,k):
#     return int(scipy.special.comb(n,k))

def calculate(n,k):
    # 1. 在n+1个缝隙上，选择i个地方 Cn+1,i

    # 2. 在i个地方，放入k个球 C(k-1),(i-1)

    for i in range(1,k+1):

        a1 = cnk(n-k+1,i)
        a2 = cnk(k-1,i-1)
        print((a1 * a2) % (1000000000+7))


S = input().split(" ")

N = int(S[0])
K = int(S[1])

calculate(N,K)