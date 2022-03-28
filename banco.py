import mysql.connector as mc
import json

lista = []
lista2 = []
dic = {}


conexao = mc.connect(
    host="put your mysql database ip or localhost",
    database="write your database name",
    user="the bank username",
    password="password",
    autocommit="True")
    # if the mysql database is a localhost remove the variable's autocommit conexaos

if conexao.is_connected():
        cursor = conexao.cursor()
        cursor.execute("select * from empresas")
        linhas = cursor.fetchall()

        for row in linhas:
            lista.append(row)

        total = len(lista) 
        for i in range(total):
            dic[f'{lista[i][1]}'] = [{'id': lista[i][0], 'razao': f'{lista[i][1]}', 'cnpj_': f'{lista[i][2]}', 'insc_est': f'{lista[i][3]}', 'muni': f'{lista[i][4]}', 'rg_': f'{lista[i][5]}',  'prod': f'{lista[i][6]}',  'stts': f'{lista[i][7]}'}]

            


