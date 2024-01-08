import os
def processar_resposta(resposta, nome):
    if resposta == '1':
        # Se o usuário escolheu a opção 1, imprime uma mensagem positiva sobre aprender Python
        print('Vale muito a pena aprender Python, {}!'.format(nome))
        print('Pois é a linguagem que mais cresce.')

    elif resposta == '2':
        # Se o usuário escolheu a opção 2, imprime informações sobre o salário médio de cientistas de dados
        print('Ganham em média $30.000 por ano.')

    elif resposta == '3':
        # Se o usuário escolheu a opção 3, imprime informações sobre a média salarial no Brasil
        print('A média salarial no Brasil é de $1.500 por mês.')

    else:
        # Se o usuário escolheu uma opção inválida, imprime uma mensagem de erro
        print('Digite [1], [2] ou [3]')

def start():
    # Solicita o nome do usuário e o saúda
    nome = input('Digite seu nome: ')
    print('Olá, Bem vindo(a), {}'.format(nome))

    while True:  # Inicia um loop infinito para continuar fazendo perguntas até que o usuário escolha sair
        resposta = input(f'O que gostaria de saber hoje?{os.linesep}'
                          f'[1] - Vale a pena aprender Python?{os.linesep}'
                          f'[2] - Quanto ganha um cientista de Dados?{os.linesep}'
                          f'[3] - Qual a média salarial dos brasileiros?{os.linesep}'
                          f'Escolha a opção (1/2/3) ou digite "sair" para encerrar: ')

        if resposta.lower() == 'sair':
            # Se o usuário digitar "sair", encerra o programa
            break
        else:
            # Chama a função processar_resposta para lidar com a escolha do usuário
            processar_resposta(resposta, nome)

if __name__ == '__main__':
    # Inicia o programa chamando a função 'start' quando o script é executado
    start()
