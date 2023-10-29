import turtle
import time
from disk_scheduling import FCFS, SSTF, SCAN, CSCAN, CLOOK


def Visualise(option, request_arr, start):
    request = list(request_arr.split(" "))
    request = [int(i) for i in request]
    if option == "FCFS":                        # Select and run algorithm
        Order, Sum = FCFS(request, start)
    elif option == "SSTF":
        Order, Sum = SSTF(request, start)
    elif option == "SCAN":
        Order, Sum = SCAN(request, start)
    elif option == "CSCAN":
        Order, Sum = CSCAN(request, start)
    elif option == "CLOOK":
        Order, Sum = CLOOK(request, start)

    turtle.clearscreen()
    t0 = time.time()
    Disk = turtle.Screen()
    Disk.title(option)
    Disk.bgcolor("Light Gray")
    Disk.setworldcoordinates(-5, -20, 210, 10)  # Set turtle window boundaries
    head = turtle.Turtle()
    head.shape("square")
    head.color("Black")
    head.turtlesize(.5, .5, 1.5)
    head.speed(2)
    head.pensize(0)

    head2 = turtle.Turtle()
    head2.shape("circle")
    head2.color("Red")
    head2.turtlesize(.5, .5, 1.5)
    head2.speed(4)
    head2.pensize(0)

    n = len(Order)
    y = -1
    y2 = 0
    temp_order = [int(i*10) for i in range(0, 21)]
    for i in range(0, len(temp_order)):
        head2.goto(temp_order[i], y2)
        head2.stamp()
        head2.write(temp_order[i], False, align="right")

    for i in range(0, n):
        if i == 0:                                          # No drawing while the diskhead reaches start position
            head.penup()
            head.goto(Order[i], y)
            head.pendown()
            head.stamp()
            head.write(Order[i], False, align="right")
        else:                                               # Diskhead draws its path to each request
            head.goto(Order[i], y-1)
            head.stamp()
            head.write(Order[i], False, align="right")
            y -= 1
    head.hideturtle()
    head.speed(0)
    head.penup()
    head.goto(100, 5)
    t1 = time.time()

    message1 = "Disk Scheduling Algorithm: " + option
    message2 = "Total Head Movement: " + str(Sum)
    start = "\033[1m"
    end = "\033[0;0m"
    head.write(message1, False, align="center", font=(
        "Inter", 16))    # Display algorithm used
    head.goto(100, 4)
    head.write(message2, False, align="center", font=(
        "Inter", 16))     # Display total movement
    head.goto(100, 3)
    head.write("Time taken: " + str(round(t1-t0, 2)) + " Seconds",
               False, align="center", font=("Inter", 16))
    head.pendown()
    Disk.exitonclick()
