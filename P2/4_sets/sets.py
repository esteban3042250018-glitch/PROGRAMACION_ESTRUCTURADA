"""

 
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""

print("\033c")

set1={"Hola","123","123","Mexico","Holandaa",123,3.1416}
print(set1)
set1.add("Ganador")
print(set1)

set1.pop()
print(set1)
#ejemplo Crear un programa que solicite los email de los alumnos de la UTD almacenar en una lista y posteriormente mostrar en pantalla los email sin duplicados

#Solucion 1
emails = []

for i in range(5):
    correo = input("Introduce el email del alumno: ").strip().lower()
    if correo not in emails:
        emails.append(correo)

print("Emails sin duplicados:")
print(emails)

#Solucion 2
# Solucion 2
emails = []

for i in range(5):
    correo = input("Introduce el email del alumno: ").strip().lower()
    emails.append(correo)

emails_unicos = list(set(emails))

print("Emails sin duplicados:")
print(emails_unicos)

  



