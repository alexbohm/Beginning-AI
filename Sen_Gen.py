from random import randrange
class Word(object):
	def __init__(self, word,w_type,forms = {}):
		self.word = word
		self.type = w_type
		if w_type == "verb":
			self.forms = forms
	def save(self):
		if self.type == "verb":
			return "%s|%s|%s\n" % (self.word, self.type, str(self.forms))
		else:
			return "%s|%s\n" % (self.word, self.type)

class Sen_Gen(object):
	def __init__(self):
		self.words = {"noun":{}, "adjective":{}, "verb":{}, "adverb":{}, "conjunction":{}, "preposition":{}, "interjection":{}}
		with open("words.txt", "r") as f:
			temp = f.read().splitlines()
		for word in temp:
			temp2 = word.split("|")
			if temp2[1]=="verb":
				self.words[temp2[1]][temp2[0]] = Word(temp2[0], temp2[1], eval(temp2[2]))
			else:
				self.words[temp2[1]][temp2[0]] = Word(temp2[0], temp2[1])
	def add_word(self):
		w_type = str(raw_input("Word Type: "))
		while w_type not in self.words: #check if word type is valid
			if w_type not in self.words:
				print "invalid type"
			w_type = str(raw_input("Word Type: "))
		forms = {}
		if w_type == "verb":
			forms = {}
			forms['infinitive'] = raw_input("Infinitive: ")
			while forms['infinitive'] in self.words[w_type]: #check if word is valid
				if forms['infinitive'] in self.words[w_type]:
					print "Verb Aready in List"
				forms['infinitive'] = raw_input("Infinitive: ")
			forms['past'] = raw_input("Past Tense: ")
			forms['present'] = raw_input("Present Tense: ")
			forms['future'] = raw_input("Future Tense: ")
			word = forms['infinitive']
		else:
			word = str(raw_input("Word: "))
			while word in self.words[w_type]: #check if word is valid
				if word in self.words[w_type]:
					print "Aready in List"
				word = str(raw_input("Word: "))
		self.words[w_type][word] = Word(word, w_type, forms)
		with open("words.txt", "a") as f:
			f.write(self.words[w_type][word].save())
	def random_word(self, w_type): #find random word with inputed type
		rand_num = randrange(0, len(self.words[w_type]))
		i = 0
		for word in self.words[w_type]:
			if i==rand_num:
				return word
			i += 1