import turtle as tr

def circ():
    for i in range(360):
        tr.forward(1)
        tr.left(1)
    for i in range(360):
        tr.forward(1)
        tr.right(1)

tr.speed(1000)

while True:
    circ()
    tr.right(45)
