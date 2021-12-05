# demanar a l'usuari quants registres vol introduir
def main():
    nom, cog1, cog2, phone, years, contacto = [], [], [], [], [], []
    lst = []
    pr, x, y = 0, 0, 4
    quants = int(input("Ingrese cuantos vas a registrar: "))
    while quants < 1:
        quants = int(input("Ingrese cuantos vas a registrar: "))
    for x in range(quants):

        name = input("Ingrese nombre: ")
        while len(name) > 20 or len(name) < 1:
            name = input("Ingrese nombre: ")
        nom.append(name)

        mname = input("Ingrese apellido 1: ")
        while len(mname) > 20 or len(mname) < 1:
            mname = input("Ingrese apellido 1: ")
        cog1.append(mname)

        lname = input("Ingrese apellido 2: ")
        while len(lname) > 20 or len(lname) < 1:
            lname = input("Ingrese apellido 2: ")
        cog2.append(lname)

        tel = int(input("Ingrese su numero de telefono: "))
        while tel > 99999999 or tel < 10000000:
            tel = int(input("Ingrese su numero de telefono: "))
        phone.append(tel)

        edad = int(input("Ingrese su edad: "))
        while edad < 1:
            edad = int(input("Ingrese su edad: "))
        years.append(edad)

        cont = int(input("Contacto True or False: "))
        while cont < 0 or cont > 1:
            cont = int(input("Contacto True or False: "))
        if cont == 0:
            contacto.append('False')
        else:
            contacto.append('True')


    print("{:<60} {:<16} {:<8} {:<8}".format('Nombre', 'Telefono', 'Años', 'Contacto'))
    for x in range(quants):
        print("{:<20} {:<20} {:<18} {:<16} {:<8} {:<8}".format(nom[x], cog1[x], cog2[x], str(phone[x]), str(years[x]), str(contacto[x])))


if __name__ == '__main__':
    main()
