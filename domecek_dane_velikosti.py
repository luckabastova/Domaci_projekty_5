s=int(input("Zadej délku strany čtverce:"))

from turtle import shape, forward, left, exitonclick
from math import sqrt
shape ("turtle")

for i in range (4):
    forward (s)
    left (90)

left (45)
forward (sqrt(2)*s)

for i in range (2):
    left (90)
    forward ((sqrt(2)/2)*s)

left (90)
forward (sqrt(2)*s)

left
exitonclick ()
