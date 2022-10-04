peso = float(input('Introduzca su peso en kg: '))
altura = float(input('Introduzca su peso en metros: '))
masa_corporal = peso / (altura**2)
masa_redondeada = round(masa_corporal, 2)
print('Tu indice de masa corporal es '+ str(masa_corporal) +' donde '\
      + str(masa_redondeada) +' es el índice de masa corporal calculado'\
      ' redondeado con dos decimales')
