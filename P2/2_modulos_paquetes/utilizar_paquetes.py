from paquete1 import modulos,modulo_paquete

modulos.borrarPantalla()
""" modulos.funcion1() """


nom="Daniel"
ape="Carreon"
edad = int(input("Edad: "))
name,lastname,age = modulo_paquete.funcion4(nom,ape,edad)
print(f"Name: {name}\nLastname: {lastname}\n Edad:{age}")

men = modulo_paquete.funcion4(nom,ape)
print(men)

