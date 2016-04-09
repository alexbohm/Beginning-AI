w_type = "verb" #type
with open("%s.txt" % (w_type), "r") as f:
	words = f.read().splitlines()
with open("new_verbs.txt", "a") as g:
	for word in words:
		if word[-1]=="e":
			past = word[0:-1]
		elif word[-1] =="y":
			past = word[0:-1] + "i"
		elif word[-1] == "p":
			past = word + "p"
		else:
			past = word
		g.write("to %s|%s|{'infinitive':'to %s','past':'%sed','present':'%ss', 'future':'will %s'}\n" % (word, w_type, word, past, word, word))
		print word


"""	def correct(self):
		
		w_type = raw_input("Type: ")
		word = raw_input("Old Word: ")
		if w_type == "verb":
			print "Enter 'a' if word is correct"
			forms = {}
			forms['infinitive'] = raw_input("Infinitive: ")
			forms['past'] = raw_input("Past Tense: ")
			forms['present'] = raw_input("Present Tense: ")
			forms['future'] = raw_input("Future Tense: ")
			for word in forms:
				if word == "a":
					pass
				else:
					self.words["verb"][word]




		new = raw_input("Correction: ")"""