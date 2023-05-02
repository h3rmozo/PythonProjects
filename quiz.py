import string
import os
import msvcrt
import sys
import subprocess

texto = '''
 ___   ____   ____   ____   ____   ____  ___     ___  
/   \ |    \ |    \ |    | /    | /    ||   \   /   \ 
|     ||  o  )|  D  ) |  | |   __||  o  ||    \ |     |
|  O  ||     ||    /  |  | |  |  ||     ||  D  ||  O  |
|     ||  O  ||    \  |  | |  |_ ||  _  ||     ||     |
|     ||     ||  .  \ |  | |     ||  |  ||     ||     |
 \___/ |_____||__|\_||____||___,_||__|__||_____| \___/ 
'''
print(texto)


perguntas = [
    {
        'Pergunta': 'Qual é o valor de y na equação 4y + 9 = 33?',
        'Opções': ['3', '4', '5', '6'],
        'Resposta': 'd',
     },
    {
        'Pergunta': 'Qual é o valor de x na equação 2x + 3 = 11?',
        'Opções': ['3', '4', '5', '6'],
        'Resposta': 'b',
    },
    {
        'Pergunta': 'Qual é a raiz quadrada de 121?',
        'Opções': ['9', '11', '13', '15'],
        'Resposta': 'b'
    },
    {
        'Pergunta': 'Qual é o resultado da expressão 3^4?',
        'Opções': ['6', '9', '12', '81'],
        'Resposta': 'd'
    },
    {
        'Pergunta': 'Qual é o valor de x na equação 4x + 9 = 21?',
        'Opções': ['2', '3', '4', '5'],
        'Resposta': 'b'
    },
    {
        'Pergunta': 'Qual é o valor de y na equação 6y - 8 = 22?',
        'Opções': ['3', '4', '5', '6'],
        'Resposta': 'c'
    },
    {
        'Pergunta': 'Qual é o resultado da expressão 9 * 8 / 12?',
        'Opções': ['6', '8', '10', '12'],
        'Resposta': 'a'
    },
    {
        'Pergunta': 'Qual é o valor de x na equação 3x - 2 = 7?',
        'Opções': ['1', '2', '3', '4'],
        'Resposta': 'c'
    },
    {
        'Pergunta': 'Qual é o valor de y na equação 2y + 5 = 19?',
        'Opções': ['7', '8', '9', '10'],
        'Resposta': 'a'
    },
    {
        'Pergunta': 'Qual é o resultado da expressão 12 - 4 * 2 + 6?',
        'Opções': ['4', '6', '8', '10'],
        'Resposta': 'd'
    },
]

perguntasGeo = [
    {
'Pergunta': 'Qual é o continente do Brasil?',
'Opções': ['América do Norte', 'América do Sul', 'Europa', 'África'],
'Resposta': 'b'
},

{
'Pergunta': 'Qual é o país que faz fronteira com o Brasil ao norte?',
'Opções': ['Argentina', 'Paraguai', 'Uruguai', 'Venezuela'],
'Resposta': 'd'
},

{
'Pergunta': 'Qual é o maior oceano do mundo?',
'Opções': ['Atlântico', 'Índico', 'Pacífico', 'Ártico'],
'Resposta': 'c'
},

{
'Pergunta': 'Qual é o nome do deserto que fica na região nordeste do Brasil?',
'Opções': ['Sahara', 'Atacama', 'Gobi', 'Lençóis Maranhenses'],
'Resposta': 'd'
},

{
'Pergunta': 'Qual é a capital do Brasil?',
'Opções': ['São Paulo', 'Rio de Janeiro', 'Brasília', 'Belo Horizonte'],
'Resposta': 'c'
},

{
'Pergunta': 'Qual é o rio mais extenso do mundo?',
'Opções': ['Nilo', 'Amazonas', 'Yangtze', 'Mississippi'],
'Resposta': 'b'
},

{
'Pergunta': 'Qual é a cordilheira mais extensa do mundo?',
'Opções': ['Andes', 'Himalaia', 'Alpes', 'Rockies'],
'Resposta': 'a'
},

{
'Pergunta': 'Qual é o nome do maior lago da América do Sul?',
'Opções': ['Titicaca', 'Maracaibo', 'Paraná', 'Maior Lago'],
'Resposta': 'a'
},

{
'Pergunta': 'Qual é o nome do maior planalto do Brasil?',
'Opções': ['Planalto Central', 'Serra do Mar', 'Serra da Mantiqueira', 'Serra do Espinhaço'],
'Resposta': 'a'
},

{
'Pergunta': 'Qual é o país que tem a maior população do mundo?',
'Opções': ['Estados Unidos', 'China', 'Índia', 'Brasil'],
'Resposta': 'c'
},
]

