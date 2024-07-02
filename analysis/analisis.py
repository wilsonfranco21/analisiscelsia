from generators.generadorConsumo import generarDatos
import pandas as pd

def analizarDatos():
    datos=generarDatos()
    tabla=pd.DataFrame(datos,columns=["id","referencia","marca","capacidad","consumo","ciudad","responsable"])
    tabla.to_csv("./data/energiaAburraSur.csv",index=False)
analizarDatos()