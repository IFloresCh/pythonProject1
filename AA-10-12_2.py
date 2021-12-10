def main():
    total = 0
    notas = [2.0, 5.5, 9.0, 10.0, 4.9, 8.0, 8.5, 7.0, 6.6, 5.0, 9.0, 7.0]
    for x in notas:
        if x == 10:
            print("Un alumno a sacado 10 de nota!")

    for x in notas:
        total += x
    print("La Media del curso es", total / len(notas))


if __name__ == '__main__':
    main()
