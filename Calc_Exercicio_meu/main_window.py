from PySide6.QtWidgets import (QMainWindow, QWidget, QGridLayout, QPushButton,
                               QLineEdit, QMessageBox)
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Configurando layout basico
        self.cw = QWidget()
        self.v_layout = QGridLayout()
        self.v_layout.setVerticalSpacing(0)
        self.v_layout.setHorizontalSpacing(0)
        self.v_layout.setContentsMargins(0, 0, 0, 0)
        self.cw.setLayout(self.v_layout)

        self.setCentralWidget(self.cw)
        # Titulo da janela
        self.setWindowTitle('Calculadora')

        # Ajustando o tamanho da janela
        self.resize(415, 500)  # Largura: 400px, Altura: 300px
        self.move(500, 100)    # Posição na tela: X=100px, Y=100px

        # Tela dos calculos
        self.display1 = QLineEdit()
        self.display1.setReadOnly(True)
        self.display1.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.display1.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display1.setFixedHeight(40)
        self.display1.setStyleSheet('font-size: 15px;'
                                    'background: #202124;'
                                    'color: #fff;'
                                    'border: none;'
                                    'border-radius: 10px;'
                                    'padding-right: 10px;'
                                    'padding-left: 10px;')
        self.v_layout.addWidget(self.display1, 0, 1, 1, 4)

        # Tela de exibição
        self.display2 = QLineEdit()
        self.display2.setReadOnly(True)
        self.display2.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display2.setStyleSheet('font-size: 40px;'
                                    'background: #3f4042;'
                                    'color: #fff;'
                                    'border: none;'
                                    'padding: 15px;'
                                    'border-radius: 10px;')
        self.v_layout.addWidget(self.display2, 1, 1, 1, 4)

        # Criando Botões (ajuste as linhas +1 para ficarem abaixo do display)
        self.create_buttons('button1', 'C', '2, 1, 1, 1')
        self.create_buttons('button2', '◀', '2, 2, 1, 1')
        self.create_buttons('button3', '^', '2, 3, 1, 1')
        self.create_buttons('button4', '/', '2, 4, 1, 1')
        self.create_buttons('button5', '7', '4, 1, 1, 1')
        self.create_buttons('button6', '8', '4, 2, 1, 1')
        self.create_buttons('button7', '9', '4, 3, 1, 1')
        self.create_buttons('button8', '*', '4, 4, 1, 1')
        self.create_buttons('button9', '4', '5, 1, 1, 1')
        self.create_buttons('button10', '5', '5, 2, 1, 1')
        self.create_buttons('button11', '6', '5, 3, 1, 1')
        self.create_buttons('button12', '-', '5, 4, 1, 1')
        self.create_buttons('button13', '1', '6, 1, 1, 1')
        self.create_buttons('button14', '2', '6, 2, 1, 1')
        self.create_buttons('button15', '3', '6, 3, 1, 1')
        self.create_buttons('button16', '+', '6, 4, 1, 1')
        self.create_buttons('button17', '+/-', '7, 1, 1, 1')
        self.create_buttons('button18', '0', '7, 2, 1, 1')
        self.create_buttons('button19', '.', '7, 3, 1, 1')
        self.create_buttons('button20', '=', '7, 4, 1, 1')

        self.setFocus()

    def create_buttons(self, name, text, position):
        if text.isdigit():
            name = QPushButton(text)
            name.setStyleSheet("""
                QPushButton {
                    font-size: 30px;
                    background-color: #202124;
                    color: #0083b1;
                    border-radius: 10px;
                    border: 2px solid #0083b1;
                }
                QPushButton:hover {
                    background-color: #005f7f;
                    color: #fff;
                }
                QPushButton:pressed {
                    background-color: #003f5c;
                    color: #fff;
                }
            """)
            name.setFixedSize(100, 70)
        else:
            name = QPushButton(text)
            name.setStyleSheet("""
                QPushButton {
                    font-size: 30px;
                    background-color: #0083b1;
                    color: #fff;
                    border-radius: 10px;
                    border: 2px solid #0083b1;
                }
                QPushButton:hover {
                    background-color: #00aaff;
                    color: #202124;
                }
                QPushButton:pressed {
                    background-color: #005f7f;
                    color: #fff;
                }
            """)
            name.setFixedSize(100, 70)

        # Converte a string '1, 1, 1, 1' para uma tupla de inteiros
        pos_args = tuple(map(int, position.split(',')))
        self.addWidgetToVLayout(name, *pos_args)

        # Exemplo dentro de create_buttons
        if text == '+/-':
            def inverter_sinal():
                valor_str = self.display1.text()
                try:
                    valor_list = list(valor_str)
                    # Verifica se a lista está vazia
                    if not valor_list:
                        return             
                    elif valor_list[0] == '-':
                        valor_list.pop(0)
                    else:
                        valor_list.insert(0, '-')
                    self.display1.setText(''.join(valor_list))
                except ValueError:
                    self.display1.setText("")
            name.clicked.connect(inverter_sinal)

        if text == "1":
            name.clicked.connect(
                lambda: self.display1.setText(self.display1.text() + "1"))

        if text == "2":
            name.clicked.connect(
                lambda: self.display1.setText(self.display1.text() + "2"))

        if text == "3":
            name.clicked.connect(
                lambda: self.display1.setText(self.display1.text() + "3"))

        if text == "4":
            name.clicked.connect(
                lambda: self.display1.setText(self.display1.text() + "4"))

        if text == "5":
            name.clicked.connect(
                lambda: self.display1.setText(self.display1.text() + "5"))

        if text == "6":
            name.clicked.connect(
                lambda: self.display1.setText(self.display1.text() + "6"))

        if text == "7":
            name.clicked.connect(
                lambda: self.display1.setText(self.display1.text() + "7"))

        if text == "8":
            name.clicked.connect(
                lambda: self.display1.setText(self.display1.text() + "8"))

        if text == "9":
            name.clicked.connect(
                lambda: self.display1.setText(self.display1.text() + "9"))

        if text == "0":
            name.clicked.connect(
                lambda: self.display1.setText(self.display1.text() + "0"))

        if text == "C":
            name.clicked.connect(lambda: self.display1.setText(""))
            name.clicked.connect(lambda: self.display2.setText(""))

        if text == "◀":
            name.clicked.connect(
                lambda: self.display1.setText(self.display1.text()[:-1]))

        if text == "^":
            def add_caret():
                op_total = 0
                current = self.display1.text()
                if not current:
                    current = '0'
                if current and current[-1] in ["/", "*", "-", "+", "^"]:
                    current = current[:-1]
                for op in ["*", "-", "+", "^", "/"]:
                    if op in current:
                        op_total += 1
                    if op_total == 1:
                        self.calcular_resultado()
                        self.display1.setText(self.display1.text() + "^")
                        return
                self.display1.setText(current + "^")
            name.clicked.connect(add_caret)

        if text == "/":
            def add_div():
                op_total = 0
                current = self.display1.text()
                if not current:
                    current = '0'
                if current and current[-1] in ["/", "*", "-", "+", "^"]:
                    current = current[:-1]
                for op in ["*", "-", "+", "^", "/"]:
                    if op in current:
                        op_total += 1
                    if op_total == 1:
                        self.calcular_resultado()
                        self.display1.setText(self.display1.text() + "/")
                        return
                self.display1.setText(current + "/")
            name.clicked.connect(add_div)

        if text == "*":
            def add_mult():
                op_total = 0
                current = self.display1.text()
                if not current:
                    current = '0'
                if current and current[-1] in ["/", "*", "-", "+", "^"]:
                    current = current[:-1]
                for op in ["*", "-", "+", "^", "/"]:
                    if op in current:
                        op_total += 1
                    if op_total == 1:
                        self.calcular_resultado()
                        self.display1.setText(self.display1.text() + "*")
                        return
                self.display1.setText(current + "*")
            name.clicked.connect(add_mult)

        if text == "-":
            def add_sub():
                op_total = 0
                current = self.display1.text()
                if not current:
                    current = '0'
                if current and current[-1] in ["/", "*", "-", "+", "^"]:
                    current = current[:-1]
                for op in ["*", "-", "+", "^", "/"]:
                    if op in current:
                        op_total += 1
                    if op_total == 1:
                        self.calcular_resultado()
                        self.display1.setText(self.display1.text() + "-")
                        return
                self.display1.setText(current + "-")
            name.clicked.connect(add_sub)

        if text == "+":
            def add_plus():
                op_total = 0
                current = self.display1.text()
                if not current:
                    current = '0'
                if current and current[-1] in ["/", "*", "-", "+", "^"]:
                    current = current[:-1]
                for op in ["*", "-", "+", "^", "/"]:
                    if op in current:
                        op_total += 1
                    if op_total == 1:
                        self.calcular_resultado()
                        self.display1.setText(self.display1.text() + "+")
                        return
                self.display1.setText(current + "+")
            name.clicked.connect(add_plus)

        if text == ".":
            def add_dot():
                current = self.display1.text()
                if current and (current[-1] in ["/", "*", "-", "+", "^", "."]):
                    return  # Não adiciona ponto após operador ou ponto
                self.display1.setText(current + ".")
            name.clicked.connect(add_dot)

        if text == "=":
            name.clicked.connect(self.calcular_resultado)

    def calcular_resultado(self):
        text = self.display1.text()
        negative = False
        if text and text[0] == "-":
            text = text[1:]
            negative = True

        for op in ["/", "*", "-", "+", "^"]:
            if op in text:
                number1, number2 = text.split(op, 1)
                operator = op
                break
        else:
            # Nenhum operador encontrado
            try:
                result = -float(text) if negative else float(text)
            except Exception:
                result = "Erro na expressão 1"
            try:
                valor_formatado = (
                    f"{float(result):,.2f}"
                    .replace(',', 'v')
                    .replace('.', ',')
                    .replace('v', '.')
                )
            except Exception:
                valor_formatado = str(result)
            self.display2.setText(valor_formatado)
            self.display1.setText(valor_formatado)
            return

        try:
            number1 = -float(number1) if negative else float(number1)
            if number2 == '':
                number2 = 0.0
            else:
                number2 = float(number2)

            if operator == "/":
                result = number1 / number2
            elif operator == "*":
                result = number1 * number2
            elif operator == "-":
                result = number1 - number2
            elif operator == "+":
                result = number1 + number2
            elif operator == "^":
                result = number1 ** number2
        except ZeroDivisionError:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setWindowTitle("Erro")
            msg.setText("Erro: Divisão por zero")
            msg.exec()
            result = "Erro: Divisão por zero"
        except Exception:
            result = "Erro na expressão 2"
        try:
            valor_formatado = (
                f"{float(result):,.2f}".replace(',', 'v')
                .replace('.', ',').replace('v', '.'))
        except Exception:
            valor_formatado = str(result)
        self.display2.setText(valor_formatado)
        self.display1.setText(valor_formatado)

    def adjustFixedSize(self):
        # Ultima coisa a ser feita
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVLayout(
            self, widget: QWidget, row, col, rowspan=1, colspan=1):
        self.v_layout.addWidget(widget, row, col, rowspan, colspan)
        self.adjustFixedSize()

    def keyPressEvent(self, event):
        t = event.text()
        if t in "0123456789":
            self.adicionar_numero(t)
        elif t in "+-*/^":
            self.adicionar_operador(t)
        elif t == ".":
            self.adicionar_ponto()
        elif t.lower() == "c":
            self.display1.setText("")
            self.display2.setText("")
        elif event.key() == Qt.Key.Key_Backspace:
            self.display1.setText(self.display1.text()[:-1])
        elif event.key() in (
            Qt.Key.Key_Enter, Qt.Key.Key_Return, Qt.Key.Key_Equal):
            self.calcular_resultado()

    def adicionar_numero(self, numero):
        self.display1.setText(self.display1.text() + numero)

    def adicionar_operador(self, operador):
        op_total = 0
        current = self.display1.text()
        if current and current[-1] in ["/", "*", "-", "+", "^"]:
            current = current[:-1]
        for op in ["*", "-", "+", "^", "/"]:
            if op in current:
                op_total += 1

            # Se houver mais de um operador, calcula o resultado
            # Isso evita que o usuário adicione múltiplos operadores sem
            # calcular
            if op_total == 1:
                self.calcular_resultado()
                self.display1.setText(self.display1.text() + operador)
                return
                # Adiciona a barra ao final da expressão
        self.display1.setText(current + operador)

    def adicionar_ponto(self):
        current = self.display1.text()
        if current and (current[-1] in ["/", "*", "-", "+", "^", "."]):
            return  # Não adiciona ponto após operador ou ponto
        self.display1.setText(current + ".")
