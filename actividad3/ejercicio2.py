cantidad_inicial = int(input("Ingrese la cantidad inicial del inventario: "))
cantidad_recibidos = int(input("Ingrese la cantidad de produtos recibidos: "))
cantidad_vendidos = int(input("Ingrese el total de productos vendidos: "))

sumatoria = cantidad_inicial + cantidad_recibidos
inventario_actual = sumatoria + cantidad_vendidos

print(f"""{"Inventario inicial:":<21} {cantidad_inicial:>3}
{"Productos recibidos:":<21} {cantidad_recibidos:>3}
{"Productos vendidos:":<21} {cantidad_vendidos:>3}
{"Inventario actual:":<21} {inventario_actual:>3}""")