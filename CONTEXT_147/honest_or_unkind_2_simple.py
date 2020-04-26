# N = 3
# ARR = [[[2],[3]], [[3],[1]], [[1],[2]]]

# N = 2
# ARR = [[[], [2]], [[], [1]]]


# N = 3
# ARR = [[[2],[]],[[1],[]],[[],[2]]]

N = int(input())
ARR = []
for i in range(N):
    A = int(input())
    X = []
    Y = []
    for j in range(A):
        x, t = map(int, input().split())
        if t == 1:
            X.append(x)
        else:
            Y.append(x)
    ARR.append([X,Y])

def calculate(n,arr):
    result = []
    for i in range(2**n):
        cases = []
        goods = set()
        suspicious = set()
        for j in range(n):
            cases.append(i >> j & 1)
            if i >> j & 1:
                goods.add(j)
            else:
                suspicious.add(j)
        res = judge(arr,cases,goods,suspicious)
        if res:
            result.append(len(goods))

    if len(result) == 0:
        print(0)
    else:
        print(max(result))

def judge(arr,cases,goods,suspicious):
        tempGoods = set()
        tempSuspicious = set()

        if sum(cases) == 0:
            return False

        for index,ca in enumerate(cases):
            if ca == 1:
                for g in arr[index][0]:
                    tempGoods.add(g - 1)
                for s in arr[index][1]:
                    tempSuspicious.add(s - 1)

        if len(list(tempGoods & suspicious)) > 0:
            return False

        if len(list(tempSuspicious & goods)) > 0:
            return False

        return True


calculate(N,ARR)