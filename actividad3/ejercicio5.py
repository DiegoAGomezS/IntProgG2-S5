litros_con_mes = float(input("Ingrese los litros de agua consumidos en un mes en su residencia: "))
cant_personas = int(input("Ingrese la cantidad de personas que habitan la vivienda: "))

consumo_mensual = litros_con_mes / cant_personas
consumo_diario = consumo_mensual / 30

print(f"""{"Consumo total del mes:":<34} {litros_con_mes:>3}
{"Personas habitando la vivienda:":<34} {cant_personas:>3}
{"Consumo mensual:":<34} {consumo_mensual:>3.02f}
{"Consumo diario:":<34} {consumo_diario:>3.02f}""")