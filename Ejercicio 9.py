inversion = float(input('Cuantos euros quiere invertir? '))
interes = float(input('Que porcentaje de interes tiene la inverison? '))
tiempo = float(input('Durante cuantos años?'))
print('Vas a obtener '+str(inversion+(inversion*tiempo*(interes/100)))+'€')