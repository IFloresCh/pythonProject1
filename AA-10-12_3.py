def main():
   app, rep = [], []
   s_app, s_rep, m_app, m_rep, i = 0, 0, 0, 0, 1
   num = int(input("Introduce cuantas notas quiere registrar: "))
   while num < 1:
       num = int(input("Debe ser mayor a 0\nIntroduce cuantas notas quiere registrar: "))

   while i < num + 1:
       note = int(input("Introduce la nota del 0 al 10: "))
       if note in range(5, 11):
           app.append(note)
           i += 1
       elif note in range(0, 5):
           rep.append(note)
           i += 1
       else:
           print("Solo notas del 0 al 10")
   for y in app:
       s_app += y
       m_app = s_app / len(app)
   for z in rep:
       s_rep += z
       m_rep = s_rep / len(rep)

   print("hay", len(app), "aprobados y su media es: ", m_app)
   print("hay", len(rep), "reprobados y su media es: ", m_rep)


if __name__ == '__main__':
   main()
