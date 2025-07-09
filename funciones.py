def pregunta1():

    respuesta = input('Que deseas comprar? [Q] para salir ')

    if respuesta == 'Q':
        return '', False
    else:
        return respuesta, True

def pregunta2(producto):
    while (True):
        respuesta = input('Seguro que quiere añadir "{}" [S/N]'.format(producto))
        if respuesta in ['S', 'N']:
            logica = True if respuesta == 'S' else False
            return logica

