N, K = [1000, 8]
DRR = [1, 3, 4, 5, 6, 7, 8, 9]



N, K = [9999, 1]
DRR = [0]


N, K = list(map(int,input().split()))
DRR = list(map(int,input().split()))

def calculate(n, k, drr):
    dislikes = set()

    for i in range(k):
        dislikes.add(drr[i])

    while not condition(n, dislikes):
        n += 1

    print(n)
def condition(n,dislikes):
    arr = list(map(int, str(n)))

    for i in range(len(arr)):
        if  dislikes.__contains__(arr[i]):
            return False
    return True


calculate(N, K, DRR)
