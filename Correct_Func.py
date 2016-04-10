def correct(self):
	w_type = raw_input("Type: ")
	word = raw_input("Old Word: ")
	if w_type == "verb":
		print "Enter 'a' if word is correct"
		oforms = {}
		oforms['infinitive'] = raw_input("Infinitive: ")
		oforms['past'] = raw_input("Past Tense: ")
		oforms['present'] = raw_input("Present Tense: ")
		oforms['future'] = raw_input("Future Tense: ")
		referendum, i = ['infinitive','past','present','future'], 0
		for word_ in oforms:
			if word_!='a':
				with open('words.txt', '') as inF:
					for line in inF:
						if word_ in line:
							line = line.replace(self.words["verb"][word].forms[oforms[referendum[i]]], word_)
				self.words["verb"][word].forms[oforms[referendum[i]]] = word_
			i+=1
	else:
		print "You want to correct something that has no members.\n"
		print "Think again.\n"

#DO NOT DELETE
