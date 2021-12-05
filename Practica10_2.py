# demanar a l'usuari quants registres vol introduir
def main():
    app, rep = [], []
    s_app, s_rep, m_app, m_rep, i = 0, 0, 0, 0, 1
    num = int(input("Introduce cuantas notas quiere registrar: "))
    while num < 1:
        num = int(input("Debe ser mayor a 0\nIntroduce cuantas notas quiere registrar: "))

    note = int(input("Introduce la nota del 0 al 10: "))
    while i < num:
        note = int(input("Introduce la nota del 0 al 10: "))
        if note >= 5:
            app.append(note)
            i += 1
        elif note <= 4:
            rep.append(note)
            i += 1
        else:
            int(input("Solo notas del 0 al 10\nIntroduce la nota del 0 al 10: "))
    for y in app:
        s_app += y
        m_app = s_app / len(app)
    for z in rep:
        s_rep += z
        m_rep = s_rep / len(rep)

    print(app)
    print(rep)


if __name__ == '__main__':
    main()
