# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def main():
    lista = []
    largo = int(input("Ingrese el largo de valores de la lista: "))
    for x in range(largo):
        value = input("Ingrese el valor: ")
        lista.append(value)
    print(lista)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
