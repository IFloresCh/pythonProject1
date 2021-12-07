def main():
    usr, dpt, cls = [], [], []
    dictio = {
        "username": usr,
        "department": dpt,
        "classroom": cls
    }
    user = str(input("Ingrese Nombre de Usuario: "))
    usr.append(user)

    depar = str(input("Ingrese Nombre de departamento: "))
    dpt.append(depar)

    classroom = int(input("Ingrese numero de classroom entre 1 y 15: "))
    while classroom < 1 or classroom > 15:
        classroom = int(input("Ingrese numero de classroom entre 1 y 15: "))
    cls.append(classroom)

    print(dictio)


if __name__ == '__main__':
    main()
