N,K = list(map(int,input().split()))
PRR = list(map(int,input().split()))

# N = 10
# K = 4
# PRR = [17, 13, 13, 12, 15, 20, 10, 13, 17, 11]
#
# N = 5
# K = 3
# PRR = [1, 2, 2, 4, 5]

def calculate(n, k, prr):

    sumarr = []
    for i in range(n):
        if len(sumarr) == 0:
            sumarr.append(prr[0])
        else:
            sumarr.append(sumarr[-1] + prr[i])

    maxSum = []

    for i in range(k-1,n):

        if i - k < 0:
            sss = sumarr[i] - 0
        else:
            sss = sumarr[i] - sumarr[i - k]
        maxSum.append(sss)

    print((k+max(maxSum))/2)


calculate(N, K, PRR)
