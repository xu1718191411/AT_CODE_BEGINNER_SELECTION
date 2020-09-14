import bisect
from typing import List


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        arr = arr[::-1]

        srr = [0, len(arr) + 1]

        if max(arr) == m:
            return len(arr)
        for i in range(len(arr)):
            k = bisect.bisect_left(srr, arr[i])
            srr.insert(k, arr[i])
            print(srr)

            if (k - 1) >= 0:
                s1 = (srr[k] - srr[k - 1] - 1)
                if s1 == m:
                    return len(arr) - i - 1
            if (k + 1) < len(srr):
                s2 = (srr[k + 1] - srr[k] - 1)
                if s2 == m:
                    return len(arr) - i - 1
        return -1


solution = Solution()
arr = [3, 5, 1, 2, 4]
m = 1
arr = [3, 1, 5, 4, 2]
m = 2
#
# arr = [1]
# m = 1
#
# arr = [2,1]
# m = 2
#
# arr = [1, 2]
# m = 1
res = solution.findLatestStep(arr, m)

print("====")
print(res)
