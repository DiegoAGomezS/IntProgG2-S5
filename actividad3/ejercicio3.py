capital_inicial = float(input("Ingrese el capital inicial: "))
interes_anual = float(input("Ingrese en porcentaje la tasa de interés anual: "))
años = int(input("Ingrese los años transcurridos: "))

tasa = interes_anual / 100
valor_anual = (1 + tasa) ** años
monto_final = capital_inicial * valor_anual
interes_ganado = monto_final - capital_inicial

print(f"""{"Capital inicial":<21} {capital_inicial:>3}
{"Tasa anual":<21} {tasa:>3}
{"Cantidad de años:":<21} {años:>3}
{"Monto final":<21} {monto_final:>3.2f}
{"Interes ganado:":<21} {interes_ganado:>3.2f}""")