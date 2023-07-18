
lista=(1,2,3,4,5,6,7,8,9) #Creo la lista de donde saca los números de la matriz que se va a generar.
import random   #Importo random para que lo seleccione aleatoriamente de la lista.
matriz=[]   #Creo la lista matriz donde se van a incluir las sublistas.
def creomatriz (n): #función que crea la matriz.
    for i in range(n):  #bucle desde i hasta el valor ingresado por el usuario (filas) donde se generan las sublistas de la matriz.
        fila=[] #variable que almacena las listas que después se incluyen en la variable matriz, esta variable es solo para la función.
        for i in range(n):  #Bucle que genera los números aleatorios y lo incluye en la variable temporal, se repite generando n números aleatorios.
            numero=(random.choice(lista))   
            fila.append(numero) 
        matriz.append(fila)    #finaliza el bucle de la sublista y se ingresa la lista como sublista de la matriz.
    for i in range(n): print(matriz[i], end="\n")  #imprime la matriz en pantalla finalizado el bucle.

n=int(input("Ingresa un número entero del 1 al 100: "))
bucle=True #Variable de control del bucle de que los números sean válidos entre 0 y 100 (me ha parecido buena idea acotar el tamaño de la matriz)
while bucle==True:  
    if 0<n<=100:
        bucle=False
    else:    
        n=int(input("Número incorrecto, por favor, ingrese un número válido: "))

creomatriz(n)   #llamo a la función que crea la matriz
filaslist=[]    #lista que va a recoger la suma de las filas
columnlist=[]   #lista que va a recoger la suma de las columnas

for i in range(n):  #bucle para sumar las filas, desde i hasta el número que ha ingresado el usuario (número total de filas y columnas)
    sumafila=sum(matriz[i]) #suma las sublistas, i es la que lleva el control de la sublista que se está generando
    filaslist.append(sumafila)
print("La suma de las filas es: ", filaslist)
for i in range (n): #bucle que suma las columnas, desde i hasta el número ingresado por el usuario
    col=[row[i] for row in matriz]  #esta variable almacena a través del comando row una lista de las columnas de la matriz controladas por i (lo saqué literal de los apuntes) 
    columnlist.append(sum(col)) #sumamos las listas creadas por row y las almacenamos en una nueva lista
print("La suma de las columnas es: ", columnlist)    

