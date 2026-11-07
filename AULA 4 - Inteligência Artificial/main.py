

import sqlite3

arquivo_DB = sqlite3.connect('nome_banco.db')
cursor = arquivo_DB.cursor()

cursor.execute('''

        CREATE TABLE IF NOT EXISTS dados(

              vendas REAL,
              vendedor TEXT


         )
''')

arquivo_DB.comit()