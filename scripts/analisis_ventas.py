import pandas as pd
df = pd.read_csv("datos/dataset.csv")
print(df.head())

total_ventas = 0
for venta in df["sales_amount"]:
    total_ventas += venta
print(f"Ventas totales: {total_ventas}")
print("---")
ventas_por_mes = {}
for i in range(len(df)):
    mes = df["sales_date"][i].split("-")[1]
    monto = df["sales_amount"][i]
    if mes in ventas_por_mes:
        ventas_por_mes[mes] += monto
    else:
        ventas_por_mes[mes] = monto
print("Ventas por mes:")
for mes, total in ventas_por_mes.items():
    print(f"Mes {mes} : {int(total)}")
print("---")
mes_mayor = None
monto_mayor = 0
for mes, total in ventas_por_mes.items():
    if int(total) > monto_mayor:
        monto_mayor = int(total)
        mes_mayor = mes

print(f"Mes con mayor venta: Mes {mes_mayor} con {monto_mayor} ventas.")