# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 19:41:39 2022

@author: 18122
"""
import turtle
t = turtle.Turtle()
x=0
y=-100
t.home()
t.penup()
t.goto(x,y)
t.pendown()
t.pensize(4)
t.circle(100)
t.penup()
t.goto(0,0)
t.pensize(4)
t.pendown()
t.goto(0,-48)
t.penup()
t.goto(0,-90)
t.write("6",font=("bold"))

t.goto(90,0)
t.write("3",font=("bold"))

t.goto(-90,0)
t.write("9",font=("bold"))

t.goto(0,80)
t.write("12",font=("bold"))

t.goto(0,0)
t.pendown()
t.goto(-75,0)

t.penup()
t.goto(0,-130)
t.write("6:45:00",font=("bold"))


turtle.done()