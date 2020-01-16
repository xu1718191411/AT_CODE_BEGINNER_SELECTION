def calculate(n,m,arr,p):
    total = 0
    for i in range(2**n):
        #某一种情况

        check = [False for i in range(m)]
        for indexOfBlub in range(len(arr)):
            # 第几个灯泡
            onNumOfTheBlub = 0
            for indexOfSwitch in range(len(arr[indexOfBlub])):
                if i >> (arr[indexOfBlub][indexOfSwitch] - 1) & 1:
                    onNumOfTheBlub += 1

            # 该灯泡所有的switch都循环结束以后，统计on的数量是否和给定的一样

            if onNumOfTheBlub % 2 == p[indexOfBlub]:
                check[indexOfBlub] = True

        if all(check):
            total += 1

    return total

S = input()
S = S.split(" ")
n = int(S[0])
m = int(S[1])
inputArr = []
for i in range(m):
    S = input()
    inputArr.append([int(s) for s in S.split(" ")][1:])

S = input()
inputP = [int(s) for s in S.split(" ")]

res = calculate(n,m,inputArr,inputP)
print(res)