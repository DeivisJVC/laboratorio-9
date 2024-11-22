#Primer ejercicio
# nombre=input("Ingrese un nombre")
# edad=int(input("ingrese su edad"))
# EsEstudiante=bool(input("¿Eres estudiante?"))
# estatura=float(input("Ingrese su estatura "))
# print("Nombre: ", nombre," Edad: ",edad," EsEstudiante: ", EsEstudiante, " Estatura: ",estatura)

#Segundo ejercicio

# num1=int(input("Ingrese el primer numero"))
# num2=int(input("Ingrese el segundo numero"))

# suma=num1+num2
# resta=num1-num2
# multiplicacion=num1*num2
# division=num1/num2

# print("Suma: ", suma, " Resta: ", resta, " Multiplicacion: ", multiplicacion, " Division: ", division)

#Ejercicio 3
# frase1=input("Ingrese la primera frase:")
# frase2=input("Ingrese la segunda frase:")

# frasecompleta=(f"{frase1} {frase2}")
# print("Frase completa:",frasecompleta)

#ejercicio 4
# listavacia=[]
# for i in range(10):
#     lista=input("ingresa 10 elementos de distintos tipos")
#     listavacia.append(lista)
    
# print(listavacia)

# listavacia[2]="Deivis"
# listavacia.append(2006)
# print(listavacia)
# listavacia.pop(2)
# print(listavacia)

#ejercicio5

persona = {
  "nombre":"Deivis",
  "edad":18,
  "ciduad":"Santa Marta",
  "profesion":"Estudiante"
}
print("Diccionario:",persona)
persona["profesion"]="Desarrolador de Sofware"
persona["hobby"]="Ver peliculas"
print("Actualizado", persona)
