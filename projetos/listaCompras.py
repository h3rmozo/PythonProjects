import os
import keyboard
import msvcrt

lista = []
novo_valor = ''
tam_lista = len(lista)
indice_apagar = -1
indice_apagar_int = -1


while True:
    opcao = input('Selecione uma opção\n[i]nserir [a]pagar [l]istar: ')
    # opcao = 'a'
    opcao = opcao.lower()

    if opcao != 'a' and opcao != 'i' and opcao != 'l':
        os.system('cls')
        print('NAO DIGITOU CERTO')
        continue
    elif opcao == 'a':
        cond_indice_valid = False
        if lista != []:
            while not cond_indice_valid:
                indice_apagar = input('Escolha um indice para apagar: ')
                
                try:
                    indice_apagar_int = int(indice_apagar)
                except ValueError:
                    print('VOZE NAO DIGITOU UM NUMERO')
                cond_indice_valid = indice_apagar_int >= 0 and indice_apagar_int <= tam_lista
                if cond_indice_valid:
                    lista.pop(indice_apagar_int)
                    os.system('cls')
                else:
                    print('DIGITA DNV O BGL AI, NMRL')
            os.system('cls')
            continue
        else:
            os.system('cls')
            print('Não há nada para apagar')
            print("Pressione qualquer tecla para voltar...")
            while not msvcrt.kbhit():
                pass
        msvcrt.getch()
    elif opcao == 'i':
        os.system('cls')
        print('Para parar de inserir itens, digite "pare"')
        while novo_valor != 'pare':
            novo_valor = input('Valor: ')
            lista.append(novo_valor)
        lista.pop()
        novo_valor = ''
        continue
    else:
        os.system('cls')
        if lista != []:
            indice = 0
            for item in lista:
                print(indice, item)
                indice += 1
        else:
            print('Não há nada para listar')
        print("Pressione qualquer tecla para voltar")
        while not msvcrt.kbhit():
            pass
        msvcrt.getch()