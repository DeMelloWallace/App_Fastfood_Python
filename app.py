import os

restaurantes = [
    {'nome':'Big', 'categoria':'Hamburguer', 'ativo':False}, 
    {'nome':'50', 'categoria':'Caseiro', 'ativo':False}, 
    {'nome':'Kendrick', 'categoria':'Mexicana', 'ativo':True}
]

def exibir_nome_do_programa():
    print('Ｓａｂｏｒ Ｅｘｐｒｅｓｓ\n')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulos('Finalizar app')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def exibir_subtitulos(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def opcao_invalida():
    print('Opção inválida\n')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    '''Essa função é responsável é responsável por cadastrar um novo restaurante
    inputs:
    - Nome do restaurante
    - Categoria

    Output:
    -Adiciona um novo restaurante a lista de restaurante


    '''
    exibir_subtitulos('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante{nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante,'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso\n')
    
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''Essa função é responsável por listar todos os restaurantes'''
    exibir_subtitulos('Listando restaurantes: ')
    
    print(f'{'Nome do restaurante'.ljust(20)} | {'categoria'.ljust(20)} | Status')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        #lendo de forma norma: ativado se o termo restaurante for 'ativo', senão 'desativado'
        print(f'{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}\n')

    voltar_ao_menu_principal

def alternar_estado_restaurante():
    '''Essa função é responsável por alternar restaurantes. Para sabermos se está ativo ou desativado.'''
    exibir_subtitulos('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'o restaurante {nome_restaurante} foi desativado com sucesso! '
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    
    voltar_ao_menu_principal

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        #Ou podemos usar a opção opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
            opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()