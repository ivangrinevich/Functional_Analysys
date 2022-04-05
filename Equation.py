from math import atan


x_0 = 0
k = 0
while True:
    x_1 = 3 - (x_0 / (1 + x_0 ** 2)) - atan(x_0)
    if abs(x_1 - x_0) < 0.00001:
        print(x_1)
        print(k)
        break
    x_0 = x_1
    k += 1
