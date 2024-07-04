from generators.generadorTipoProducto import generardorTipoProducto
import pandas as pd

def analizarDatos():
    datos=generardorTipoProducto()
    tabla=pd.DataFrame(datos,columns=["tienda","categoria"])
    tabla.to_csv("./data/tipoProductoDatos.csv",index=False)
analizarDatos()