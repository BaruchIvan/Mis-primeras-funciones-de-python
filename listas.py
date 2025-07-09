import funciones as fun

print("=== Program Lista de la compra ===")

lista = []

while True:
    producto, salida = fun.pregunta1()

    if not salida:
        break
    if producto in lista:
        print('{} ya esta en la lista'.format(producto))
        continue
    aniadir = fun.pregunta2(producto)

    if aniadir:
        lista.append(producto)


print('\n \n la lista de compra es: \n {}'.format(lista))