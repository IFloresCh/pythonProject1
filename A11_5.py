def main():
    vocales = 'éaeiou'
    state = "Practica els problemes de list comprehensions per a ser més Pythonic!"

    for x in vocales:
        state = state.replace(x, "")
    print(state)

#con lista
    voc = [i for i in state if i not in 'éaeiou, ']
    print(voc)


if __name__ == '__main__':
    main()
