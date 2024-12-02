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
  


# frutas=["Pera","Manzana","Uva","Banana"]

# frutas.append("Aguacate")

# print(frutas)
# print("*******************************************")
# print(frutas[3])

diccionario={
  "Titulo":"Programando mejor",
  "Autor":"Deivis",
  "Año":2024
}
diccionario["genero"]="Python"

print(diccionario["Autor"])

num1={1,2,3,4,67,78,9}
num2={1,2,3,4,63,636,36,63}
insert=num1&num2
print(insert)

numero_en_cadena="2024"
numero=int(numero_en_cadena)
print(f"{numero-2006} es tu edad")


