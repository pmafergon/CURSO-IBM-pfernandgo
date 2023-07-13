#Lo primero que hago es definir el tamaño de la matriz, para ello creo la variable n que es introducida por el usuario.


"""while n>9 or n<1:
    n = int(input("El número introducido no es correcto, por favor, ingrese un número del 1 al 9: "))"""
lista=(1,2,3,4,5,6,7,8,9)
import random
matriz=[]
def creomatriz (filas):
    for i in range(filas):
        fila=[]
        for i in range(filas):
            numero=(random.choice(lista))
            fila.append(numero)
        matriz.append(fila)    
    print (matriz)

filas=int(input("Ingresa un número del 1 al 9: "))
bucle=True
while bucle==True:
    if 0<filas<=9:
        bucle=False
    else:    
        filas=int(input("Número incorrecto, por favor, ingrese un número del 1 al 9: "))
creomatriz(filas)
filaslist=[]
columnlist=[]

for i in range(filas):
    sumafila=sum(matriz[i])
    filaslist.append(sumafila)
print("La suma de las filas es: ", filaslist)
for i in range (filas):
    col=[row[i] for row in matriz]
    columnlist.append(sum(col))
print("La suma de las columnas es: ", columnlist)    

