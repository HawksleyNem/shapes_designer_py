from turtle import *

# circle(50)
# penup()
# goto(100,0)
# pendown()
# circle(50)
# penup()
# goto(100,100)
# pendown()
# circle(50)
# penup()
# goto(0,100)
# pendown()
# circle(50)

# exitonclick() 

# value = int(input(print("Saisir un rayon : "))) #Demande le rayon à l'utilisateur
# color = str(input(print("Saisir une couleur (anglais + minuscule) : "))) #Demande la couleur de remplissage des cercles

# fillcolor(f"{color}")
# begin_fill()
# circle(value)           #Trace le cercle avec la couleur choisie
# end_fill()

# hideturtle()
# penup()                 #Changement d'emplacement en masquant le curseur
# goto((value*2),0)

# showturtle()
# pendown()
# begin_fill()
# circle(value)
# end_fill()

# hideturtle()
# penup()
# goto((value*2),(value*2))

# showturtle()
# pendown()
# begin_fill()
# circle(value)
# end_fill()

# hideturtle()
# penup()
# goto(0,(value*2))

# showturtle()
# pendown()
# begin_fill()
# circle(value)
# end_fill()

# hideturtle()

# exitonclick() #Cliquer pour quitter

value = int(input(print("Saisir un rayon : "))) #Demande le rayon à l'utilisateur
color = str(input(print("Saisir une couleur (anglais + minuscule) : "))) #Demande la couleur de remplissage des cercles
coo = value*2

for i in [100,0,0,0]:
    fillcolor(f"{color}")
    showturtle()
    begin_fill()
    circle(value)           #Trace le cercle avec la couleur choisie
    end_fill()
    hideturtle()
    penup()                 #Changement d'emplacement en masquant le curseur
    goto((coo),i)
    coo = 0

exitonclick() #Cliquer pour quitter