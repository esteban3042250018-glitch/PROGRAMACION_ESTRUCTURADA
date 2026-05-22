def borrarPantalla():
    print("\033c")

def ventaAutos(opc,autos,acum_pv):
    borrarPantalla()
   
    while opc == "si":
        
        marca = input("Marca: ").strip().lower()
        origen = input("Origen: ").strip().lower()
        costo = float(input("Costo: "))


        impuesto = 0
        if origen == "alemania":
            impuesto = 0.20
        elif origen == "japon":
            impuesto  = 0.30
        elif origen == "italia":
            impuesto = 0.15
        elif origen == "usa":
            impuesto = 0.08

        imp_vent = costo * impuesto
        precio_venta = costo + imp_vent

        print (f"El impuesto a pagar es: ${imp_vent:.2f}")
        print (f"El precio de venta es: ${precio_venta:.2f}")


        autos+=1
        acum_pv+=precio_venta

        opc = input("¿Desea ingresar otro vehiculo? (si/no): ").strip().lower()
    
    return autos, acum_pv
    


AUTOS = 1
ACUM_PV=0
OPC = "si"
autos,acum_pv = ventaAutos(OPC,AUTOS,ACUM_PV)
print(f"El total de vehiculos ingresados es: {autos-1} \n Y el precio de venta acumulado es: ${acum_pv:.2f}")


