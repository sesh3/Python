import math
import sys


a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

D = b ** 2 - 4 * a * c

x1 = ((b * -1) + math.sqrt(D)) / (2 * a)
x2 = ((b * -1) - math.sqrt(D)) / (2 * a)

print(int(x1))
print(int(x2))