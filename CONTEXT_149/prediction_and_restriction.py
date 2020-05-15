N, K = 5, 2
R, S, P = 8, 7, 6
TRR = ['r', 's', 'r', 'p', 'r']

N, K = map(int,input().split())
R, S, P = map(int,input().split())
TRR = list(input())


def calculate(n, k, r, s, p, trr):
    commands = []
    points = 0

    for i in range(n):
        command = ""
        point = 0

        if trr[i] == 'r':
            command = "p"
            point = p

        if trr[i] == 's':
            command = 'r'
            point = r

        if trr[i] == 'p':
            command = 's'
            point = s

        if i - k >= 0:
            if commands[i - k] == command:
                command = ""
                point = 0

        commands.append(command)
        points = points + point

    print(points)


calculate(N, K, R, S, P, TRR)
