import turtle as tr

def zvezda(n):
    for i in range(n):
        tr.forward(100)
        tr.left(180 - 360 / n)

zvezda(11)
