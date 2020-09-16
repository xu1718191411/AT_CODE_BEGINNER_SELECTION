def calculate(n,s):
    if n % 2 == 0:
        print(-1)
        return

    left = 0
    right = len(s) - 1

    leftMax = n // 2

    isOK = True
    while (left <= leftMax) and (right >= left):

        leftIndex = leftMax - left

        if leftIndex % 3 == 1:
            if s[left] == 'a' and s[right] == 'c':

                left += 1
                right -= 1
                continue
            else:
                isOK = False
                break

        if leftIndex % 3 == 2:
            if s[left] == 'c' and s[right] == 'a':

                left += 1
                right -= 1
                continue
            else:
                isOK = False
                break

        if leftIndex % 3 == 0:
            if s[left] == 'b' and s[right] == 'b':

                left += 1
                right -= 1
                continue
            else:
                isOK = False
                break

        left += 1
        right -= 1

    if isOK:
        print(leftMax)
    else:
        print(-1)

N = int(input())
S = input()
calculate(N,S)
