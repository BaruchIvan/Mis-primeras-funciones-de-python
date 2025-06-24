def contador(palabra):
    espacios = 0
    puntos = 0
    comas = 0
    for letra in palabra:
        if letra == ' ':
            espacios += 1
        elif letra == '.':
            puntos += 1
        elif letra == ',':
            comas += 1

    return([espacios, comas, puntos])

def Mayusculas():
    palabra = input('Introduce una palabra  ')
    contador = 0
    for letra in palabra:
        if letra == ' ':
            continue
        letraMayuscula = letra.upper()
        if letra == letraMayuscula:
            contador += 1
    return contador

def tabla(num):
    lista = []
    for i in range(1,11):
        lista.append(num * i)
    return  lista


if __name__ == '__main__':
    print(contador(palabra= 'Hola me llamo Nate, ¿tu como te llamas?'))
    print(tabla(10))
    print(Mayusculas())