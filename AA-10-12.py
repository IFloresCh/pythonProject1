def main():
    lista = 'azgdwohexs'

    letra = input("Introduce una letra para verificar si esta en la lista: ")
    if letra in lista:
        print("La letra esta en la lista")
    else:
        print("la letra no esta en la lista")


if __name__ == '__main__':
    main()
