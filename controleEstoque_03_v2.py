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

def calcular(CodProduto, CP, CF, CV, IV, ML, conexao):
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
            tipoLucro = 'Lucro Alto'
    
        if rent2>=10 and rent2<20:
            print("Lucro Médio")
            tipoLucro = 'Lucro Médio' 
    
        if rent2>0 and rent2<10:
            print("Lucro Baixo")
            tipoLucro = 'Lucro Baixo'

        if rent2==0:
            print("Equilíbrio")
            tipoLucro = 'Equilíbrio'
        
        if rent2<0:
            print("Prejuízo")
            tipoLucro = 'Prejuízo'
        
        select = f"select * from piControleEstoque.Resultados where CodProduto = {CodProduto};"
        cursor = conexao.cursor()
        cursor.execute(select)
        resultados = cursor.fetchall()

        if not resultados:
            cursor = conexao.cursor()
            insert = "INSERT INTO Resultados(CodProduto, PrecoVenda, CustoAquisicao, ReceitaBruta, CustoFixoAdm, ComissaoVendas, Impostos, OutrosCustos, Rentabilidade, TipoLucro) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
            resultado = (CodProduto, PV,CP2, RB2, CF2, CV2, IV2, OC2, rent2, tipoLucro)
            cursor.execute(insert, resultado)
            conexao.commit()

    except ValueError:
        print("ERRO! O valor deve ser numérico!")

def leituraGeral(conexao):
    try:
        select = f"select * from piControleEstoque.Produtos;"
        cursor = conexao.cursor()
        cursor.execute(select)
        resultados = cursor.fetchall()
        if not resultados:
            print("\nNenhum produto encontrado!")
        else:
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

def leituraGeralResultados(conexao):
    try:
        select = f"select * from piControleEstoque.Resultados;"
        cursor = conexao.cursor()
        cursor.execute(select)
        resultados = cursor.fetchall()
        if not resultados:
            print("\nNenhum resultado encontrado!")
        else:
            for resultado in resultados:
                print(f"\nCódigo do Produto: {resultado[1]}")
                print(f"Preço de venda: R${resultado[2]}")
                print(f"Custo aquisição: R${resultado[3]}")
                print(f"Receita Bruta: R${resultado[4]}")
                print(f"Custo Fixo Administrativo: R${resultado[5]}")
                print(f"Comissão de Vendas: R${resultado[6]}")
                print(f"Impostos: R${resultado[7]}")
                print(f"Outros custos: R${resultado[8]}")
                print(f"Rentabilidade: R${resultado[9]}")
                print(f"Tipo de lucro: {resultado[10]}")
    except ValueError:
        print("Digite um valor válido para códigos de produto!")
    if cursor:
        cursor.close()

def leituraECalculo(conexao):
        try:
            while True:
                codigo = int(input("\nDigite o código referente ao produto que deseja obter os resultados: "))
                select = f"select * from piControleEstoque.Produtos where CodProduto = {codigo} limit 1;"
                cursor = conexao.cursor()
                cursor.execute(select)
                resultados = cursor.fetchall()
                if not resultados:
                    print("Código de produto não encontrado!")
                else:
                    for resultado in resultados:
                        calcular(resultado[0], resultado[3], resultado[4], resultado[5], resultado[6],resultado[7], conexao)
                    break

        except ValueError:
            print("Digite um valor válido para códigos de produto!")
        if cursor:
            cursor.close()

