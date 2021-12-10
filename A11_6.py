def main():
    state = "Practica els problemes de list comprehensions per a ser més Pythonic!"

    #state = state.split()

    #result = [x for x in state if len(x) < 5]
    #print(result)

    result = [x for x in state.split() if len(x) < 5]
    print(result)


if __name__ == '__main__':
    main()
