# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 17:17:27 2022

@author: 18122
"""

print("Cramer's Rule")
a=float(input("Enter the vale of-A : "))
b=float(input("Enter the vale of-B : "))
c=float(input("Enter the vale of-C : "))
d=float(input("Enter the vale of-D : "))
e=float(input("Enter the vale of-E : "))
f=float(input("Enter the vale of-F : "))

x1 = (e*d)-(b*f)
x2 = (a*d)-(b*c)


y1 = (a*f)-(e*c)
y2 = (a*d)-(b*c)


if y2==0 and x2 ==0:
    print("The equation has no solution")
    print("A: "+str(a)+", B: "+str(b)+",C: "+str(c)+".D: "+str(d)+",E: "+str(e)+",F: "+str(f))
else:
    print("x equals : ",(x1/x2))
    print("y equals : ",(y1/y2))
    