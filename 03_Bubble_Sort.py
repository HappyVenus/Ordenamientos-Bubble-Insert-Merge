## Este programa es una explicacion del Bubble Sort. al nosotros dar el numero, generaremos al azar dicha cantidad de numeros al azar
## despues seran ordenados de forma ascendente.

import random
def bubblesort(L):
    count = 0
    acciones = 0
    for i in range (len(L)):
        acciones +=1
        for j in range (0,len(L)-i-1):
            acciones+=1
            if L[j] > L[j+1]:
                print ("Iteración",count)
                L[j], L[j+1] = L[j+1], L[j] #Intercambio
                print (L)
                count +=1
    print (acciones)

L = []
num = int (input("Escribe un número entero"))
for x in range (num):
   L.append(random.randrange(100,0,-1))
print('Antes de ordenar\t:',L)
print(bubblesort(L))
