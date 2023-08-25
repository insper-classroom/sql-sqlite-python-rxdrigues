import sqlite3

class SQL:
    def __init__(self, database, nome_tabela):
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()
        self.nome_tabela = nome_tabela
        self.database = database

    def cria_tabela(self, colunas):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        
        queue = f'CREATE TABLE IF NOT EXISTS {self.nome_tabela} (ID INTEGER PRIMARY KEY AUTOINCREMENT, '

        for coluna in colunas:
            if coluna != colunas[-1]:
                queue += f'{coluna[0]} {coluna[1]}, '
            else:
                queue += f'{coluna[0]} {coluna[1]});'

        cursor.execute(queue)

        conn.commit()
        conn.close()

    def insere_dados(self, informacoes):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        
        queue_dados = ''

        for dados in informacoes:
            if dados != dados[-1]:
                queue_dados += f'{dados[0]}, '
            else:
                queue_dados += f'{dados[0]}) VALUES'
        for dados in informacoes:
            if dados != dados[-1]:
                queue_dados += f'{dados[1]}, '
            else:
                queue_dados += f'{dados[1]});'

        cursor.executemany(f'INSERT INTO {self.nome_tabela} (', queue_dados)
        conn.commit()
        conn.close()

    def consulta_dados(self, condicao):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        
        queue_consulta = f'SELECT {condicao} FROM {self.nome_tabela}'

        cursor.execute(queue_consulta)
        conn.commit()
        print(cursor.fetchall())
        conn.close()

    def atualiza_dados(self, coluna, informacoes_antigas, condicao_where):
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        
        queue_atualiza = f"UPDATE {self.nome_tabela} SET {coluna} = {str(informacoes_antigas)} WHERE {condicao_where}"
        
        cursor.execute(queue_atualiza)
        conn.commit()
        conn.close()

    def deleta_datos(self, condicao):
        conn = sqlite3.connect(self.nome_database)
        cursor = conn.cursor()

        queue_deleta = f"DELETE FROM {self.nome_tabela} WHERE {condicao}"
        
        cursor.execute(queue_deleta)
        conn.commit()
        conn.close()
        