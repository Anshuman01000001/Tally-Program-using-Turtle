from turtle import forward, backward, left, right, penup, pendown, pos, goto


def shiftRight():
    penup()
    forward(10)
    pendown()


def drawTally():
    left(90)
    forward(50)
    backward(50)
    right(90)
    shiftRight()


def drawSlash():
    left(90)
    penup()
    forward(5)
    pendown()

    start_position = pos()
    goto(start_position[0]-50, start_position[1]+40)

    penup()
    goto(start_position)
    backward(5)
    right(90)
    pendown()

    shiftRight()
    shiftRight()

def drawFive():
    drawTally()
    drawTally()
    drawTally()
    drawTally()
    drawSlash()


def drawTallies(n):
    while(n>=5):
        drawFive()
        n -= 5
    while(n>=1):
        drawTally()
        n -= 1

num_to_draw = int(input("Enter a number: "))
drawTallies(num_to_draw)

input()