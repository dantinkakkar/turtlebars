## Graphs.py
## Generates graphs in python turtle graphics
## Currently supports bar graphs for 2-D data sets

import turtle
import canvasvg

def write_val(point,tur):
    tur.pu()
    tur.right(90)
    tur.forward(40)
    tur.left(90)
    tur.forward(50)
    tur.write(point,True,"right",("Helvetica",16,"normal"))
    tur.left(180)
    tur.forward(50)
    tur.right(90)
    tur.forward(40)
    tur.right(90)

def write_range(dataset,tur,scale,pro):
    tur.right(90)
    tur.pu()
    tur.forward(20)
    tur.right(90)
    curPos = 0
    while curPos < 300:
        tur.forward(scale*pro)
        curPos = curPos + scale*pro
        tur.write(curPos/pro,align="center")
        tur.right(90)
        tur.forward(20)
        tur.pd()
        tur.forward(20)
        tur.pu()
        tur.left(180)
        tur.forward(40)
        tur.right(90)
    tur.right(180)
    tur.forward(curPos)
    tur.left(90)
    tur.forward(20)
    tur.pd()

def draw_bar(dataset,title,scale,maxima):
    turt = turtle.Turtle()
    turt.setpos(300,0)
    window = turtle.Screen()
    window.colormode(255)
    turt.speed(700)
    max = 0
    for y in dataset:
        if y > max:
            max = y
    turt.left(180)
    turt.forward(600)
    turt.right(90)
    turt.forward(300)
    turt.pd()
    turt.left(180)
    turt.forward(300)
    write_range(dataset,turt,scale,300/maxima)
    # draw dataset
    for data in dataset:
        turt.fillcolor(((data[0]*8)%255,(data[0]*8/30)%255,(data[0]*8)%255))
        turt.forward(30)
        write_val(data[1],turt)
        turt.begin_poly()
        turt.begin_fill()
        turt.left(90)
        turt.forward(data[0]*300/maxima)
        turt.right(90)
        turt.forward(60)
        turt.right(90)
        turt.forward(data[0]*300/maxima)
        turt.end_poly()
        turt.end_fill()
        turt.left(90)
    turt.penup()
    turt.forward(300-len(dataset)*90+100)
    turt.right(90)
    turt.forward(150)
    turt.right(90)
    turt.forward(50)
    turt.left(180)
    turt.write(title,True,"center",("serif",32,"bold"))
    nameSav = title+".svg"
    ts = turt.getscreen().getcanvas()
    canvasvg.saveall(nameSav, ts)
    window.exitonclick()

#draw_bar([[95,"BST"],[91,"ECO"],[95,"ENG"],[79,"ENT"],[81,"ACC"]],"Hitu's Result",10,100)
