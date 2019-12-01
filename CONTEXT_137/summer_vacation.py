from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def calculate(N,M,arr):
    ret = 0

    j = 0

    res = []

    # 1,2,3,4,5
    #         ↑
    # 4,3,2,1

    # M = 4
    # range(1,5) => 1,2,3,4

    for i in range(1,M+1):
        # i = 1,2,3
        # 比如M=4的话，第三天(最多1天),第二天(最多2天),第一天(最多3天)

        # 记下来循环打工信息资源,以j为标记
        # j为资源编号
        # arr[j][0]为该编号资源的天数


        # 候补的资源，满足所有天数，因为是满足后续的天数来算的

        while (j < N) and (arr[j][0] <= i):

                heappush(res, -arr[j][1])
                j = j + 1 #j找到的话就往上顶一格，一共这一天，或者前一天寻找的时候以下一个资源天为开始

        if len(res) > 0:
            ret -= heappop(res)

    return ret


N,M = map(int,input().split())


# 后面的逻辑是基于前面的从小到大的排序的
list = [list(map(int,input().split())) for i in range(N)]

arr = sorted(list,key=lambda x:x[0])

result = calculate(N,M,arr)

print(result)

