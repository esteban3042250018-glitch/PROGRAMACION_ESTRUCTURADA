"""   

  Las tuplas se utilizan para almacenar varios elementos en una sola variable.

   Una tupla es una colección ordenada e inmutable .

   Las tuplas se escriben entre paréntesis.


"""
print("\033c")
# print(paises_set)
# paises_set ={"México","Canada","EUA"}

paises =("México","Canada","EUA")
varios = ("Hola",True,33,3.1416)


print(paises)
print(varios)


for i in paises:
    print(i)


for i in range(0,len(paises)):
    print(paises[i])

i=0
while i < len(paises):
    print(paises[i], "opa")
    i+=1

print(f"El pais que inaugura la copa del mundo 2026 es: {paises[0]} ")

edades = (23,24,18,20,20,23,24,19,24)

cuantos = edades.count(24)
print(cuantos)

numero = int(input("Ingresa un numero:"))
posiciones = []
# posicion = edades.index(numero) 
for i in range (0,len(edades)):
    if numero == edades[i]:
      print(f"Encontre el numero {numero} en la posicion {i}")
      posiciones.append(i)

tupla_posiciones = tuple(posiciones)
print(posiciones)

#Utilizando set
numero = int(input("Ingresa un numero:"))
posiciones_set = {""}
posiciones_set.clear()
# posicion = edades.index(numero) 
for i in range (0,len(edades)):
    if numero == edades[i]:
      print(f"Encontre el numero {numero} en la posicion {i}")
      posiciones_set.add(i)

set_posiciones = tuple(posiciones_set)
print(set_posiciones)
     

