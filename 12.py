import turtle as tr

def duga(x):
    for i in range(180):
        tr.forward(x)
        tr.right(1)

k = 1
tr.left(90)
while True:
    tr.speed(100)
    duga(k)
    tr.speed(500)
    duga(k/5)
