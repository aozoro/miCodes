#Creado por Omar de la sota
#correo: aozoro@gmail.com
#fecha: 05/04/2020

def DataFrame_noNames(data):
    from pandas import DataFrame
    dataView = DataFrame(data, index=None, columns=None)
    dataView.index = [""] * len(dataView.index)
    dataView.columns = [""] * len(dataView.columns)
    return dataView