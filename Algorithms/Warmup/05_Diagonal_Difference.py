arr = [
    [11,2,4],
    [4,5,6],
    [10,8,-12]
]

#print(arr[1][1])

for fila in arr:    #el primer for recorre las filas con index 0
    for elemento in fila: #el for anidado recorre los elementos en la fila y los toma uno a uno
        pass

# Aqui lo que hacemos es buscar la longitud del array para saber la posicion en vez de solo saber el elemento
for i in range(len(arr)): #por cada index o fila en el rango de la logitud del array (3)
    for j in range(len(arr[i])):#quiero que corras otro for para cada index en la serie en el rango del largo del array de cada serie
        elemento = arr[i][j]    #quiero que cada elemento seria el de la posicion seleccionada en el array con fila y columna
        #print(f'En fila {i}, columna {j} esta el: {elemento}')  #imprime la fila y la columna (o posiciones) con el elemento que contienen

'''
* Para recorrer una matriz por ejemplo de la columna 1 de nuestro ejemplo
'''

#todo: Recorrer el array junto con sus posiciones o indices e imprimir solo la columna 1

for i in range(len(arr)):
    for j in range(len(arr[i])):
        elemento = arr [i][j]
        
        if j == 0:
            print(arr[i][j]) # * De esta forma se imprimira de todo el array solo los que tengan el indice 0


#todo: Imprimir solo las diagonales de izquierda a derecha


total = 0 #Defino el total afuera del bucle para que no se reinicie cada vez que se recorrar el array
for i in range(len(arr)):
    for j in range(len(arr[i])):
        elemento = arr [i][j]
        
        if i == j:
            total = total + elemento
            print(arr[i][j])
#print(total)

#todo: Imprimir solo las diagonales de derecha a izquierda

#todo: Imprimir la diferencia absoluta entre diagonal 1 y diagonal 2

suma_diagonal_primaria = 0
suma_diagonal_secundaria = 0

n = len(arr)

for i in range(n):
    for j in range(n):
        elemento = arr[i][j]
        #print(f'ejercicio diferencia absoluta {elemento}')
        if i == j:
            suma_diagonal_primaria = suma_diagonal_primaria + elemento
        if i + j == n - 1 :
            suma_diagonal_secundaria = suma_diagonal_secundaria + elemento

valor_absoluto = suma_diagonal_primaria - suma_diagonal_secundaria
print(f'el valor de la resta es: {abs(valor_absoluto)}')

