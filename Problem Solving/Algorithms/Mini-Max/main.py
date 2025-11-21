def main():
    
    "Solucion Clasica del ejercio, similar a c y java"
    arr = [1, 2, 3, 4, 5]
    large = len(arr)  # Solo es para recordar que se puede saber el largo mediante el metodo len() , devuelve un objeto completamente nuevo en realidad. 
    
    
    # Inicializamos las variables o los acumuladores en 0
    suma_min = 0
    suma_max = 0
    
    # Creamos un for sencillo que en vez de recorrer el arr simplemente, lo que hacemo es pasarle el objeto iterable range() para generar la sencuencia en i con: 0, 1, 2, 3
    for i in range(4):
        suma_min = suma_min + arr[i] # suma min guardamos en cada iteracion el arr con la posicon 0, 1, 2 ,3 y sus elementos contenidos y asi en cada iteración
    print(f"suma min es: {suma_min}") # Saliendo imprimimos en patanlla la suma de los primeros 4 numeros
    
    # Creamos otro for para iterar sobre sobre los ultimos 4 numeros
    for i in range(1, 5):
        suma_max = suma_max + arr[i]
    print(f"suma max es: {suma_max}")


def minMaxSum():
    """
    Solucion Correcta - Una posible solución
        - Usando el metodo max(): extrae el valor max de una lista
        - Usando el metodo min(): extrae el valor min de una lista
        - Usando el metodo sum(): suma todo los valores de una lista
    """
    arr_minMaxSum = [1, 2, 3, 4, 5]

    sumMin = min(arr_minMaxSum)

    sumMax = max(arr_minMaxSum)

    total = sum(arr_minMaxSum)
  
    print(f"el {total - sumMin} {total - sumMax}")


if __name__ == "__main__":
    main()
    minMaxSum()
