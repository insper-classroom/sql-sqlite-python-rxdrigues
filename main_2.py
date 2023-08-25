from db.db_utils import *
import sqlite3


# Exercício de Python - Sqlite

tabela = SQL('db/database_alunos.db', 'Alunos')
tabela.cria_tabela([('Nome', 'TEXT NOT NULL'), ('Curso', 'TEXT NOT NULL'), ('Ano_De_Ingresso', 'INTEGER'), ])
estudantes=[
('Nome', 'Ana Silva'), ('Curso', 'Computação'), ('Ano_De_Ingresso', 2019),
('Nome', 'Pedro Mendes'), ('Curso', 'Física'), ('Ano_De_Ingresso', 2021),
('Nome', 'Carla Souza'), ('Curso', 'Computação'), ('Ano_De_Ingresso', 2020),
('Nome', 'João Alves'), ('Curso', 'Matemática'), ('Ano_De_Ingresso', 2018),
('Nome', 'Maria Oliveira'), ('Curso', 'Química'), ('Ano_De_Ingresso', 2022)
]
tabela.insere_dados(estudantes)
tabela.consulta_dados('*', f'Ano_de_Ingresso IN (2019, 2020)')
tabela.atualiza_dados('Ano_de_Ingresso', 2023, 'Curso = "Química"')
tabela.deleta_dados('ID = 4')
tabela.consulta_dados('*')
tabela.atualiza_dados('Ano_de_Ingresso','2018', '"Computação"')
tabela.consulta_dados('*','')