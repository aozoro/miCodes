def FV(nPeriodos,tasa,anualidad=0,valorPresente=0):
    tasa=tasa/100
    sum1 = -valorPresente * (1+tasa)**nPeriodos
    sum2 = -anualidad*(((1+tasa)**nPeriodos-1)/tasa)
    return sum1+sum2

def PV(nPeriodos,tasa,anualidad=0, valorFuturo=0):
    tasa=tasa/100
    sum1 = -valorFuturo*(1+tasa)**(-nPeriodos)
    sum2 = -anualidad*((1-(1+tasa)**(-nPeriodos))/tasa)
    return sum1 +sum2

def PMT(nPeriodos, tasa, valorPresente=0,valorFuturo=0):
    valorPresente=valorPresente+PV(nPeriodos=nPeriodos,tasa=tasa,anualidad=0,valorFuturo=-valorFuturo)
    tasa=tasa/100
    anualidad=-valorPresente*(tasa/(1-(1+tasa)**(-nPeriodos)))
    return anualidad

def IY(nPeriodos,anualidad=0,valorPresente=0,valorFuturo=0):
     pass

def N(tasa,anualidad=0,valorPresente=0,valorFuturo=0):
    pass

def valuacionBonos(tasaCupon, tasaRendimiento, nPeriodos, valorPar=100):
    cupon=tasaCupon*valorPar/100
    valor=-PV(nPeriodos,tasaRendimiento,cupon)+valorPar/(1+tasaRendimiento/100)**nPeriodos
    return valor

def rendimientoActual(tasaCupon,tasaRendimiento,nPeriodos,valorPar=100):
    cupon=tasaCupon*valorPar/100
    rendimientoBono=100*cupon/valuacionBonos(tasaCupon,tasaRendimiento,nPeriodos,valorPar)
    return rendimientoBono

def duracionBono(tasaCupon,tasaRendimiento,nPeriodos):
    valorPar=100
    cupon=tasaCupon
    sum=0
    for i in range(1,nPeriodos+1):
        sum=sum+i*cupon/(1+tasaRendimiento/100)**i
    sum=sum+nPeriodos*valorPar/(1+tasaRendimiento/100)**nPeriodos
    duracionMacaulay=sum/valuacionBonos(tasaCupon,tasaRendimiento,nPeriodos)
    return duracionMacaulay

def volatilidadBono(tasaCupon,tasaRendimiento,nPeriodos):
    duracionModificada=duracionBono(tasaCupon,tasaRendimiento,nPeriodos)/(1+tasaRendimiento/100)
    return duracionModificada

#Ejemplos
#x=valorFuturo()
x=rendimientoActual(6.25,4.3345,16)
y=valuacionBonos(6.25,4.3345,16)
print(x)
print(y)
