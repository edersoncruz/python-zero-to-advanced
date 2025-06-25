from PySide6.QtWidgets import QApplication, QPushButton
import sys

app = QApplication(sys.argv)

botao = QPushButton('Texto do botão')
botao.setStyleSheet('font-size:40px; color:blue')
botao.show()

botao2 = QPushButton('Texto do botão 2')
botao2.show()

app.exec()