def inclusao(conexao):
    try:
        while True:
            codigo=float(input("Insira o código do produto: "))
            if codigo > 9999:
                print("\nCódigo inválido. Digite um código de até 4 digitos!\n")
            else:
                cursor = conexao.cursor()
                selectCodigos = f"select CodProduto from Produtos where CodProduto = {codigo};"
                cursor.execute(selectCodigos)
                resultados = cursor.fetchall()
                if len(resultados)>0:
                    print("Esse código já existe, digite novamente!")
                else:
                    break

        nome=input("Insira o nome do produto: ")
        desc=input("Insira a descrição do produto: ")
    
        while True:
            try:
                CP=float(input("\nInsira o custo do produto (em R$): ").replace(',','.')) 
                break
            except ValueError:
                print("Custo do produto inválido. Digite novamente!")
        while True:
            try:        
                CF=float(input("Insira o custo fixo/administrativo (em %): ").replace(',','.').rstrip('%'))
                break
            except ValueError:
                print("Custo fixo inválido. Digite novamente!")

        while True:
            try:
                CV=float(input("Insira a comissão de vendas (em %): ").replace(',','.').rstrip('%'))
                break
            except ValueError:
                print("Comissão de vendas inválida. Digite novamente!")

        while True:
            try:
                IV=float(input("Insira os impostos sobre venda (em %): ").replace(',','.').rstrip('%'))
                break
            except:
                print("Impostos sobre venda inválidos. Digite novamente!")


        while True:
            try:
                ML=float(input("Insira a margem de lucro (em %): ").replace(',','.').rstrip('%'))
                break
            except:
                print("Margem de lucro inválida. Digite novamente!")
                
        insert = "insert into Produtos (CodProduto, Nome, Descricao, CustoProduto, CustoFixo, ComissaoVendas, Impostos, Rentabilidade) values (%s, %s, %s, %s, %s, %s, %s, %s);"
        produto = (codigo, nome, desc, CP, CF, CV, IV, ML)

        cursor.execute(insert, produto)

        conexao.commit()

        print("\nProduto inserido com sucesso!")

        calcular(codigo,CP,CF,CV,IV,ML, conexao)

    except ValueError:
        print("O valor deve ser numérico!")

    except Error as e:
        print("Erro ao conectar ou executar comando SQL:", e)

def atualizacao(conexao, opcao, tipoAtualizacao, nomeCampo):
    try:
        while True:
            while True:
                try:
                    codigo = int(input("\nDigite o código referente ao produto que deseja atualizar: "))
                    break
                except:
                    print("Código inválido. Digite novamente!")
            select = f"select * from piControleEstoque.Produtos where CodProduto = {codigo} limit 1;"
            cursor = conexao.cursor()
            cursor.execute(select)
            resultados = cursor.fetchall()
            if not resultados:
                print("Código de produto não encontrado!")
            else:
                if opcao == 3:
                    while True:
                        try:
                            novoValor = float(input(f"Digite o novo valor para {tipoAtualizacao}: ").replace(',','.'))
                            break
                        except ValueError:
                            print("Valor digitado inválido. Digite novamente!")
                elif opcao == 4 or opcao == 5 or opcao == 6 or opcao == 7:
                    while True:
                        try:
                            novoValor = float(input(f"Digite o novo valor para {tipoAtualizacao}: ").replace(',','.').rstrip('%'))
                            break
                        except ValueError:
                            print("Valor digitado inválido. Digite novamente!")
                elif opcao == 1 or opcao == 2:
                    novoValor = input(f"Digite o novo valor para {tipoAtualizacao}: ")
                if isinstance(novoValor, str):
                    novoValor = f"'{novoValor}'"
                    update = f'Update Produtos set {nomeCampo} = {novoValor} where CodProduto = {codigo};'
                elif isinstance(novoValor, float):
                    update = f'Update Produtos set {nomeCampo} = {novoValor} where CodProduto = {codigo};'
                for resultado in resultados:
                    cursor = conexao.cursor()
                    cursor.execute(update)
                    conexao.commit()
                    print("\nProduto atualizado!")
                atualizarOutro = input("\nDeseja atualizar este mesmo campo de outro produto? (s/n): ").strip().lower()
                if atualizarOutro != 's':
                    break
                    
    except ValueError:
        print("Digite um valor válido para códigos de produto!")

