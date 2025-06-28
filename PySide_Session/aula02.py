# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#   -> show
# -> exec

from PySide6.QtWidgets import (
 QApplication, QPushButton,
 QWidget, QGridLayout, QMainWindow
)
from PySide6.QtCore import Slot
import sys

app = QApplication(sys.argv)
# Criar o Layout Central com QMainWindow
window = QMainWindow()
# Criar o layout Central
central_widget = QWidget()
# Conecta o window com o central widget
window.setCentralWidget(central_widget)

window.setWindowTitle('Minha janela')

botao1 = QPushButton('Texto do botão 1')
botao1.setStyleSheet('font-size:40px; color:blue')

botao2 = QPushButton('Texto do botão 2')
botao2.setStyleSheet('font-size:20px; color:blue')

botao3 = QPushButton('Texto do botão 3')
botao3.setStyleSheet('font-size:10px; color:blue')

# Criar o Widget que pode adicionar outros widgets
layout = QGridLayout()

# Conecta o central com o layout
central_widget.setLayout(layout)

# Add os widgets
layout.addWidget(botao1, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)


@Slot()
def slot_example(status_bar):
    def inner():
        status_bar.showMessage('O Meu slot foi executado')
    return inner


@Slot()
def outro_slot(checked):
    print('Está marcado?', checked)


@Slot()
def terceiro_slot(action):
    def inner():
        outro_slot(action.isChecked())
    return inner


# Status bar
status_bar = window.statusBar()
status_bar.showMessage("Mostrar MSG")

# menu Bar
menu = window.menuBar()
primeiro_menu = menu.addMenu('Primeiro Menu')
primeira_acao = primeiro_menu.addAction('Primeira Ação')
primeira_acao.triggered.connect(slot_example(status_bar))

segunda_action = primeiro_menu.addAction('Segunda Ação')
segunda_action.setCheckable(True)
segunda_action.toggled.connect(outro_slot)
segunda_action.hovered.connect(terceiro_slot(segunda_action))

botao1.clicked.connect(terceiro_slot(segunda_action))


window.show()

# O Loop da aplicação
app.exec()
