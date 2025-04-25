salario = float(input("Ingrese su salario estimado trabajador: "))

if salario > 3000:
    bono = salario * 0.10
elif salario > 1500 and salario <= 3000:
    bono = salario * 0.05
elif salario <= 1500:
    print ("Usted no tendrá bono")
else:
    bono = 0

print(f"{"Salario: ":<19} {salario:<3}")    
print(f"{"Bono: ":<19} {bono:<3.2f}")
print(f"{"Sueldo total: ":<19} {salario + bono:<3.2f}")