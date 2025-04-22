Algoritmo detectar_ausencia
	Definir dia, mes, ANO, dia_act, mes_act, ANO_ACT Como Entero
	Escribir 'Ingrese la fecha inicial (día, mes, año):'
	Leer dia, mes, ANO
	dia_act <- 22
	mes_act <- 4
	ANO_ACT <- 2025
	Definir dias_transc Como Entero
	Definir mes_transc Como Entero
	Definir ANO_TRANSC Como Entero
	Definir suma_dias Como Entero
	ANO_TRANSC <- ANO_ACT-ANO
	mes_transc <- mes_act-mes
	dias_transc <- dia_act-dia
	Si ANO_TRANSC>0 Entonces
		suma_dias <- 365*ANO_TRANSC
	FinSi
	Si mes_transc>0 Entonces
		suma_dias <- suma_dias+(30+mes_transc)
	FinSi
	Si dias_transc>0 Entonces
		suma_dias <- suma_dias+dias_transc
	FinSi
	Escribir dias_transc
	Escribir mes_transc
	Escribir ANO_TRANSC
	Escribir suma_dias
	Si suma_dias>30 Entonces
		Escribir 'Cuenta inactiva'
	SiNo
		Escribir 'Cuenta activa'
	FinSi
FinAlgoritmo
