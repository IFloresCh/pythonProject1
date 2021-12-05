# demanar a l'usuari quants registres vol introduir
def main():
    print("Introduce 2 números el primero debe ser menor al segundo")
    n1 = int(input("Introduce el primer número: "))
    n2 = int(input("Introduce el segundo número: "))
    while n1 > n2:
        int(input("El segundo número debe ser el Mayor!\nIntroduce el primer numero: "))
        n2 = int(input("Introduce el segundo número: "))
    if n1 < n2:
        print("Los números del intervalo son: ")
        for x in range(n1 + 1, n2):
            print(x, end=' ')


if __name__ == '__main__':
    main()
