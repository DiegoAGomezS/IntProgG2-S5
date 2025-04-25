calificacion = float(input("Ingrese su calificación (0-10): "))

if calificacion >= 9 and calificacion <= 10:
    print("Usted tiene una A")
elif calificacion >= 7 and calificacion <= 8:
    print("Usted tiene una B")
elif calificacion >= 5 and calificacion <= 6:
    print("Usted tiene una C")
elif calificacion >= 3 and calificacion <= 4:
    print("Usted tiene una D")
elif calificacion >= 0 and calificacion <= 2:
    print("Usted tiene una F")
else:
    print("Error. Su calificación no es válidad")