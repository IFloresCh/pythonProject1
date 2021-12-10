def main():
##sin lista
    for x in range(1, 1001):
        if '6' in str(x):
            print(x, end=', ')
#######################################
    lista = [x for x in range(1, 1001) if '6' in str(x)]
    print(lista)


if __name__ == '__main__':
    main()
