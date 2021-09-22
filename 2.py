import turtle

turtle.shape('turtle')
turtle.speed(100)
i = 0
while True:
    turtle.forward(0.2 + i/500)
    turtle.left(1)
    turtle.speed(100 + i * 10)
    i += 1
