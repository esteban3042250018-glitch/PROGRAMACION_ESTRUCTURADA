
print("\033c")
#Ejemplo 1 Crear una lista de numeros e imprimir el contenido
numeros = [23,33,45,8,24,0,100]
print(numeros)

# lista = ""
for i in numeros:
    lista += f"{i}, " 

print("["+lista+"]")

# lista = ""
for i in range(0,len(numeros)):
    lista += f"{numeros[i]}, " 

print("["+lista+"]")

# lista = ""
i=0
while  i<len(numeros):
    lista += f"{numeros[i]}, " 
    i+=1

print("["+lista+"]")

#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 
#primer forma
palabras = ["UTD", "tercer", "cuatrimestre", "TI"]

palabra = input("Ingresa la palabra a buscar").strip()
if palabra in palabras:
    print(f"Encontre la palabra {palabra}")
else:
    print("No encontre la palabra")

#2DA FORMA
palabra = input("Ingresa la palabra a buscar").strip()

encontro = False
for i in palabras:
    if i == palabra:
        encontro=True
if encontro:
    print("Encontre la palabra")
else:
    print("No encontre la palabra")
        
#3er FORMA Len
encontro = False
for i in range(len(palabras)):
    if palabras[i] == palabra:
        encontro=True
if encontro:
    print("Encontre la palabras")
else:
    print("No encontre la palabra")
#4ta FORMA While
encontro = False
i=0
while i < len(palabras):
    if palabras[i] == palabra:
        encontro=True
    i+=1
if encontro:
    print("Encontre la palabra")
else:
    print("No encontre la palabra")
#Ejemplo 3 Añadir elementos a la lista

#Opcion 1
lista = []
true=True
while true:
    lista.append(input("Dame un valor: ").strip())
    true=input("Ingresa True/False para continuar: ").strip()
    if true == "False":
        true=False


print(lista)

# opcion 2
lista = []
true="true"
while true=="true":
    lista.append(input("Dame un valor: ").strip())
    true=input("Ingresa True/False para continuar: ").lower().strip()
    

#Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda

agenda = [
    ["Carlos","618123456"],
    ["Adrian","6182332456"],
    ["Luis","6182223444"]
]
# print(agenda)

for i in agenda:
    print(i)

agendas=""
for r in range(0,3):
    for c in range (0,2):
        agendas+=f"{agenda[r][c]}, "
    agendas += "\n[ "

print(agendas)

