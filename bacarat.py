#aposta
import random as rdm

fichas = int(input('Quantas fichas você tem ?  :'))

#em quem será a aposta
resposta = True
while resposta:
    apostado = input("Qual você acha que será o resultado?:\n       a)Jogador vencerá. \n       b)Mesa Vencerá \n       c)Empate \nDigite a letra da alternativa correspondente: " )
    if apostado != 'a' and apostado != 'b' and apostado != 'c':
        print('Resposta Inválida')
    else:
        resposta = False


#quanto é a aposta
while True :
    aposta = int(input("Quanto é sua aposta ? : "))
    if aposta > fichas:
        print("Saldo Insuficiente")
    if aposta == fichas:
        print('All in !!!')
        break
    if aposta < fichas:
        print("Aposta feita, Boa sorte!")
        break


#dar duas cartas
carta_A = 'A' 
carta_J = 'J'
carta_Q = 'Q'
carta_K = 'K'
carta_10 = 10
lista_cartas = [carta_A,2,3,4,5,6,7,8,9,carta_10,carta_J,carta_Q,carta_K]
mesa1 = lista_cartas[rdm.randint(0,12)]
mesa2 = lista_cartas[rdm.randint(0,12)]
jogador1 = lista_cartas[rdm.randint(0,12)]
jogador2 = lista_cartas[rdm.randint(0,12)]
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
    cartas_jogador.append(lista_cartas[rdm.randint(0,12)]) #adicionar a carta
    print("O jogador adicionou a carta {0}".format(cartas_jogador[len(cartas_jogador)-1]))
    #mudar pra número se for A, J,Q,K
    if cartas_jogador[len(cartas_jogador)-1] =='Q' or cartas_jogador[len(cartas_jogador)-1] =='J' or cartas_jogador[len(cartas_jogador)-1] =='K' or cartas_jogador[len(cartas_jogador)-1] ==10:
        cartas_jogador[len(cartas_jogador)-1] = 0
    if cartas_jogador[len(cartas_jogador)-1] == 'A':
        cartas_jogador[len(cartas_jogador)-1] = 1
    #somar o total denovo
    soma_jogador += cartas_jogador[len(cartas_jogador)-1]

#transformar o jogador se >10 em unidade
i=0
while soma_jogador >= 10:
    soma_jogador -= 10
print("O jogador tem a soma de {0} pontos".format(soma_jogador))



#fazer o mesmo com a mesa
if soma_mesa <= 5 and soma_jogadorpre <=7 : #saber se da mais uma ou não:
    cartas_mesa.append(lista_cartas[rdm.randint(0,12)]) #adicionar a carta
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
if resultado != apostado:
    print("Que pena, você perdeu. Seu novo saldo é de {0}".format(fichas - aposta))

#acertando o resultado

#se jogador 
if resultado == apostado and apostado == 'a' :
    print('Parabéns! Você ganhou {0} fichas. Seu novo saldo é de {1} fichas.'.format(aposta, fichas + aposta ))

#se mesa ganha 
if resultado == apostado and apostado == 'b':
    print('Parabéns! Você ganhou {0} fichas. Seu novo saldo é de {1} fichas.'.format(int(aposta*0.95),int(aposta*0.95)+fichas))

#se empata
if resultado == apostado and apostado == 'c':
    print('Parabéns! Você ganhou {0} fichas. Seu novo saldo é de {1} fichas.'.format(aposta * 8 , aposta * 8 + fichas))