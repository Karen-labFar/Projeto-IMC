# # DESAFIO 05
# Tabela Padrão:
# ·    Abaixo do peso para imc abaixo de 18,5
# ·    Peso normal se o imc estiver entre 18,5 e 24,9:
# ·   Sobrepeso se o imc estiver entre 25 e 29,9
# ·   Obesidade para imc maior que 29,9

print('_________VERSÃO 01 IMC______________') #Lógica simples usando realizando a leitura dos dados e apresentando o resultado.


id_usuario= (input('Digite o nome da pessoa:')),float(input('Digite o peso da pessoa:')),float(input('Digite sua altura: '))

nome = id_usuario[0]
peso = id_usuario[1]
altura= id_usuario[2]   
print(nome)
print(peso)
imc = peso/(altura**2)
print(imc)
if imc<18.5:
    print('Abaixo do peso')
elif imc>=18 and imc<24.9:
    print('Peso normal')
elif imc>=24.9 and imc<29.9:
    print('Sobrepeso')
else:
    print('Obesidade')

# print('____________________FIM______________________')