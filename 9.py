import turtle as tr
import math

def nug(x):
    tr.left(90 * (x - 2) / x)
    a = x * 50 * math.sin(180/x)
    for i in range(x):
        tr.forward(a)
        tr.right(180 - 180 * (x - 2) / x )
    tr.right(90 * (x - 2) / x)
    tr.backward(10)

for i in range(3, 11):
    nug(i)
    

