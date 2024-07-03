import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import QFile, Qt

class IMCApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.dados = []

    def initUI(self):
        self.setWindowTitle('Calculadora de IMC')
        self.setFixedSize(300, 500)
        self.setStyleSheet('background-color: rgb(255, 255, 191);')
        
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout_principal = QVBoxLayout(central_widget)

        # Adicionando uma QLabel para exibir a imagem
        imagem_label = QLabel(self)
        pixmap = QPixmap("C:\\Users\\Aluno\\Desktop\\Projeto IMC\\desenho_lateral.png")  # Substitua pelo caminho correto da sua imagem

        # Redimensionar a imagem para caber na QLabel
        pixmap_redimensionado = pixmap.scaled(300, 300, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio)
        imagem_label.setPixmap(pixmap_redimensionado)

        layout_principal.addWidget(imagem_label)

        # Criando um layout secundário para os widgets de entrada
        layout_entrada = QVBoxLayout()

        self.label_nome = QLabel('Nome:')
        layout_entrada.addWidget(self.label_nome)

        self.input_nome = QLineEdit()
        layout_entrada.addWidget(self.input_nome)

        self.label_peso = QLabel('Peso (kg):')
        layout_entrada.addWidget(self.label_peso)

        self.input_peso = QLineEdit()
        layout_entrada.addWidget(self.input_peso)

        self.label_altura = QLabel('Altura (m):')
        layout_entrada.addWidget(self.label_altura)

        self.input_altura = QLineEdit()
        layout_entrada.addWidget(self.input_altura)

        self.btn_adicionar = QPushButton('Adicionar')
        self.btn_adicionar.clicked.connect(self.adicionar_dados)
        layout_entrada.addWidget(self.btn_adicionar)

        self.btn_calcular = QPushButton('Calcular e Mostrar Resultados')
        self.btn_calcular.clicked.connect(self.calcular_mostrar_resultados)
        layout_entrada.addWidget(self.btn_calcular)

        layout_principal.addLayout(layout_entrada)

        self.resultado_texto = QTextEdit()
        layout_principal.addWidget(self.resultado_texto)

    def adicionar_dados(self):
        nome = self.input_nome.text()
        peso = float(self.input_peso.text())
        altura = float(self.input_altura.text())

        self.dados.append((nome, peso, altura))

        self.input_nome.clear()
        self.input_peso.clear()
        self.input_altura.clear()

        self.resultado_texto.append(f'Dados de {nome} adicionados.')

    def calcular_mostrar_resultados(self):
        if not self.dados:
            self.resultado_texto.append('Nenhum dado para calcular.')
            return

        self.resultado_texto.clear()
        self.resultado_texto.append('Análise de IMC:\n')

        resultados, abaixo, normal, sobrepeso, obesidade, percent_abaixo, percent_normal, percent_sobrepeso, percent_obesidade = analisar_dados(self.dados)

        for nome, imc, classificacao in resultados:
            self.resultado_texto.append(f'{nome}: {classificacao} (IMC: {imc:.2f})')

        self.resultado_texto.append('\nEstatísticas:')
        self.resultado_texto.append(f'Total de pessoas: {len(self.dados)}')
        self.resultado_texto.append(f'Pessoas abaixo do peso: {abaixo} ({percent_abaixo:.2f}%)')
        self.resultado_texto.append(f'Pessoas com peso normal: {normal} ({percent_normal:.2f}%)')
        self.resultado_texto.append(f'Pessoas com sobrepeso: {sobrepeso} ({percent_sobrepeso:.2f}%)')
        self.resultado_texto.append(f'Pessoas com obesidade: {obesidade} ({percent_obesidade:.2f}%)')

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

def main():
    app = QApplication(sys.argv)
    app.setFont(QFont("Times new roman", 10))
    window = IMCApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