def menuAtualizacao(conexao):

    print("\nSelecione a opção que deseja atualizar!")
    opcoesAAtualizar = ['Atualizar Nome', \
        'Atualizar Descrição', \
        'Atualizar Custo do Produto', \
        'Atualizar Custo fixo', \
        'Atualizar Comissão de Vendas', \
        'Atualizar Impostos', \
        'Atualizar Rentabilidade', \
        'Finalizar Atualizações']

    nomeCampo = ''
    opcao = -1
    while opcao != 8:
        opcao = int(opcaoEscolhida(opcoesAAtualizar))
        if opcao == 1:
            nomeCampo = 'Nome'
            atualizacao(conexao, 1, opcoesAAtualizar[0].lower(), nomeCampo)
        elif opcao == 2:
            nomeCampo = 'Descricao'
            atualizacao(conexao, 2, opcoesAAtualizar[1].lower(), nomeCampo)
        elif opcao == 3:
            nomeCampo = 'CustoProduto'
            atualizacao(conexao, 3, opcoesAAtualizar[2].lower(), nomeCampo)
        elif opcao == 4:
            nomeCampo = 'CustoFixo'
            atualizacao(conexao, 4, opcoesAAtualizar[3].lower(), nomeCampo)
        elif opcao == 5:
            nomeCampo = 'ComissaoVendas'
            atualizacao(conexao, 5, opcoesAAtualizar[4].lower(), nomeCampo)
        elif opcao == 6:
            nomeCampo = 'Impostos'
            atualizacao(conexao, 6, opcoesAAtualizar[5].lower(), nomeCampo)
        elif opcao == 7:
            nomeCampo = 'Rentabilidade'
            atualizacao(conexao, 7, opcoesAAtualizar[6].lower(), nomeCampo)
        elif opcao == 8:
            break
        
def exclusao(conexao):
    try:
        while True:
            codigo = int(input("\nDigite o código referente ao produto que deseja excluir: "))
            select = f"select * from piControleEstoque.Produtos where CodProduto = {codigo} limit 1;"
            cursor = conexao.cursor()
            cursor.execute(select)
            resultados = cursor.fetchall()
            if not resultados:
                print("Código de produto não encontrado!")
            else:
                for resultado in resultados:
                    prodAExcluir = resultado[0]
                    cursor = conexao.cursor()
                    delete = f"delete from Produtos where CodProduto = {prodAExcluir}"
                    deleteResultado = f"delete from Resultados where CodProduto = {prodAExcluir}"
                    cursor.execute(deleteResultado)
                    cursor.execute(delete)
                    conexao.commit()
                    print(f"Produto com código {prodAExcluir} excluído com sucesso")
                    excluirOutro = input("\nDeseja excluir outro produto? (s/n): ").strip().lower()
                    if excluirOutro != 's':
                        break
    except ValueError:
            print("Digite um valor válido para códigos de produto!")
    if cursor:
        cursor.close()


def main():
    menu = ['Leitura Geral de Dados', 'Leitura e cálculo de dados', 'Inclusão de Produto', 'Atualização', 'Exclusão', 'Leitura de resultados', 'Sair do Programa']
    
    conexao = obtemConexaoComMySQL('localhost', 'root', 'Julia.kimura071203', 'picontroleestoque') 

    if not conexao:
        print("Falha ao conectar ao banco de dados. Encerrando o programa.")
        return
    
    print("\nPrograma para Controle de Estoque")
    opcao = -10
    while opcao != 7:
        opcao = int(opcaoEscolhida(menu))
        if opcao == 1:
            leituraGeral(conexao)
        if opcao == 2:
            leituraECalculo(conexao)
        elif opcao == 3:
            inclusao(conexao)
        elif opcao == 4:
            menuAtualizacao(conexao)
        elif opcao == 5:
            exclusao(conexao)
        elif opcao == 6:
            leituraGeralResultados(conexao)
        elif opcao == 7:
            break

    if conexao and conexao.is_connected():
        conexao.close()
    
    print("Obrigada por usar este programa!")


if __name__ == "__main__":
    main()