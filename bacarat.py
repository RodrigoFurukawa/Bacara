#aposta
import random as rdm


#quantos baralhos
numero_baralhos = True
while numero_baralhos:
    baralhos = int(input('Com quantos baralhos deseja jogar ? 1,6 ou 8  :'))

    if baralhos == 1:
        print('Estamos selecionando o seu baralho')
        numero_baralhos = False
    elif baralhos == 6:
        print('Estamos selecionando os 6 baralhos')
        numero_baralhos = False
    elif baralhos == 8:
        print('Estamos selecionando os 8 baralhos')
        numero_baralhos = False
    else:
        print('Número de baralhos selecionado é inválido.')
        numero_baralhos = True



#quantos jogadores são
while True:
    numjogadores = int(input("Quantos jogadores vão jogar esa rodada ?"))
    if numjogadores<=0:
        print('Número de jogadores inválidos')
    else:
        break
listajogadores = [0] * numjogadores
x = 0
apostado= [0] * numjogadores
aposta = [0] * numjogadores 
fichas = [0] * numjogadores
while x < numjogadores: 
    #em quem será a aposta
    resposta = True
    while resposta:
        apostado[x] = input("Qual você acha que será o resultado?:\n       a)Jogador vencerá. \n       b)Mesa Vencerá \n       c)Empate \nDigite a letra da alternativa correspondente: " )
        if apostado[x] != 'a' and apostado[x] != 'b' and apostado[x] != 'c':
            print('Resposta Inválida')
        else:
            resposta = False
            

    #quanto é a aposta
    fichas[x] = int(input('Quantas fichas você tem ?  :'))
    while True :
        aposta[x] = int(input("Quanto é sua aposta ? : "))
        if aposta[x] > fichas[x]:
            print("Saldo Insuficiente")
        if aposta[x] == fichas[x]:
            print('All in !!!')
            break
        if aposta[x] < fichas[x] and aposta[x] > 1:
            print("Aposta feita, Boa sorte!")
            break
        if aposta[x] <= 1:
            print('Valor mínimo de aposta igual a 2.')
    if x < numjogadores-1:
        print("Próximo jogador")
    x += 1
    



#dar duas cartas
carta_A = 'A' 
carta_J = 'J'
carta_Q = 'Q'
carta_K = 'K'
carta_10 = 10
lista_cartas = ([carta_A,2,3,4,5,6,7,8,9,carta_10,carta_J,carta_Q,carta_K]*4) * baralhos

mesa1rdm = rdm.randint(0,51*baralhos+baralhos-1)
mesa2rdm = rdm.randint(0,51*baralhos+baralhos-1)
jogador1rdm = rdm.randint(0,51*baralhos+baralhos-1)
jogador2rdm = rdm.randint(0,51*baralhos+baralhos-1)

#garantirr que a mesma carta(nao no sentido de valor mas fisicamente a mesma carta) seja tirada duas vezes 
while(mesa1rdm == mesa2rdm or mesa1rdm == jogador1rdm or mesa1rdm == jogador2rdm):
    mesa1rdm = rdm.randint(0,51*baralhos+baralhos-1)
while(mesa2rdm == jogador1rdm or mesa2rdm == jogador2rdm or mesa2rdm == mesa1rdm):
    mesa2rdm = rdm.randint(0,51*baralhos+baralhos-1)
while(jogador1rdm == mesa1rdm or jogador1rdm == mesa2rdm or jogador1rdm == jogador2rdm):
    jogador1rdm = rdm.randint(0,51*baralhos+baralhos-1)
while(jogador2rdm == mesa1rdm or jogador2rdm == mesa2rdm or jogador2rdm == jogador1rdm):
    jogador2rdm = rdm.randint(0,51*baralhos+baralhos-1)

#dar valor às cartas
mesa1 = lista_cartas[mesa1rdm]
mesa2 = lista_cartas[mesa2rdm]
jogador1 = lista_cartas[jogador1rdm]
jogador2 = lista_cartas[jogador2rdm]

#mostrar as quatro cartas viradas
print('As cartas da mesa são: {0} e {1} \nAs cartas do jogador são : {2} e {3}'.format(mesa1,mesa2,jogador1,jogador2))

#transformar A,J,Q,K em números e zerar 10
lista_viradas = [mesa1,mesa2,jogador1,jogador2]
i=0
for carta in lista_viradas:
    if carta == 'A':
        lista_viradas[i] = 1
    if carta == 'J':
        lista_viradas[i] = 0
    if carta == 'Q':
        lista_viradas[i] = 0
    if carta == 'K':
        lista_viradas[i] = 0
    if carta == 10:
        lista_viradas[i] = 0
    i+=1

#somar as cartas
soma_mesa = lista_viradas[0] + lista_viradas[1]
soma_jogador = lista_viradas[2] + lista_viradas[3]
lista_somas=[soma_mesa,soma_jogador]


soma_mesa = lista_somas[0]
# nao deixar ser mais que 10
while soma_mesa >= 10: 
    soma_mesa -= 10
soma_mesapre = soma_mesa 
cartas_mesa = [soma_mesa]


soma_jogador = lista_somas[1]
soma_jogadorpre = soma_jogador
# nao deixar ser mais que 10
while soma_jogador >= 10: 
    soma_jogador -= 10
soma_jogadorpre = soma_jogador
cartas_jogador = [soma_jogador]

#adicionar cartas

