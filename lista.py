miLista=[3,4,1,87]

#print(miLista[2])
for ele in miLista:
    print(ele)

#agregar
print("agregar")
miLista.append("pepe")
#agrega al final
for ele in miLista:
    print(ele)

#insertar
print("insertar")
#agrega segun la posicion que indiquemos
miLista.insert(1,"hi")
for ele in miLista:
    print(ele)

#Eliminar
print("Eliminar")
try:
    miLista.remove("pepe")
    miLista.remove("hi")
except ValueError as ex:
    print("No se elimino, por que no se encontro")
else:
    print("Se elimino")
for ele in miLista:
    print(ele)

#ordenar y dar vuelta
print("order y girar")
miLista.sort()#ordena de menor a mayor
miLista.reverse()#invierte orden
for ele in miLista:
    print(ele)
"""
print("Imprimir forma distinta")
indice=0
max= int(miLista.__len__ ,"")
while indice< max:
    print(miLista[indice])
    indice=indice+1
"""