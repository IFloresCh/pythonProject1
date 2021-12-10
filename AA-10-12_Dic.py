# demanar quants planetas es volen introduir i per cada planeta, demanar:
# -nom
# -pes
# -diametre
# -distancia a la tierra
def main():
    header = ['Nombre', 'Peso', 'Diametro', 'Distancia a la tierra']
    nom = list()
    pes = list()
    diam = list()
    dist = list()
    registres = int(input("Cuantos planetas quiere introducir: "))

    for i in range(registres):
        nom.append(input("Introduce el Nombre: "))
        pes.append(int(input("Introduce el peso: ")))
        diam.append(int(input("Introduce el diametro: ")))
        dist.append(int(input("Introduce la distancia a la tierra: ")))

    regs = {
        'nom': nom,
        'pes': pes,
        'diam': diam,
        'dist': dist
    }
    #    for i in header:
    #        print(i, end='\t\t\t|')
    #    print()
    #    for i in range(registres):
    #        print(regs['nom'][i] + '\t\t\t| ' + str(regs['pes'][i]) + '\t\t\t| ' + str(regs['diam'][i]) + '\t\t\t|' + str(regs['dist'][i]) + '\t\t|')

    print("{:<20}| {:<20}| {:<20}| {:<20}|".format('Nombre', 'Peso', 'Diametro', 'Distancia a la tierra'))
    for x in range(registres):
        print("{:<20}| {:<20}| {:<20}| {:<20}|".format(nom[x], pes[x], diam[x], dist[x]))

if __name__ == '__main__':
    main()
