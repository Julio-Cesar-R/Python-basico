
'''import datetime
hora=datetime.time(17,49,50)
print(hora)
dia=datetime.date(2025,10,11)
print(dia.ctime())

print(datetime.date.today().ctime())#fecha actual
print(datetime.datetime.now())
'''
'''from datetime import datetime
mi_fecha=datetime(2025,9,11,12,12,12,2500)
mi_fecha=mi_fecha.replace(month=10)#reemplaza fecha
print(mi_fecha)'''

'''from datetime import date
nacimiento=date(1992,9,11)
defuncion=date(2070,2,3)

vida=defuncion-nacimiento#periodo de tiempo entre dos fechas
print(vida.days/365)'''

'''from _datetime import datetime
hora_despertar=datetime(2022,4,1,9,00,00)
hora_dormir=datetime(2022,4,1,23,00,00)
print(hora_despertar)
print(hora_dormir)
tiempo=hora_dormir-hora_despertar
print(tiempo)'''

#import datetime
#mi_fecha=datetime.date(1999,2,3)

import datetime
hoy=datetime.date.today()
print(hoy)

from datetime import datetime

minutos = datetime.now().minute
print(minutos)