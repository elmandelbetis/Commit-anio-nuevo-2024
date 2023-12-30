import turtle
import time

# Configuración de la ventana de salida
wn = turtle.Screen()
wn.setup(width=1920, height=1080)
wn.bgcolor("black")
wn.title("FELIZ AÑO NUEVO 2024")

# Creación del objeto turtle
betis = turtle.Turtle()
betis.speed(15)  # Velocidad del dibujo

# Función dibujante de círculos de color específico
def circulo_central(radio, x, y):
    betis.penup()
    betis.goto(x,y)
    betis.pendown()
    betis.color("#E7A614")
    betis.width(5)
    betis.fillcolor("white")
    betis.begin_fill() # Rellenamos de blanco
    betis.circle(radio)
    betis.end_fill() # Termina rellenado

#Función para dibujar el triángulo principal del escudo
def triangulo(x, y, width, length):
    betis.penup()
    betis.goto(x,y)
    betis.pendown()
    betis.color("#E7A614")
    betis.width(width)
    
    betis.fillcolor("white")
    betis.begin_fill()
    betis.backward(length)
    betis.right(45)    
    betis.forward(645)
    betis.left(90)
    betis.forward(645)
    betis.right(45)
    betis.backward(length)
    betis.end_fill()

#Función para dibujar las barras verticales de la mitad izquierda
def barra_vertical(x, y, anchura, altura):
    betis.penup()
    betis.goto(x,y)
    betis.right(90)
    betis.begin_fill()  # Comienza el llenado
    betis.forward(anchura)  # Dibuja hacia la derecha
    betis.right(90)  # Gira 90 grados a la derecha
    betis.forward(altura+20)  # Dibuja hacia abajo
    betis.right(135)  # Gira 90 grados a la derecha
    betis.forward(155)  # Dibuja hacia la izquierda
    betis.end_fill()  # Termina el llenado
    betis.right(45)

#Función para dibujar las barras verticales de la mitad derecha
def barra_vertical_inversa(x, y, anchura, altura):
    betis.penup()
    betis.goto(x, y)
    betis.right(270)
    betis.begin_fill()  # Comienza el llenado
    betis.forward(anchura)  # Dibuja hacia la derecha
    betis.left(90)  # Gira 90 grados a la izquierda
    betis.forward(altura + 20)  # Dibuja hacia arriba
    betis.left(135)  # Gira 135 grados a la izquierda
    betis.forward(155)  # Dibuja hacia la derecha
    betis.end_fill()  # Termina el llenado
    betis.left(45)    
    
def circulo(radio,x,y):
    betis.penup()
    betis.goto(x,y)
    betis.pendown()
    betis.color("#E7A614")
    betis.width(5)
    betis.begin_fill() # Rellenamos de blanco
    betis.circle(radio)
    betis.end_fill() # Termina rellenado

# Dibujamos la estructura base del escudo
circulo_central(126, 0, -126)
triangulo(-106,70, 5, 350)
betis.penup()
betis.color("#0BB363")
betis.left(90)
barra_vertical(-350,67,110,190)
barra_vertical(-150,67,110,390)
barra_vertical_inversa(150, 67, 110, 390)
barra_vertical_inversa(350,67,110,190)
circulo_central(150, 150, 0)


#Dibujamos las letras B, R y los detalles del centro
betis.penup()
betis.color("#0BB363")
betis.width(10)
betis.goto(-70,-90)
betis.pendown()
betis.forward(175)
betis.penup()
betis.goto(-80, 90)
betis.right(90)
betis.pendown()
betis.forward(160)
betis.right(85)
betis.forward(80)
betis.right(60)
betis.forward(20)
betis.right(35)
betis.forward(135)
betis.penup()
betis.right(180)
betis.forward(135)
betis.pendown()
betis.right(45)
betis.forward(25)
betis.right(50)
betis.forward(70)
betis.right(85)
betis.forward(150)
betis.penup()
betis.goto(-85,45)
betis.pendown()
betis.backward(20)
betis.penup()
betis.backward(135)
betis.pendown()
betis.backward(20)
betis.penup()
betis.goto(-85,-45)
betis.pendown()
betis.backward(20)
betis.penup()
betis.backward(135)
betis.pendown()
betis.backward(20)
betis.penup()
betis.right(90)
betis.goto(5,-10)
betis.pendown()
betis.forward(20)
betis.penup()
betis.goto(-30, -110)
betis.pendown()
betis.forward(220)
betis.left(90)
betis.forward(10)
betis.penup()
betis.goto(-30, -110)
betis.pendown()
betis.forward(10)
betis.penup()
betis.goto(40,-110)
betis.right(90)
betis.pendown()
betis.forward(220)
betis.left(90)
betis.forward(40)
betis.penup()
betis.goto(40,-110)
betis.pendown()
betis.forward(40)

# Sí, lo sé. El código es horrible. Debería haberlo metido en una 
# función pero lo iba haciendo sobre la marcha y al final quedó esto
# 
# Con la corona flipáis ya

# Realización de la base dorada de la corona
betis.penup()
betis.color("#E7A614")
betis.width(25)
betis.goto(-140,77)
betis.pendown()
betis.right(120)
betis.forward(40)
betis.right(15)
betis.forward(20)
betis.right(15)
betis.forward(40)
betis.right(15)
betis.forward(40)
betis.right(10)
betis.forward(45)
betis.right(10)
betis.forward(25)
betis.right(15)
betis.forward(30)
betis.right(15)
betis.forward(40)
betis.right(15)
betis.forward(30)
betis.right(10)
betis.forward(30)

# Dibujando el cojín rojo de la corona
betis.penup()
betis.color("red")
betis.width(50)
betis.goto(-140,140)
betis.left(105)
betis.pendown()
betis.forward(25)
betis.right(15)

for i in range(8):
    betis.forward(30)
    betis.right(8)
    
for i in range(2):
    betis.forward(15)
    betis.right(15)
    
betis.penup()
betis.goto(-140,77)

# Dibujando los círculos del adorno
circulo(15,-155,130)
circulo(15,-95,175)
circulo(15,-10,185)
circulo(15,70,167)
circulo(15,120,135)

#Dibujando la diadema y la cruz cristiana

betis.penup()
betis.goto(-140,140)
betis.width(20)
betis.setheading(135)
betis.pendown()
betis.forward(50)
for i in range(3):
    betis.forward(20)
    betis.right(10)
betis.right(60)
betis.forward(35)
for i in range(3):
    betis.forward(20)
    betis.right(10)
for i in range(3):
    betis.forward(20)
    betis.right(2)
for i in range(4):
    betis.right(6)
    betis.forward(60)
betis.right(25)
betis.forward(45)
betis.right(80)
betis.forward(100)
betis.penup()
betis.setheading(105)
betis.goto(-85,180)
betis.pendown()
betis.forward(100)
betis.penup()
betis.goto(5,185)
betis.pendown()
betis.setheading(90)
betis.forward(120)
betis.width(5)
betis.forward(25)
betis.backward(8)
betis.setheading(0)
betis.backward(15)
betis.forward(30)

betis.width(20)
betis.penup()
betis.goto(85,170)
betis.pendown()
betis.setheading(70)
betis.forward(105)


turtle.exitonclick()