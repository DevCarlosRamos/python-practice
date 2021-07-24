#practice 14 Calcular la Diferencia en Días de Dos Fechas Dadas

from datetime import date;

today = date(2021,7,24);
other_day = date(2027,5,1);

number = other_day - today;

print(number);
print(number.days);