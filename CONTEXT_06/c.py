def calculate(n, m):

    for z in range(m // 4 + 1):
        x = 3 * n - m + z
        y = n - x - z

        if x >= 0 and y >= 0 and z >= 0:
            print(x, y, z)
            return

    print(-1, -1, -1)


N, M = map(int,input().split())
calculate(N, M)
