def main():
    usr, dpt, cls = [], [], []
    dictio = {
        "username": usr,
        "department": dpt,
        "classroom": cls
    }
    quants = int(input("Ingrese cuantos vas a registrar: "))
    while quants < 1:
        quants = int(input("Ingrese cuantos vas a registrar: "))
    for x in range(quants):

        user = str(input("Ingrese Nombre de Usuario: "))
        while len(user) < 1:
            user = str(input("Ingrese Nombre de Usuario: "))
        usr.append(user)

        depar = str(input("Ingrese Nombre de departamento: "))
        while len(user) < 1:
            depar = str(input("Ingrese Nombre de departamento: "))
        dpt.append(depar)

        classroom = int(input("Ingrese numero de classroom entre 1 y 15: "))
        while classroom < 1 or classroom > 15:
            classroom = int(input("Ingrese numero de classroom entre 1 y 15: "))
        cls.append(classroom)

        print(dictio)


if __name__ == '__main__':
    main()
