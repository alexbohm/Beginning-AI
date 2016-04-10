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
			i = 0
			referendum = {0:'infinitive',1:'past',2:'present',3:'future'}
			for word_ in oforms:
				if word_!='a':
					#1. Find word in words.txt
					#2. Replace wrong form with correct form in words.txt
					self.words["verb"][word].forms[oforms[referendum[i]]] = word_
				i+=1
		else:
			print "You want to correct something that has no members.\n"
			print "Think again.\n"

#DO NOT DELETE
#THIS WILL BE VERY USEFUL LATER
