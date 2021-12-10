def main():
    for x in range(1, 1000):
        if x % 8 == 0:
            print(x, end=', ')

#con lista
    ocho = [x for x in range(1001) if x % 8 == 0]
    print(ocho)

if __name__ == '__main__':
    main()