import math

x = int(input())

answer = 1 / (1 + math.exp(-x))

print(round(answer, 2))
