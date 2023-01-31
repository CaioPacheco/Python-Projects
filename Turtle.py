import turtle
from random import random

# kct = turtle.Turtle()
bct = turtle.Turtle()
# kct.penup()

rep = int(1+((random())*12))
print('Repetições')
print(rep)

ang = round(15+((random())*150), 2)
print('Angulo')
print(ang)

vnca = round((-1+((random())*4)), 2)
print('Variação Angular')
print(vnca)


vncl = round((-0.6+((random())*4.5)), 2)
print('Variação Linear')
print(vncl)


pas = round((1+((random())*7)), 2)
print('Passo')
print(pas)

bct.speed(0)
# kct.speed(10)
bct.color(random(), random(), random())
# kct.pen(shown= False)

for i in range(600):
    bct.lt(ang)
    # kct.lt(ang)
    local_vncl = (i*pas+(2*vncl*(random())))
    local_vnca = (ang+(0.2*vnca*(random())))
    for u in range(rep):

        # kct.fd(i*pas)
        # kct.lt(ang)
        bct.fd(local_vncl)
        bct.lt(local_vnca)

turtle.mainloop()

print(random())
