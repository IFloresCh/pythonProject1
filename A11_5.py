def main():
    vocales = 'aeiou'
    state = "Practica els problemes de list comprehensions per a ser més Pythonic!"

    for x in vocales:
        state = state.replace(x, "")

    print(state)


if __name__ == '__main__':
    main()
