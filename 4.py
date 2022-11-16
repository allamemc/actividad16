#4. Busca un archivo csv en internet y muestra un gráfico circular que muestre los datos

import pandas as pd
import matplotlib.pyplot as plt

datos = pd.read_csv("casasboston.csv")
# datos = datos[["RM","CRIM", "MEDV", "TOWN", "CHAS", "INDUS", "LSTAT"]]
df = datos[["RM", "CRIM", "MEDV", "TOWN", "CHAS"]]

df = datos.rename(columns={
    "TOWN": "CIUDAD",
    "CRIM": "INDICE_CRIMEN",
    "INDUS": "PCT_ZONA_INDUSTRIAL",
    "CHAS": "RIO_CHARLES",
    "RM": "N_HABITACIONES_MEDIO",
    "MEDV": "VALOR_MEDIANO",
    "LSTAT": "PCT_CLASE_BAJA"
})
df.RIO_CHARLES.value_counts().plot.pie()
plt.show()