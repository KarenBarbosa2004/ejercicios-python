Descuento=0 
Compra=int (input("Digite el valor de la compra"))
print("El valor de la compra ingresada es", Compra)
if Compra>=50.000:
    print("participa en descuento")
    colorbalota=str (input("Ingrese el color de la boleta: "))
    mayuscula= colorbalota.upper ()
    match mayuscula:
        case 'ROJO':
            Descuento=100

        case 'VERDE':
            Descuento=50

        case 'BLANCO':
            Descuento=30

        case 'NEGRO':
            Descuento=20

        case 'AMARILLO':
            Descuento=10

    totalfloat = (Compra - ((Compra * Descuento)/ 100))

else:
    Descuento= 0
    total= Compra 
    print ("No aplica al descuento")



print ("Valor del descuento=", Descuento, "%")
print("El valor total a pagar es =", total)