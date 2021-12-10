def main():
    lista = []
    for x in range(31):
        if x % 2 == 0:
            lista.append(x)
    print(lista)
# lista corto
    lista2 = [x for x in range(31) if x % 2 == 0]
    print(lista2)


if __name__ == '__main__':
    main()
