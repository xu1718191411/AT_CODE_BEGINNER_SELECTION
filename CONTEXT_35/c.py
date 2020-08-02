# N, Q = 5, 4
# ARR = [
#     [1, 4],
#     [2, 5],
#     [3, 3],
#     [1, 5],
# ]

N, Q = map(int, input().split())
ARR = []
for i in range(Q):
    ARR.append(list(map(int,input().split())))

def calculate(n, q, arr):

   qrr = [0 for i in range(n)]

   for i in range(q):
       start = arr[i][0] - 1
       end = arr[i][1]

       qrr[start] = qrr[start] + 1
       if end < n:
            qrr[end] = qrr[end] - 1

   currentSum = 0
   result = []
   for i in range(n):
       currentSum += qrr[i]
       qrr[i] = currentSum

       if currentSum % 2 == 0:
           result.append("0")
       else:
           result.append("1")

   print("".join(result))



calculate(N, Q, ARR)
