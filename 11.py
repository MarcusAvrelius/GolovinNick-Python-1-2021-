import turtle as tr

def circ(x):
    for i in range(360):
        tr.forward(x)
        tr.left(1)
    for i in range(360):
        tr.forward(x)
        tr.right(1)
i = 1
while True:
    circ(i)
    i += 1
