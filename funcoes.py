def imprime_lista(lista, maximo):
    if len(lista) > maximo:
        nova_lista = lista[:maximo]
        return nova_lista
    else:
        return lista

def media(soma, quantidade):
    media = soma / quantidade
    return media