def main():
    count = 0
    state = "Practica els problemes de list comprehensions per a ser més Pythonic!"

    for i in range(0, len(state)):

        if state[i] == " ":
            count += 1

    print("La frase tiene", count, "espacios")


if __name__ == '__main__':
    main()
