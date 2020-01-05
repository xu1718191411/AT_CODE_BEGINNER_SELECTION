import numpy as np

def calculate(arr,n,k):
    max = 0

    maxSum = min(n,k)
    # A+B的和

    for i in range(0,maxSum+1):

        for l in range(0,i+1):
            larr = arr[:l]
            if i-l == 0:
                rarr = np.array([])
            else:
                rarr = arr[-(i-l):]

            ab = np.concatenate([larr,rarr])

            abs = np.sort(ab,axis=0)

            # 扔东西
            # k - i

            thawMax = (k-i)

            for th in range(thawMax+1):
                abs[:th] = 0
                tmpSum = np.sum(abs,axis=0)

                if tmpSum > max:
                    max = tmpSum


    return int(max)



S = input().split(" ")
N = int(S[0])
K = int(S[1])

arr = [int(s) for s in input().split(" ")]
arr = np.array(arr)

result = calculate(arr,N,K)

print(result)