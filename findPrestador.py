'''
Funco que retorna o ID do prestador que esta mais perto do cliente
dado uma string com o servico de busca e a localizacao do cliente
'''

import xlrd
import math

file_location = 'C:/python/BOT/BDMeuPrestador.xlsx'
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)

def findPrest(xsrv, pos):
	dict = {}
	ID = 0
	Servico = 1
	Localizacao = 3
	for row in range(sheet.nrows):
		if (sheet.cell_value(row, Servico).upper() == xsrv.upper()): # testa se o servico buscado se encontra na coluna de Servicos, mesmo que escrito em maiusculo ou minisculo
			dist = int(math.fabs(pos - int(sheet.cell_value(row, Localizacao)))) # calcula a distancia entre o prestador e o cliente
			dict[int(sheet.cell_value(row, ID))] = dist # adiciona os resultados a um dicionario
	if (not dict): # Se o dicionario estiver vazio significa que o servico nao se encontra na base de dados, logo retorna ID 17, para que o bot saiba que nao encontou ninguem
			ID_return = 17
			return ID_return
	ID_return = int(min(dict, key = dict.get)) # ID_return recebe o ID do prestador mais perto do cliente
	return ID_return