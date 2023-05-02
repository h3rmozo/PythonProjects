nome = ''
idade = ''
condicao_idade_errada = (idade =='')
condicao_nome_errado = (nome =='')
while condicao_nome_errado:
    nome = input('Digite seu nome: ')
    # nome = 'nicolas'
    condicao_nome_errado = (nome =='')
    
    if condicao_nome_errado:
        print('--------NOME INVALIDO-----------')
        print('--------DIGITE NOVAMENTE--------')


nome_list_sEspaco = nome.split(' ')
nome_s_esp = ''.join(nome_list_sEspaco)
qnt_carac = (len(nome))


while condicao_idade_errada:
    idade = input('Digite sua idade: ')
    # idade = ''
    condicao_idade_errada = (idade =='') or (not idade.isdigit())
    if condicao_idade_errada:
        print('--------IDADE INVALIDA----------')
        print('--------DIGITE NOVAMENTE--------')
print(f'------------------------------------')
print(f'Seu nome é {nome}')
print(f'Você tem {idade} anos')
print(f'Seu nome invertido é {nome[::-1]}')
if not' ' in nome:
    print('Seu nome não contem espaço')
else:
    print('Seu nome contém espaço')
print(f'Seu nome contém ', len(nome_s_esp), 'letras')
print(f'A primeira letra do seu nome é {nome[0]}')
print(f'A Ultima letra do seu nome é {nome[qnt_carac-1]}')