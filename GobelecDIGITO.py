# -*- coding: utf-8 -*-
"""
Rutina para la validacion de Digito Verificador de Gobierno electronico

barras correctas
66463013600090000111070000000000002052303064684590
66465010401521200021301201835412002052303000000360
66463013600090000111070000000000002052303064692540
66463013600090000111070000000000002052303064692572
66463013600180000111070000000000002062303064718757
66465010405849800021301000233437782052303000001586
66465010423190800021301000233437782052303000001595
66465010406750800021301000233437782052303000001604
66008130500777000021071336450416292052303000001960
66026080200171700021071306149909412002303000000036
66463013600301000111070000000000002062303064752428
66026080204549300021071306908270652052303000000621
66026080200550900021071306345796282052303000000292
66026080203505500021071307082938022052303000000451
66026080200819500021071306559650052052303000000398
66026080210101500021071306858596172052303000000448
66026080200860300021071307108537772052303000000394
66026080201543700021071307096509272052303000000416
66026080200346834021071306972468232052303000000454
66026080201880300021071305718401262052303000000521
66026080200178568021071337152302892052303000000381
66026080202271300021071307144697422052303000000436
5500802011122233300020011271905732871932103000000907
5500802020987654125021191271905732871932103000000892
5500416021122233300021071271905732871932103000000878



"""

def calcularDigitoVerificador(numero):
    bSerie = 1
    producto = 0
    for i in range(len(numero)):
        value = int(numero[i]) * bSerie
        producto = producto + value
        print(numero[i])
        print(bSerie)
        if bSerie == 1:
            bSerie = 3
        elif bSerie == 3:
            bSerie = 9
        elif bSerie == 9:
            bSerie = 7
        elif bSerie == 7:
            bSerie = 1
        
        print(producto)
        print("//")
    digito = 0
    digito = producto // 2
    print(digito)
    return str(digito)[-1]

def verificarDigito(barra):
    digito=barra[-1]
    print(digito)
    long = int(len(barra)-1)
    print(long)
    resultado =999
    if digito == calcularDigitoVerificador(barra[0:long]): 
         resultado = 0 
    return resultado  

barra = "5500416021122233300021071271905732871932103000000878"
resultado = verificarDigito(barra)
print("resulado", resultado)  # Imprime el dígito verificador