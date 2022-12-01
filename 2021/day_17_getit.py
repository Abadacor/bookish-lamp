import math

x_min = 150
foundIt = False
x0 = 0

while not foundIt:
    if (x0 + sum(j for j in range(x0)) >= x_min):
        foundIt = True
    else:
        x0 += 1
print(x0)
        