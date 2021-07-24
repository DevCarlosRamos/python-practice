# practice 15 Calcular el Volumen de una Esfera a partir del Radio Dado

from math import pi;

r = float(input('write the radius of esfera... '));
v = 3/4 * pi * r**3;

print('the volumen of esfera is {} metros cubicos'.format(v));