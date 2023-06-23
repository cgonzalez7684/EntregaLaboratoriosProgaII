def elevarnemeroalapotencia2(numero, potencia):
    calculo= numero**potencia
    return calculo

resultado=elevarnemeroalapotencia2(numero=2, potencia =3)

etiqueta="elevar {0} a la potencia {1} da como resultado {2}"

print(etiqueta.format(2,3, resultado))