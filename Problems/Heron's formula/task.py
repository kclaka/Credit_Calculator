# put your python code here
import math

a = int(input())
b = int(input())
c = int(input())


def get_p():
    p = (a + b + c) / 2
    return p


def get_s():
    get_p()
    return math.sqrt(get_p()*(get_p() - a)*(get_p() - b)*(get_p() - c))


print(get_s())