'''
Funcao que retorna uma string com as informacoes do prestador, dados seu ID
'''
import xlrd

file_location = 'C:/python/BOT/BDMeuPrestador.xlsx'
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)

def getInfo(ID_in):
	ID = 0
	strReturn = ""
	for row in range(sheet.nrows):
		if (sheet.cell_value(row, ID) == ID_in): # Procurando o ID do prestador na coluna ID
			for col in range(1,sheet.ncols):
				if (sheet.cell_value(0, col) == 'Servico'):
					strReturn = "O " + str(sheet.cell_value(row, col)) + " mais proximo de voce se chama "
				elif (sheet.cell_value(0, col) == 'Nome'):
					strReturn = strReturn + str(sheet.cell_value(row, col)) + ", seu preco por hora e de R$ "
				elif (sheet.cell_value(0, col) == 'Preco por Hora'):
					strReturn = strReturn + str(int(sheet.cell_value(row, col))) + " e seu telefone e:\n"
				elif (sheet.cell_value(0, col) == 'Contato'):
					strReturn = strReturn + str(sheet.cell_value(row, col)) + "\nA nota do prestador e "
				elif (sheet.cell_value(0, col) == 'Avaliacao'):
					strReturn = strReturn + str(sheet.cell_value(row, col)) + " e foi avaliado(a) por "
				elif (sheet.cell_value(0, col) == 'Clientes'):
					strReturn = strReturn + str(int(sheet.cell_value(row, col))) + " pessoas.\n\nSe quiser outro servico e so falar. :D"
		if (ID_in == 17): # caso o ID seja 17 o bot retorna uma mensagem ao cliente informando que nao entendeu a mensagem ou nao encontrou o servico.
			strReturn = "Nao entendi ou nao temos prestadores dessse servico, pode repetir por favor? :/"
			return strReturn
	return strReturn