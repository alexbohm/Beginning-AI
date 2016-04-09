def correct(self):
		w_type = raw_input("Type: ")
		word = raw_input("Old Word: ")
		if w_type == "verb":
			print "Enter 'a' if word is correct"
			forms = {}
			forms['infinitive'] = raw_input("Infinitive: ")
			forms['past'] = raw_input("Past Tense: ")
			forms['present'] = raw_input("Present Tense: ")
			forms['future'] = raw_input("Future Tense: ")
			i = 0
			for word_ in forms:
				if word!=a:
					self.words["verb"][word][i] = word_
				i+=1
		else:
			print "You want to correct something that has no members.\n"
			print "Think again.\n"

#DO NOT DELETE
#THIS WILL BE VERY USEFUL LATER
