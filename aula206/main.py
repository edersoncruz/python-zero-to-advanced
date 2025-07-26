# PyMySQL - um cliente MySQL feito em Python Puro
# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import os

import dotenv
import pymysql

TABLE_NAME = 'customers'

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
    charset='utf8mb4'
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(  # type: ignore
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id)'
            ') '
        )
        # CUIDADO: ISSO LIMPA A TABELA
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')  # type: ignore
    connection.commit()

    # Começo a manipular dados a partir daqui
    # Inserindo um registro usando um placeholder e um iterável
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%s, %s) '
        )
        data = ('Sora', 18)
        result = cursor.execute(sql, data)  # type: ignore
        # print(sql, data)
        # print(result)
    connection.commit()

    # Inserindo outro registro usando um placeholder e um dicionário
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%(nome)s, %(idade)s) '
        )
        data2 = {
            "nome": "Ovyva",
            "idade": 27,
        }
        result = cursor.execute(sql, data2)  # type: ignore

    connection.commit()
    
    # Inserindo vários registros de uma vez usando uma tupla e dicionários
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%(nome)s, %(idade)s) '
        )
        data3 = (
            {"nome": "GPT","idade": 33,},
            {"nome": "Gemini","idade": 22,},
            {"nome": "Cortana","idade": 55,},
        )
        result = cursor.executemany(sql, data3)  # type: ignore

    connection.commit()

    # Inserindo vários registros usando um placeholder e uma tupla com tuplas
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) '
            'VALUES '
            '(%s, %s) '
        )
        data4 = (
            ("Siri", 33,),
            ("Alexa", 22,),
        )
        result = cursor.executemany(sql, data4)  # type: ignore

    connection.commit()

    # Lendo os valores com SELECT
    with connection.cursor() as cursor:
        sql = (
            f'SELECT * FROM {TABLE_NAME} '
        )
        cursor.execute(sql)  # type: ignore
        data5 = cursor.fetchall()  # type: ignore

        for row in data5:
            print(f'ID: {row[0]}, Nome: {row[1]}, Idade: {row[2]}')

