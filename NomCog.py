# demanar a l'usuari quants registres vol introduir
def main():
    nom, cog1, cog2, phone, years, contacto = [], [], [], [], [], []
    lst = []
    pr, x, y = 0, 0, 4
    quants = int(input("Ingrese cuantos vas a registrar: "))
    while quants < 1:
        quants = int(input("Ingrese cuantos vas a registrar: "))
    for x in range(quants):

        name = input("Ingrese Nombre, Apellido1, Apellido2: ")
        while len(name) > 30:
            name = input("Ingrese Nombre, Apellido1, Apellido2: ")
        nom.append(name)

        tel = int(input("Ingrese su numero de telefono: "))
        while tel > 99999999 or tel < 1000000:
            tel = int(input("Ingrese su numero de telefono: "))
        phone.append(tel)

        edad = int(input("Ingrese su edad: "))
        while edad < 1:
            edad = int(input("Ingrese su edad: "))
        years.append(edad)

        cont = int(input("Contacto True or False: "))
        while cont < 0 or cont > 1:
            cont = int(input("Contacto True or False: "))
        contacto.append(cont)

    print("{:<30} {:<15} {:<10} {:<10}".format('Nombre', 'Telefono', 'Años', 'Contacto'))
    for x in range(quants):
        print("{:<30} {:<15} {:<10} {:<10}".format(nom[x], str(phone[x]), str(years[x]), contacto[x]))


if __name__ == '__main__':
    main()
