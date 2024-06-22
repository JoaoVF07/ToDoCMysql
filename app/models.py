import pymysql

conexao = pymysql.connect(
        host='localhost',
        user='root',
        password='Tartaruga20',
        database='todo',
    )
cursor = conexao.cursor()