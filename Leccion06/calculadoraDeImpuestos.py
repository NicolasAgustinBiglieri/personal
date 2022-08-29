# Función que calcula el total de un pago incluyendo el impuesto

def calcular_total_pago(pagoSinImpuestos, valorImpuesto):
    return pagoSinImpuestos + pagoSinImpuestos * valorImpuesto / 100


pagoSinImpuestos = float(input('Proporcione el pago sin impuesto: '))
valorImpuesto = float(input('Proporcione el monto del impuesto: '))
pagoTotal = calcular_total_pago(pagoSinImpuestos, valorImpuesto)


print(f'Pago con impuesto: {pagoTotal}')