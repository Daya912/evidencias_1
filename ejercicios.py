# Actividad clase 2

#1 Escribe un programa que pida al usuario su nombre y apellido, y luego los imprima juntos en un mensaje de saludo.
nombre = input("Por favor, ingresa tu nombre: ")

apellido = input("Por favor, ingresa tu apellido: ")

print(f"Hola, {nombre} {apellido}! Bienvenido/a.")

#2 Crea una variable llamada precio con el valor 100. Calcula el precio con un descuento del 15% y muestra el precio final.
precio = 100

descuento = precio * 0.15

precio_final = precio - descuento

print("El precio final después del descuento es:", precio_final)

#3 Escribe un programa que pida al usuario su edad y luego determine si es mayor o menor de edad.
edad = int(input("Por favor, ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

#4 Crea un programa que pida al usuario un número y determine si es par o impar.
numero = int(input("Por favor, ingresa un número: "))

if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

#5 Escribe un programa que pida al usuario dos números y luego calcule su suma, resta, multiplicación y división.
numero1 = float(input("Por favor, ingresa el primer número: "))
numero2 = float(input("Por favor, ingresa el segundo número: "))


suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

if numero2 != 0:
    division = numero1 / numero2
else:
    division = "No se puede dividir por cero"

print(f"La suma de {numero1} y {numero2} es: {suma}")
print(f"La resta de {numero1} y {numero2} es: {resta}")
print(f"La multiplicación de {numero1} y {numero2} es: {multiplicacion}")
print(f"La división de {numero1} entre {numero2} es: {division}")

#6 Crea un programa que pida al usuario su calificación y luego imprima el mensaje "Aprobado" si la calificación es mayor o igual a 70, o "Reprobado" si la calificación es menor que 70.
calificacion = float(input("Introduce tu calificación: "))

if calificacion >= 70:
    print("Aprobado")
else:
    print("Reprobado")

#7 Escribe un programa que pida al usuario dos números y luego determine cuál es el mayor.
num1 = float(input("Introduce el primer número: "))

num2 = float(input("Introduce el segundo número: "))

if num1 > num2:
    print(f"El mayor número es: {num1}")
elif num2 > num1:
    print(f"El mayor número es: {num2}")
else:
    print("Ambos números son iguales.")

#8 Crea un programa que pida al usuario su nombre y luego imprima un mensaje de bienvenida con su nombre.
nombre = input("Introduce tu nombre: ")

print(f"¡Bienvenido, {nombre}!")

#9 Escribe un programa que pida al usuario un número y luego imprima la tabla de multiplicar de ese número hasta el 10.
numero = int(input("Introduce un número: "))

print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

#10 Crea un programa que pida al usuario dos números y luego calcule su promedio.
numero1 = float(input("Introduce el primer número: "))

numero2 = float(input("Introduce el segundo número: "))

promedio = (numero1 + numero2) / 2

print(f"El promedio de {numero1} y {numero2} es: {promedio}")
