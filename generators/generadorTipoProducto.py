import random

def generardorTipoProducto():
     
    productos=["Musica","Tv","App","Pc","Celulares","tablets","Accesorios"]
    data=[]

    for producto in productos: 
        tienda={}
        categoria=random.choice(["plus","mega","basic"])
        tienda=[producto,categoria]   
        data.append(tienda)    

    return data

print (generardorTipoProducto())