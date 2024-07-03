# DESAFIO 05
print('_________VERSÃO 02 IMC______________') #Implementar no projeto a possibilidade de realizar quantas análises for preciso através do uso de estrutura de loop. Apresentar no final o total de análises feitas, 
# a quantidade e porcentagem obtida em cada classificação.
def coleta_dados():
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
    
    return nomes, pesos, alturas

def calculo_imc(pesos,alturas):
   imcs=[]
   for i in range(len(pesos)):
      imc=pesos[i]/(alturas[i]**2)
      imcs.append(imc)
   return imcs
def classific_imc(nomes,imcs):
  abaixo=[]
  normal=[]
  sobrepeso=[]
  obesidade=[]
  total= len(nomes)
  for i in range(total):
    if imcs[i]<18.5:
      abaixo.append(nomes[i])
    elif imcs[i]>=18 and imcs[i]<24.9:
      normal.append(nomes[i])
    elif imcs[i]>=24.9 and imcs[i]<29.9:
      sobrepeso.append(nomes[i])
    else:
      obesidade.append(nomes[i])
      
  return abaixo, normal, sobrepeso, obesidade

def mostrar(abaixo, normal, sobrepeso, obesidade, total):
  print('Porcentagens de IMC: ')
  print(f'Temos {len(abaixo)} pessoas abaixo do peso e elas representam {len(abaixo)/total*100:.2f}%')
  print(f'Temos {len(normal)} pessoas com peso normal e elas representam {len(normal)/total*100:.2f}%')
  print(f'Temos {len(sobrepeso)} pessoas com sobrepeso e elas representam {len(sobrepeso)/total*100:.2f}%')
  print(f'Temos {len(obesidade)} pessoas com obesidade e elas representam {len(obesidade)/total*100:.2f}%')

def main():
  nomes=[]
  pesos=[]
  alturas=[]
  imcs=[]

  while True:
    print('_______MENU_______')
    calculadora_imc=int(input('Escolha uma das opções abaixo:\n 1-Calculadora de IMC \n 2-Verificar a análise dos dados \n 3- Sair\n Sua escolha: '))

    if calculadora_imc ==1:
      nomes, pesos, alturas = coleta_dados()
      imcs = calculo_imc(pesos, alturas)
      print("\nDados coletados com sucesso!")
    
    elif calculadora_imc==2:
      abaixo,normal,sobrepreso,obesidade = classific_imc(nomes,imcs)
      total = len(nomes)
      mostrar(abaixo, normal, sobrepreso, obesidade, total)
    else:
     print('Saindo do programa...')

if __name__ =="__main__":
  main()



# print('____________________FIM______________________')