letras = list(string.ascii_uppercase)
varLetra = 0
contadorCertas = 0
totalPerguntas = 0
escolhida = []
materia = 0

def limpar_linha():
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")

def subir_tela():
    for i in range(100):
        print()

os.system('cls')
print('----------- QUIZ PERGUNTAS -----------')
print()
print('Escolha a matéria...')

while materia not in ['1', '2']:
    materia = input('matemática(1) ou geografia(2)? ')
    limpar_linha()

if materia == '2':
    perguntas = perguntasGeo

for pergunta in perguntas:
    totalPerguntas += 1

invalido = True

respondidas = 0

while invalido == True:
    numQuestao = 1
    os.system('cls')
    for pergunta in perguntas:
        resposta = pergunta['Resposta'].upper()
        questao = pergunta['Pergunta']
        varLetra = 0
        print(f'{numQuestao}/{totalPerguntas} {questao}')
        numQuestao += 1
        print()
        for opcao in (pergunta['Opções']):
            print(f'{letras[varLetra].upper()}) {opcao}')
            varLetra += 1
        print()

        print('para desistir digite "x"')
        

        escolha = input('Escolha uma opção: ')
        escolha = escolha.upper()

        
        print()

        letrasAlternativas = letras[0:varLetra]
        letrasAlternativas.append('X')

        while escolha not in letrasAlternativas:
            invalido = True
            escolha = input('Alternativa inválida. Escolha uma opção valida: ').upper()
            limpar_linha()


       
        invalido = False
        if escolha == 'X':
            os.system('cls')
            escolhida.append(escolha)
            break
        index = letrasAlternativas.index(escolha)
        escolhida.append(escolha)
        if resposta == escolha:
            contadorCertas += 1
            respondidas += 1
            os.system('cls')
        else:
            respondidas += 1
            os.system('cls')

print(f'Você acertou {contadorCertas} de {respondidas}')
print()

varEscolhida = 0
numQuestao = 1

if respondidas != 0:
    for pergunta in perguntas:
        resposta = pergunta['Resposta'].upper()
        questao = pergunta['Pergunta']
        varLetra = 0
        print(f'{numQuestao}/{totalPerguntas} {questao}')
        for opcao in (pergunta['Opções']):
                print(f'{letras[varLetra].upper()}) {opcao}')
                varLetra += 1
        print(f"A resposta é '{resposta}'")
        alternativaEscolhida = escolhida[varEscolhida]
        if resposta == alternativaEscolhida:
            print('Você acertou')
        elif alternativaEscolhida == 'X':
            ...
        else:
            print(f"Você errou. Sua resposta foi '{escolhida[varEscolhida].upper()}'")
        print()
        varEscolhida += 1
        numQuestao += 1
        if 'X' in escolhida:
            print('"Nossa maior fraqueza está em desistir. O caminho mais certo de vencer é tentar mais uma vez." Thomas Edison')
            print()

        if numQuestao > respondidas:
            break
        
        if numQuestao == 6:
            print('Pressione algo para ir para a próxima pagina...')
            msvcrt.getche()
            os.system('cls')
            continue
    if respondidas == 10:
        print(texto)
else:
    print('"Nossa maior fraqueza está em desistir. O caminho mais certo de vencer é tentar mais uma vez." Thomas Edison')
    print()



