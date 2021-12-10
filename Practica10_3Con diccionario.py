def main():
    header = ['Username', 'Department', 'Classroom']
    username = list()
    department = list()
    classroom = list()
    registres = int(input("Cuantos registros quiere introducir: "))

    for i in range(registres):

        username.append(input("Introduce el usuario: "))
        department.append(input("Introduce el departamento: "))
        classroom.append(int(input("Introduce la clase: ")))

    regs = {
        'username': username,
        'department': department,
        'classroom': classroom
    }
    for i in header:
        print(i, end='\t\t|')
    print()
    for i in range(registres):
        print(regs['username'][i] + '\t\t| ' + regs['department'][i] + '\t\t\t| ' + str(regs['classroom'][i]) + '\t\t|')


if __name__ == '__main__':
        main()
