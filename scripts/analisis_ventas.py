import pandas as pd
df = pd.read_csv("datos/dataset.csv")
print(df.head())

total_ventas = 0
for venta in df["sales_amount"]:
    total_ventas += venta
print(f"Ventas totales: {total_ventas}")