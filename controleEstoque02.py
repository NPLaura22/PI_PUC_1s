from mysql.connector import connect

def obtemConexaoComMySQL(servidor, usuario, senha, bd): 
    if obtemConexaoComMySQL.conexao == None:
        obtemConexaoComMySQL.conexao = connect(host=servidor, user=usuario, passwd=senha, database=bd) 
    return obtemConexaoComMySQL.conexao

obtemConexaoComMySQL.conexao = None


def umTexto(solicitacao, mensagem, valido):
    digitouDireito = False
    while not digitouDireito:
        txt = input(solicitacao)

        if txt not in valido:
            print(mensagem, '- Favor redigitar...')
        else:
            digitouDireito = True

    return txt

def opcaoEscolhida(mnu):
    print()
    opcoesValidas = []
    posicao = 0
    while posicao < len(mnu):
        print(posicao + 1, ') ', mnu[posicao], sep='')
        opcoesValidas.append(str(posicao + 1))
        posicao += 1

    print()
    return umTexto('Qual é a sua opção? ', 'Opção inválida', opcoesValidas)

def calcular(CP, CF, CV, IV, ML):
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

    print("\n\nPreço de Venda: {:.2f} \n".format(PV))

    print("Custo de Aquisição (Fornecedor) {} -> R$ = {:.2f} %\n".format(CP, CP2))

    print("Receita Bruta: {:.2f} -> R$ = {:.2f} %\n".format(RB, RB2))

    print("Custo Fixo/Administrativo: {:.2f} -> R$ = {} %\n".format(CF2, CF))

    print("Comissão de Vendas: {:.2f} -> R$ = {} %\n".format(CV2, CV))

    print("Impostos: {:.2f} -> R$ = {} %\n".format(IV2, IV))

    print("Outros custos: {:.2f} -> R$ = {:.2f} %\n\n".format(OC, OC2))

    try:
        print("Rentabilidade: {:.2f} - R$ = {:.2f} %".format(rent, rent2))
        if rent2>=20:
            print("Lucro Alto")
    
        if rent2>=10 and rent2<20:
            print("Lucro Médio")
    
        if rent2>0 and rent2<10:
            print("Lucro Baixo")
    
        if rent2==0:
            print("Equilíbrio")
        
        if rent2<0:
            print("Prejuízo")
        
    except ValueError:
        print("ERRO! O valor deve ser numérico!")

def leituraGeral(conexao):
    try:
        select = f"select * from piControleEstoque.Produtos;"
        cursor = conexao.cursor()
        cursor.execute(select)
        resultados = cursor.fetchall()
        for resultado in resultados:
            print(f"\nCódigo: {resultado[0]}")
            print(f"Nome: {resultado[1]}")
            print(f"Descrição: {resultado[2]}")
            print(f"Custo do Produto: R$ {resultado[3]:.2f}")
            print(f"Custo Fixo: {resultado[4]:.2f}%")
            print(f"Comissão de Vendas: {resultado[5]:.2f}%")
            print(f"Impostos: {resultado[6]:.2f}%")
            print(f"Rentabilidade: {resultado[7]:.2f}%")
    except ValueError:
        print("Digite um valor válido para códigos de produto!")
    if cursor:
        cursor.close()

def leituraECalculo(conexao):
    try:
        codigo = int(input("\nDigite o código referente ao produto que deseja obter os resultados: "))
        select = f"select * from piControleEstoque.Produtos where CodProduto = {codigo} limit 1;"
        cursor = conexao.cursor()
        cursor.execute(select)
        resultados = cursor.fetchall()
        for resultado in resultados:
            calcular(resultado[3], resultado[4], resultado[5], resultado[6],resultado[7])

    except ValueError:
        print("Digite um valor válido para códigos de produto!")
    if cursor:
        cursor.close()

def inclusao(conexao):
    try:
        codigo=float(input("Insira o código do produto: "))
    
        nome=input("Insira o nome do produto: ")
        desc=input("Insira a descrição do produto: ")
    
        CP=float(input("\nInsira o custo do produto (em R$): ").replace(',','.')) 

        CF=float(input("Insira o custo fixo/administrativo (em %): ").replace(',','.').rstrip('%'))

        CV=float(input("Insira a comissão de vendas (em %): ").replace(',','.').rstrip('%'))
    
        IV=float(input("Insira os impostos sobre venda (em %): ").replace(',','.').rstrip('%'))

        ML=float(input("Insira a margem de lucro (em %): ").replace(',','.').rstrip('%'))

        insert = "insert into Produtos (CodProduto, Nome, Descricao, CustoProduto, CustoFixo, ComissaoVendas, Impostos, Rentabilidade) values (%s, %s, %s, %s, %s, %s, %s, %s);"
        produto = (codigo, nome, desc, CP, CF, CV, IV, ML)

        cursor = conexao.cursor()
        cursor.execute(insert, produto)

        conexao.commit()

        print("Produto inserido com sucesso!\n")

        calcular(CP,CF,CV,IV,ML)


    except ValueError:
        print("O valor deve ser numérico!")

    except Error as e:
        print("Erro ao conectar ou executar comando SQL:", e)

def atualizacao(conexao):
    print("Função ainda não implementada")

def exclusao(conexao):
    print("Função ainda não implementada")

def main():
    menu = ['Leitura Geral de Dados', 'Leitura e cálculo de dados', 'Inclusão de Produto', 'Atualização', 'Exclusão', 'Sair do Programa']
    
    conexao = obtemConexaoComMySQL('localhost', 'root', 'NPL_BD*81(PEDRO)', 'piControleEstoque') 

    if not conexao:
        print("Falha ao conectar ao banco de dados. Encerrando o programa.")
        return
    
    print("\nPrograma para Controle de Estoque")
    opcao = -10
    while opcao != 6:
        opcao = int(opcaoEscolhida(menu))
        if opcao == 1:
            leituraGeral(conexao)
        if opcao == 2:
            leituraECalculo(conexao)
        elif opcao == 3:
            inclusao(conexao)
        elif opcao == 4:
            atualizacao(conexao)
        elif opcao == 5:
            exclusao(conexao)
        elif opcao == 6:
            break

    if conexao and conexao.is_connected():
        conexao.close()
    
    print("Obrigada por usar este programa!")


if __name__ == "__main__":
    main()