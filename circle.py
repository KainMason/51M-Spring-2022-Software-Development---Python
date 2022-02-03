# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 21:15:07 2022

@author: 18122
"""

import turtle
t = turtle.Turtle()
r=int(input("enter the radius of the circles: "))

count=0
x=-(r*2)
y=0
while count < 3:
    
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.circle(r)
    x+=(r*2)
    count += 1


count = 0
x=-(r*2)
y=-(r*2)
while count < 3:
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.circle(r)
    x+=(r*2)
    count += 1






turtle.done()