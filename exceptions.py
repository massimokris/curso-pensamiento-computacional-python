def divide(lista, divider):
    try:
        return [i / divider for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista

lista = list(range(10))
divider = 0

print(divide(lista, divider))