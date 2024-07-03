def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return 'Abaixo do peso'
    elif 18.5 <= imc < 25.0:
        return 'Peso normal'
    elif 25.0 <= imc < 30.0:
        return 'Sobrepeso'
    else:
        return 'Obesidade'

def analisar_dados(dados):
    resultados = []
    total = len(dados)
    abaixo = 0
    normal = 0
    sobrepeso = 0
    obesidade = 0

    for nome, peso, altura in dados:
        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)
        resultados.append((nome, imc, classificacao))

        if classificacao == 'Abaixo do peso':
            abaixo += 1
        elif classificacao == 'Peso normal':
            normal += 1
        elif classificacao == 'Sobrepeso':
            sobrepeso += 1
        elif classificacao == 'Obesidade':
            obesidade += 1

    percent_abaixo = (abaixo / total) * 100 if total > 0 else 0
    percent_normal = (normal / total) * 100 if total > 0 else 0
    percent_sobrepeso = (sobrepeso / total) * 100 if total > 0 else 0
    percent_obesidade = (obesidade / total) * 100 if total > 0 else 0

    return resultados, abaixo, normal, sobrepeso, obesidade, percent_abaixo, percent_normal, percent_sobrepeso, percent_obesidade

