def main():
    count = 0
    state = "Practica els problemes de list comprehensions per a ser més Pythonic!"

    for i in range(len(state)):
        if state[i] == " ":
            count += 1

    print("La frase tiene", count, "espacios")
# con listas
    count = [i for i in state if i in ' ']
    print(len(count))




if __name__ == '__main__':
    main()
