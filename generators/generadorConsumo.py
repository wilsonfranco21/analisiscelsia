import random
def generarDatos():
    datos = []
    for i in range(5000):
        dato={}
        id=random.randint(1,10000)
        referencia=random.choice(["ACH01","ACH22","ACH43"])
        marca=random.choice(["kalley","sony","rico"])
        capacidad=random.randint(100,2000)
        consumo=random.randint(100,2000)
        ciudad=random.choice(["Medellin","Envigado","Sabaneta","La estrella","itagui"])
        responsable=random.choice(["Jhon doe","Pedro Perez","Ana Rubio","Carlos Zapata","Martha builes"])
        dato=[id,referencia,marca,capacidad,consumo,ciudad,responsable]
        datos.append(dato)
    return datos

print(generarDatos())