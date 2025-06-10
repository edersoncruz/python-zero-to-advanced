# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela

from datetime import datetime
from dateutil.relativedelta import relativedelta


class Emprestimo():
    def __init__(self, nome, data_inicio, tempo, valor):
        self.nome = nome
        self.data_inicio = data_inicio
        self.tempo = tempo
        self.valor = valor

    def __repr__(self) -> str:
        return f'Nome: {self.nome} | Data Inicio: {self.data_inicio} | '\
                f'Tempo: {self.tempo} | Valor: {self.valor}'

    def calcular_data_fim(self):
        self.data_inicio_frmt = datetime.strptime(self.data_inicio, '%d-%m-%Y')
        self.data_fim = self.data_inicio_frmt + relativedelta(years=self.tempo)
        return self.data_fim

    def printar_parcelas(self):
        total_meses = self.tempo * 12
        valor_parcela = self.valor / total_meses
        self.data_inicio_frmt = self.data_inicio_frmt + relativedelta(months=1)
        for i in range(total_meses):
            vencimento = self.data_inicio_frmt + relativedelta(months=i)
            print(f'Parcela {i+1} {vencimento.strftime("%d/%m/%Y")}'
                  f' R$ {valor_parcela:.2f}')


emprestimo_maria = Emprestimo('Maria', '20-12-2020', 5, 5000)

emprestimo_maria.calcular_data_fim()

emprestimo_maria.printar_parcelas()
