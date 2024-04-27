print("\033[97mPrograma para Controle de Estoque\033[0m\n\n")


'''
Input de Dados
'''
while True:
    while True:
        try:
            codigo=float(input("\nInsira o código do produto: "))

            nome=input("Insira o nome do produto: ")
            desc=input("Insira a descrição do produto: ")
            break   
        except ValueError:
                print("\033[91mErro! O valor deve ser numérico. Tente novamente!\033[0m\n")


    while True:
        try:
            CP=float(input("\nInsira o custo do produto (em R$): ").replace(',','.')) 
            break
        except ValueError:
            print("\033[91mErro! O valor deve ser numérico. Tente novamente!\033[0m\n")

    while True:
        try:  
            CF=float(input("Insira o custo fixo/administrativo (em %): ").replace(',','.').rstrip('%'))
            break
        except ValueError:
            print("\033[91mErro! O valor deve ser numérico. Tente novamente!\033[0m\n")
    

    while True:
        try:
            CV=float(input("Insira a comissão de vendas (em %): ").replace(',','.').rstrip('%'))
            break
        except ValueError:
            print("\033[91mErro! O valor deve ser numérico. Tente novamente!\033[0m\n")
            
                
    while True:
        try:
            IV=float(input("Insira os impostos sobre venda (em %): ").replace(',','.').rstrip('%'))
            break
        except ValueError:
            print("\033[91mErro! O valor deve ser numérico. Tente novamente!\033[0m\n")
        
    while True:
        try:
            ML=float(input("Insira a margem de lucro (em %): ").replace(',','.').rstrip('%'))
            break
        except ValueError:
            print("\033[91mErro! O valor deve ser numérico. Tente novamente!\033[0m\n")   



    '''
    Fórmulas
    '''
    a=CF+CV+IV+ML
    b=1-(a/100)
    PV=CP/b
    RB=PV-CP
    CP2=(CP*100)/PV
    RB2=(100-CP2)
    CF2=(CF/100)*PV
    CV2=(CV/100)*PV
    IV2=(IV/100)*PV
    OC=CF2+CV2+IV2
    OC2=(OC*100)/PV
    rent=RB-OC
    rent2=(rent*100)/PV



    '''
    Devolução de Resultados
    '''

    print("\n\nPreço de Venda: {:.2f} \n".format(PV))

    print("Custo de Aquisição (Fornecedor) {} -> R$ = {:.2f} %\n".format(CP, CP2))

    print("Receita Bruta: {:.2f} -> R$ = {:.2f} %\n".format(RB, RB2))

    print("Custo Fixo/Administrativo: {:.2f} -> R$ = {} %\n".format(CF2, CF))

    print("Comissão de Vendas: {:.2f} -> R$ = {} %\n".format(CV2, CV))

    print("Impostos: {:.2f} -> R$ = {} %\n".format(IV2, IV))

    print("Outros custos: {:.2f} -> R$ = {:.2f} %\n\n".format(OC, OC2))



    '''
    Classificação Rentabilidade
    '''

    try:
        print("Rentabilidade: {:.2f} - R$ = {:.2f} %".format(rent, rent2))

        if rent2>=20:
            print("\033[92mLucro Alto\033[0m")

        if rent2>=10 and rent2<20:
            print("\033[94mLucro Médio\033[0m")

        if rent2>0 and rent2<10:
            print("\033[93mLucro Baixo\033[0m")

        if rent2==0:
            print("Equilíbrio")

        if rent2<0:
            print("\033[91mPrejuízo\033[0m")

    except ValueError:
        print("ERRO! O valor deve ser numérico!")
    
    
    while True:
        cont=input('\nDeseja inserir mais produtos [S/N]? \n').upper()
        if cont not in ["S","N"]:
            print("\033[91mA resposta deve ser S ou N; tente novamente!\033[0m\n")
        else:
            break
    if cont=="N":
        break

print('Obrigado por utilizar este programa!')
    

    