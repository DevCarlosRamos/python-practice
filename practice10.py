# practice 10 Solicitar al Usuario un Número n y Calcular n + nn + nnn

# 3 + 33 + 333 = 369

n = input('write the value from n ...');

nn = int('{}{}'.format(n,n));
nnn = int('%s%s%s'%(n,n,n));
n = int(n);

suma = n+nn+nnn;

print(suma);

