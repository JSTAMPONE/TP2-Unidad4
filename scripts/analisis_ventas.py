#Importamos la biblioteca pandas para poder analizar el dataset de ventas
import pandas as pd
#Cargamos el archivo csv en un DataFrame de pandas para poder analizar los datos
df = pd.read_csv("datos/dataset.csv")
#Verificamos que el dataset se cargó correctamente mostrando las primeras 5 filas
print(df.head())
#Calculamos el total de ventas recorriendo la columna "sales_amount" con un ciclo
#for y acumulando cada valor.
total_ventas = 0
for venta in df["sales_amount"]:
    total_ventas += venta
print(f"Ventas totales: {total_ventas}")

print("---")
#Calculamos las ventas mensuales recorriendo la columna "sales_date" con un ciclo for
ventas_por_mes = {}
for i in range(len(df)):
    #Utilizamos el método split para tomar únicamente el mes en la fecha
    mes = df["sales_date"][i].split("-")[1]
    monto = df["sales_amount"][i]
    #A cada mes distinto, le sumamos la cantidad correspondiente a ese mes
    if mes in ventas_por_mes:
        ventas_por_mes[mes] += monto
    else:
        ventas_por_mes[mes] = monto
#Utilizamos un diccionario para mostrar el total de ventas por mes
print("Ventas por mes:")
for mes, total in ventas_por_mes.items():
    print(f"Mes {mes} : {int(total)}")

print("---")
#Utilizando el diccionario de ventas por mes, calculamos el mes con más ventas
#Se declaran las variables iniciales para que al recorrer con el ciclo for
#se puedan actualizar
mes_mayor = None
monto_mayor = 0
for mes, total in ventas_por_mes.items():
    if int(total) > monto_mayor:
        monto_mayor = int(total)
        mes_mayor = mes

print(f"Mes con mayor venta: Mes {mes_mayor} con {monto_mayor} ventas.")