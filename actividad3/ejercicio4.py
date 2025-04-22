distancia_recorrida = float(input("Ingrese los kilometros recorridos: "))
litros_consumidos = float(input("Ingrese los litros que ha consumido: "))
precio_litro = float(input("Ingrese el precio unitario del litro: "))

rendimiento = distancia_recorrida / litros_consumidos
gasto_total_combustible = litros_consumidos * precio_litro

print(f"""{"Distancia recorrida":<31} {distancia_recorrida:>3}
{"Litros consumidos":<31} {litros_consumidos:>3}
{"Precio por litro:":<31} {precio_litro:>3}
{"Rendimiento del vehículo:":<31} {rendimiento:>3.2f}
{"Gasto total del combustible:":<31} {gasto_total_combustible:>3.2f}""")