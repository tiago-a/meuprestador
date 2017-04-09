from findPrestador import findPrest
from getInfoPrest import getInfo
from stringStrip import sstrip
from jobChecker import jCheck
from random import randint



def convo(mensagem):
	wordList = sstrip(mensagem) # Separa a mensagem enviada pelo cliente em uma lista de palavras e guarda em wordList
	serv = jCheck(wordList) # Envia a lista wordList para que o servico que o cliente busca seja identificado e guarda o servico desejado na string serv
	ID = findPrest(serv, randint(0, 200)) # Encontra o prestador do servico baseado na necessidade do cliente e gera uma posicao aleatoria para o cliente e retorna o ID
	BOTmsg = getInfo(ID) # Com o ID, essa funcao busca as informacoes do prestador e retorna uma string com todas informacoes do mesmo
	return BOTmsg