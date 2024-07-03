# DESAFIO 05
print('_________VERSÃO 02 IMC______________') #Implementar no projeto a possibilidade de realizar quantas análises for preciso através do uso de estrutura de loop. Apresentar no final o total de análises feitas, 
# a quantidade e porcentagem obtida em cada classificação.
nomes =[]
pesos=[]
alturas=[]

while True:
    nome =(input('Digite o nome da pessoa:'))
    peso= float(input('Digite o peso da pessoa:'))
    altura= float(input('Digite a altura: '))
    inserir= int(input('Deseja continuar?\n 1-SIM ou 2-NÃO: '))
    nomes.append(nome)
    pesos.append(peso)
    alturas.append(altura)
    if inserir !=1:
        break

abaixo=[]
normal=[]
sobrepeso=[]
obesidade=[]
total= len(nomes)

for i in range(total):
    imc = pesos[i]/(alturas[i]**2)
    if imc<18.5:
       abaixo.append(nomes[i])
    elif imc>=18 and imc<24.9:
       normal.append(nomes[i])
    elif imc>=24.9 and imc<29.9:
       sobrepeso.append(nomes[i])
    else:
        obesidade.append(nomes[i])
print(total)
print(abaixo, normal, sobrepeso, obesidade)
print('Porcentagens de IMC: ')
print(f'Temos {len(abaixo)} pessoas abaixo do peso e elas representam {len(abaixo)/total*100:.2f}%')
print(f'Temos {len(normal)} pessoas com peso normal e elas representam {len(normal)/total*100:.2f}%')
print(f'Temos {len(sobrepeso)} pessoas com sobrepeso e elas representam {len(sobrepeso)/total*100:.2f}%')
print(f'Temos {len(obesidade)} pessoas com obesidade e elas representam {len(obesidade)/total*100:.2f}%')



# print('____________________FIM______________________')
