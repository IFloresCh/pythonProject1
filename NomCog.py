# demanar a l'usuari quants registres vol introduir
def main():
    lista = []
    quants, tel, edad = 0, 0, 0

    while quants < 1:
        quants = int(input("Ingrese cuantos vas a registrar: "))
    for x in range(quants):
        name = input("Ingrese Nombre, Apellido1, Apellido2: ")
        lista.append(name)

        while tel > 999999999 or tel < 1000000:
            tel = int(input("Ingrese su numero de telefono: "))
        lista.append(tel)

        while edad < 1:
            edad = int(input("Ingrese su edad: "))
        lista.append(edad)

        cont = bool(input("Contacto True or False: "))
        if cont is True:
            lista.append(True)
        elif cont is False:
            lista.append(False)
        while cont is not True or cont is not False:
            cont = input("Contacto True or False: ")

    print(lista)


if __name__ == '__main__':
    main()
