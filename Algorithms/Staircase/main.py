"""
Imprimir una escalera de almuadillas
"""

''' Solucion que no cumple para nada los requisitos
n = 4
espacio = " "
almuadilla = "#"
for i in range(n):
    if i == 0:
        print(f"{espacio * 3}{almuadilla}")
    elif i == 1:
        print(f"{espacio * 2}{almuadilla * 2}")
    elif i == 2:
        print(f"{espacio * 1}{almuadilla * 3}")
    elif i == 3:
        print(f"{almuadilla * 4}")
'''

'''Primera solución
Es lo correcto pero no un correcto orden
'''
def staircase_1(n):
    espacio = " "
    almuadilla = "#"
    for i in range(1, n + 1):
        # print((n-i)*espacio+almuadilla*i)
        print(almuadilla * i + espacio * (n - i))

'''Segunda Solución
# Es la solución correcta que pide el problema de hackerrank, se puede describir de la siguente manera
'''
def staircase_2(n):
    for i in range(1, n + 1):
        print((n - i) * " " + "#" * i)


if __name__ == "__main__":
    n = 10
    staircase_1(n)
    staircase_2(n)
