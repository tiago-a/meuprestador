srvs = ["motorista", "pintor", "diarista", "encanador", "pedreiro"]

def jCheck (strinList):
	nIntendeu = "vazio"
	for strin in strinList:
		for x in srvs:
			if strin.upper() == x.upper():
				return strin
	return nIntendeu