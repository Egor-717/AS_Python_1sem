n = int(input())

x = []
for i in range(n):
    x.append(list(map(int, input().split())))

y = []

for c in range(n):
    line = []
    for r in range(n - 1, -1, -1):
        line.append(x[r][c])
    y.append(line)

main = 0
side = 0

for i in range(n):
    main += y[i][i]
    side += y[i][n - i - 1]

for i in range(n):
    for k in range(n):
        print(y[i][k], end=' ')
    print()

print(main, side)
