ppos = []
vp = []
pneg = []
vn = []
contgeral = contp = contn = 0

def adc_ppos(contp):
    contp += 1
    ppos.append(str(input('Adicionar ponto \033[36mpositivo\033[m: ')))
    vp.append(int(input('Valor (de 1+ até 3+++): ')))


def adc_pneg(contn):
    contn += 1
    pneg.append(str(input('Adicionar ponto \033[31mnegativo\033[m: ')))
    vn.append(int(input('Valor (de 1+ até 3+++): ')))


def proc_dat():
    somapt = sum(vp)
    somapn = sum(vn)

    print(f'\033[36m\n\n{contp} Pontos Positivos: \033[m')
    for i in range(len(ppos)):
        print(ppos[i])
    print('Total de pontos: ', somapt)

    print(f'\033[31m\n\n{contn} Pontos Negativos: \033[m')
    for j in range(len(pneg)):
        print(pneg[j])
    print('Total de pontos: ', somapn)
    print('\n')

    if contp > contn:
        print('\nPela quantidades de argumentos, vale a pena morar no seu apartamento!')
    else:
        print('\nNão vale!')

    if somapt > somapn:
        print('\nPela quantidade de pontos, vale a pena morar no seu apartamento!\n')
    else:
        print('\nNão vale!\n')

print('\033[35m=' * 40)
print(f'{"Gatinha s2":^40}'.upper())
print(f'{"Vale morar no meu apartamento?":^40}')
print('=' * 40)
print("""\033[m\033[33mPara sair e calcular o
resultado aperte: "0" (zero)\033[m""")

while True:
    aux = int(input(f'\n\nDigite "\033[7;36m1\033[m" para \033[36mponto positivo\033[m e '
                    f'"\033[7;31m2\033[m" para \033[31mponto negativo\033[m: '))

    if aux == 1:
        contp += 1
        adc_ppos(contp)
    elif aux == 2:
        contn +=1
        adc_pneg(contn)
    elif aux == 0:
#        print('Pontos Positivos: ', ppos, vp)
#        print('Pontos Negativos: ', pneg, vn)
        proc_dat()
        break
    contgeral += 1