if soma_jogador <= 5 and soma_mesapre <=7 : #saber se da mais uma ou não:
    cartas_jogador.append(lista_cartas[rdm.randint(0,51*baralhos+baralhos-1)]) #adicionar a carta
    print("O jogador adicionou a carta {0}".format(cartas_jogador[len(cartas_jogador)-1]))
    #mudar pra número se for A, J,Q,K
    if cartas_jogador[len(cartas_jogador)-1] =='Q' or cartas_jogador[len(cartas_jogador)-1] =='J' or cartas_jogador[len(cartas_jogador)-1] =='K' or cartas_jogador[len(cartas_jogador)-1] ==10:
        cartas_jogador[len(cartas_jogador)-1] = 0
    if cartas_jogador[len(cartas_jogador)-1] == 'A':
        cartas_jogador[len(cartas_jogador)-1] = 1
    terceira_carta = cartas_jogador[len(cartas_jogador)-1]
    #somar o total denovo
    soma_jogador += cartas_jogador[len(cartas_jogador)-1]

#transformar o jogador se >10 em unidade
i=0
while soma_jogador >= 10:
    soma_jogador -= 10
print("O jogador tem a soma de {0} pontos".format(soma_jogador))


dacarta = False
#fazer o mesmo com a mesa
if soma_mesa <=5 and (soma_jogadorpre <=7) : #saber se da mais uma ou não
    dacarta = True
    if soma_mesa == 3 and terceira_carta == 8:
        dacarta = False
    if soma_mesa == 4:
        if terceira_carta ==0:
            dacarta = False
        if terceira_carta == 1:
            dacarta = False
        if terceira_carta == 8:
            dacarta = False
        if terceira_carta == 9:
            dacarta = False
    if soma_mesa == 5:
        if terceira_carta <=3:
            dacarta = False
        if terceira_carta == 8:
            dacarta = False
        if terceira_carta == 9:
            dacarta = False

if dacarta:
    cartas_mesa.append(lista_cartas[rdm.randint(0,51*baralhos+baralhos-1)]) #adicionar a carta
    print("A mesa adicionou a carta {0}".format(cartas_mesa[len(cartas_mesa)-1]))
    #mudar pra número se for A,J,Q,K e zerar 10
    if cartas_mesa[len(cartas_mesa)-1] =='Q' or cartas_mesa[len(cartas_mesa)-1] =='J' or cartas_mesa[len(cartas_mesa)-1] =='K' or cartas_mesa[len(cartas_mesa)-1] ==10:
        cartas_mesa[len(cartas_mesa)-1] = 0
    if cartas_mesa[len(cartas_mesa)-1] == 'A':
        cartas_mesa[len(cartas_mesa)-1] = 1
    #somar o total denovo
    soma_mesa += cartas_mesa[len(cartas_mesa)-1]

#transformar a mesa se >10 em unidade
i=0
while soma_mesa >= 10:
    soma_mesa -= 10

print("A mesa tem a soma de {0} pontos".format(soma_mesa))


#quem ganhou
if soma_mesa > soma_jogador:
    resultado = 'b'
    print('A mesa ganhou!')
if soma_mesa < soma_jogador:
    resultado = 'a'
    print('O jogador ganhou!')
if soma_mesa == soma_jogador:
    resultado = 'c'
    print('Foi um empate!')
#errou o resultado
v = 0
while v  < numjogadores: 
    if resultado != apostado[v]:
        print("Que pena o jogador nuúmero {1} perdeu. Seu novo saldo é de {0}".format(fichas[v] - aposta[v], v ))
    v=v+1

#acertando o resultado

#se jogador acerta e ganha
i = 0

while i < numjogadores:
    if resultado == apostado[i] and apostado[i] == 'a' :
        if baralhos == 1:
            print('Parabéns! O jogador {1} ganhou . Seu novo saldo é de {0} fichas.'.format( fichas[i] + int(aposta[i] - aposta[i]* 0.0129) , i))
        if baralhos == 6 or baralhos == 8:
            print('Parabéns! O jogador {1} ganhou . Seu novo saldo é de {0} fichas.'.format( fichas[i] + int(aposta[i] - aposta[i]* 0.0124) , i))


    #se mesa ganha 
    if resultado == apostado[i] and apostado[i] == 'b':
        if baralhos == 1:
            print('Parabéns! O jogador {1} ganhou . Seu novo saldo é de {0} fichas.'.format(int( int(aposta[i]*0.95) - aposta[i]*0.95 * 0.0101  )+ fichas[i] , i))
        if baralhos == 6 or baralhos == 8:
            print('Parabéns! O jogador {1} ganhou . Seu novo saldo é de {0} fichas.'.format(int( int(aposta[i]*0.95) - aposta[i]*0.95 * 0.0106  )+ fichas[i] , i))



    #se empata
    if resultado == apostado[i] and apostado[i] == 'c':
        if baralhos ==1 :
            print('Parabéns! O jogador {1} ganhou . Seu novo saldo é de {0} fichas.'.format(int(aposta[i] * 8 - (aposta[i] * 8)* 0.1575)  + fichas[i], i))
        if baralhos ==6 :
            print('Parabéns! O jogador {1} ganhou . Seu novo saldo é de {0} fichas.'.format(int(aposta[i] * 8 - (aposta[i] * 8)* 0.1444)  + fichas[i], i))
        if baralhos ==8 :
            print('Parabéns! O jogador {1} ganhou . Seu novo saldo é de {0} fichas.'.format(int(aposta[i] * 8 - (aposta[i] * 8)* 0.1436)  + fichas[i], i))    
    
    i+=1
# comisssao ja foi calculada no novo saldo
    
