from decimal import Decimal as dec


def norm(x, y):
    maximum = 0
    for i in range(m):
        if abs(x[i] - y[i]) > maximum:
            maximum = abs(x[i] - y[i])
    return maximum


m = int(input())
matrix = []
for _ in range(m):
    matrix.append([dec(i) for i in input().split()])
d = [dec(i) for i in input().split()]
c = [[0 for _ in range(m)] for _ in range(m)]
for i in range(m):
    d[i] = d[i] / matrix[i][i]
    for j in range(m):
        c[i][j] = matrix[i][j] / matrix[i][i] if i != j else 0
        if c[i][j] == 0:
            c[i][j] = 0
x_0 = [dec(0) for _ in range(m)]
x_1 = []
for i in c:
    print(*i)
for i in range(m):
    total = 0
    for j in range(m):
        total += c[i][j] * x_0[j]
    x_1.append(dec(total + d[i]))
k = 1
while norm(x_0, x_1) >= 0.001:
    for i in range(m):
        x_0[i] = x_1[i]
    for i in range(m):
        total = 0
        for j in range(m):
            total += c[i][j] * x_0[j]
        x_1[i] = dec(total + d[i])
    k += 1
for i in range(m):
    if x_1[i] == 0:
        print(0)
    else:
        print('{0:f}'.format(x_1[i]))
