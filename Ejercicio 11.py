cuenta = float(input('Cuantos euros quieres ingresar? '))
primero = round(cuenta+(cuenta*4/100), 2)
segundo = round(primero+(primero*4/100),2)
print('El primer año tendras; '+str(primero)+', el segundo; '+str(segundo)+', el tercero; '+str(round(segundo+(segundo*4/100), 2)))
