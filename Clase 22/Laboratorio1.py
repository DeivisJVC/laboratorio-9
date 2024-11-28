#• Paso 1. Sintaxis Básica y Operaciones Simples
# nombre="Deivis"
# edad=18
# Esestudiante=True
# lista=["Aguacate","Python","JavaScript","SQL"]
# caracter=input("ingresa un caracter para añadir a la lista")
# talento="Talento"
# tech="Tech"
# lista.append(caracter)
# print(nombre)
# print(edad)
# print(Esestudiante)
# suma=edad-5
# resta=edad-15
# multiplicacion=edad*5
# division=edad/2
# print(suma)
# print(resta)
# print(multiplicacion)
# print(division)
# print(talento+tech)
# print(lista)

#Paso 2. Condicionales y Bucles
# number=int(input("ingrese el numero"))
# if number%2==0:
#   print("El numero es Par")
# else:
#   print("Es impar")

# lista2=[1,2,4,5,8,4,9,4,94,7,4,54,]

# for i in lista2:
#   cuadrado=i**2
#   print("El cuadrado es:",cuadrado)
  
  
# counter = 0
# limit = 10
# while counter < limit:
#     print("El limete es 10")
#     counter=int(input("Ingresa un numero"))
#     counter += 1
  
  
#• Paso 3. Listas y Diccionarios
# Estudiantes=["deivis","digna","Veronica","Valeria"]
# for i in Estudiantes:
#   print(i)

# Informacion={
#   "Telefono:":30158566697,
#   "Nombre:" :"Deivis",
#   "Correo:":"deivisyance@gmail.com"
# }

# claves=Informacion.keys()
# valor=Informacion.values()
# print(f"la clave es:{claves} y el valor es{valor}")

# lista3=[0,"Deivis"]

# def agregar_datos_lista():
#   ingresar=1
#   while ingresar!="0":
#     ingresar=(input("Ingrese valors a la lista"))
#     lista3.append(ingresar)
#   print(lista3)
# agregar_datos_lista()

# def calculadora():
#   num1=int(input("ingrese el primer numero"))
#   num2=float(input("ingrese el segundo numero"))
#   operacion=int(input("ingrese 1 para suma, 2 para resta, 3 para multiplicacion y4 para division"))
#   if operacion==1:
#     resultado=num1+num2
#     print(f"La suma de {num1} y {num2} es:{round(resultado)}")
#   elif operacion==2:
#     resultado=num1-num2
#     print(f"La resta de {num1} y {num2} es: {round(resultado)}")
#   elif operacion==3:
#     resultado=num1*num2
#     print(f"La multiplicacion de {num1} y {num2} es: {round(resultado)}")
#   elif operacion==4:
#     resultado=num1/num2
#     print(f"La division de {num1} y {num2} es: {round(resultado)}")
#   else:
#     print("Operacion no valida")

# try:
#   calculadora()

# except ValueError as x:
#   print("ingrese solo numeros")
# except ZeroDivisionError:
#   print("no lo puede dividir por cero")
import random

def adivinar():
  comienza=random.randint(0,10)
  adivinar_input=int(input("Ingrese el numero para adivinar el rango es de 0-10"))
  while comienza!=adivinar_input:
    if adivinar_input>comienza:
      print("Un numero mas pequeño")
    elif adivinar_input<comienza:
      print("Un numero mas grande")
    adivinar_input=int(input("Ingrese el numero para adivinar"))
  print("Adivinaste el numero era",comienza)

adivinar()