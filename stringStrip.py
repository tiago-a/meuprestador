def sstrip(strin):
	convoList = strin.split(' ')
	for idx, s in enumerate(convoList):
		if s[-1] == ',':
			convoList[idx] = s[:-1]
		elif s[-1] == '.':
			convoList[idx] = s[:-1]
		elif s[-1] == '?':
			convoList[idx] = s[:-1]
		elif s[-1] == '!':
			convoList[idx] = s[:-1]
	return convoList