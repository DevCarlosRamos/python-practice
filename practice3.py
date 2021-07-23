#practice 3 Obtener la Fecha y Hora Actuales del Sistema con el Módulo datetime

import datetime;

now = datetime.datetime.now();

print(now);

# con esto veremos el tipo de dato
print(type(now));

#con esto cambiamos el formato de la variable como se va ha mostrar
print(now.strftime('%d-%m-%Y %H:%M:%S'));