# demanar a l'usuari quants registres vol introduir
def main():
    lista = []
    quants = int(input("Ingrese cuantos vas a registrar: "))
    while quants < 1:
        quants = int(input("Ingrese cuantos vas a registrar: "))
    for x in range(quants):
        name = input("Ingrese Nombre, Apellido1, Apellido2: ")
        lista.append(name)
        tel = int(input("Ingrese su numero de telefono: "))
        while tel < 999999999 or tel > 9999999:
            tel = int(input("Ingrese su numero de telefono: "))
        lista.append(tel)
        edad = int(input("Ingrese su edad: "))
        lista.append(edad)
        cont = input("Contacto True or False: ")
        lista.append(cont)

    print(lista)


if __name__ == '__main__':
    main()
