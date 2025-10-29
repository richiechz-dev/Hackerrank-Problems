arr = [1, 1, 0, -1, -1]

number_positive = 0
number_negative = 0
zero = 0

for number in arr:
    if number >= 1:
        number_positive = number_positive + 1
    elif number < 0:
        number_negative = number_negative + 1
    elif number == 0:
        zero = zero + 1

print(number_positive)
print(number_negative)
print(zero)

length_arr = len(arr)
ratio_postive = number_positive / length_arr
ratio_negative = number_negative / length_arr
ratio_zero = zero / length_arr

print(ratio_postive)
print(ratio_negative)
print(zero)

"""
Para imprimir con un formato se puede usar varias formas, con f-string por ejemplo o con format()"""

print(
    f"el ratio de los numeros positivos es: {ratio_postive:.6f}"
)  # se anexa la variable mas ":.6f" que significa que queremos 6 espacios de deciamal

print(f"el ratio de los numeros positivos es: {ratio_negative:.6f}")
print(f"el ratio de los numeros positivos es: {ratio_zero:.6f}")