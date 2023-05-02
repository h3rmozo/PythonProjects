import random
import sys

def formatar_cpf(cpf):
    cpf_formatado = "{}.{}.{}-{}".format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
    return cpf_formatado

qtd_cpf = input("Quantos CPF's deseja gerar? ")
qtd_cpf = int(qtd_cpf)

for i in range(qtd_cpf):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

    cpf_brut = nove_digitos

    cpf_sep = cpf_brut.replace('-', '.').split('.')

    cpf_num = ''.join(cpf_sep)

    cpf_list = list(cpf_num)
    i = 10
    soma = 0
    cpf_valido = True

    prim_char = cpf_num[0]
    rep_prim = prim_char * len(cpf_num)
    if rep_prim == cpf_num:
        cpf_valido = False

    if cpf_valido:
        for num in cpf_list:
            num_int = int(num)
            num_mult = (num_int * i)
            soma += num_mult
            i-=1
            if i < 2: break

        somaX10 = soma * 10

        restoSomaX10 = somaX10 % 11

        if restoSomaX10 > 9:
            restoSomaX10 = 0
        else:
            restoSomaX10 = restoSomaX10
        i = 11
        soma = 0

    cpf_list.append(str(restoSomaX10))

    for num in cpf_list:
        num_int = int(num)
        num_mult = (num_int * i)
        soma += num_mult
        i-=1
        if i < 2: break
    somaX10 = soma * 10

    restoSomaX102 = somaX10 % 11

    if restoSomaX102 > 9:
        restoSomaX102 = 0
    else:
        restoSomaX102 = restoSomaX102
    cpf_list.append(str(restoSomaX102))

    cpf_str = ','.join(cpf_list)

    cpf_ult = cpf_str.replace(',', '')

    cpf_formatado = formatar_cpf(cpf_ult)

    print(cpf_formatado)