from random import randrange
class Word(object):
	def __init__(self, word,w_type,forms = {}):
		self.word = word
		self.type = w_type
		self.forms = forms
	def save(self):
		return "%s:%s:%s\n" % (self.word, self.type, str(self.forms))

class Sen_Gen(object):
	def __init__(self):
		self.words = {"noun":{}, "adjective":{}, "verb":{}, "adverb":{}, "conjunction":{}, "preposition":{}, "interjection":{}}
		with open("words.txt", "r") as f:
			temp = f.read().splitlines()
		for word in temp:
			temp2 = word.split(":")
			self.words[temp2[1]][temp2[0]] = Word(temp2[0], temp2[1], eval(temp2[2]))
	def add_word(self):
		w_type = str(raw_input("Word Type: "))
		while w_type not in self.words: #check if word type is valid
			if w_type not in self.words:
				print "invalid type"
			w_type = str(raw_input("Word Type: "))
		if w_type == "verb":
			forms = {}
			forms['infinitive'] = raw_input("Infinitive: ")
			forms['past'] = raw_input("Past Tense: ")
			forms['present'] = raw_input("Present Tense: ")
			forms['future'] = raw_input("Future Tense: ")
		else:
			word = str(raw_input("Word: "))
			while word in self.words[w_type]: #check if word is valid
				if word in self.words[w_type]:
					print "Aready in List"
				word = str(raw_input("Word: "))
			self.words[w_type][word] = Word(word, w_type)
		with open("words.txt", "a") as f:
			f.write(self.words[w_type][word].save())
		




































'''class Sen_Gen(object):
	def __init__(self):
		self.all_words = []
		self.types = {"noun":[], "adjective":[], "verb":[], "adverb":[], "conjunction":[], "preposition":[], "interjection":[]}
		for type_w in self.types: #read in all words from files
			with open("%s.txt" % (type_w), "r") as f:
				self.types[type_w] = f.read().splitlines()
			self.all_words += self.types[type_w]
	def add_words(self, number):
		for a in range(number):
			word = ""
			word = str(raw_input("Word: "))
			while word in self.all_words: #check if word is already in list
				if word in self.all_words:
					print "already in list"
				word = str(raw_input("Word: "))
			word_type = ""
			word_type = str(raw_input("Word Type: "))
			while word_type not in self.types: #check if word type is valid
				if word_type not in self.types:
					print "invalid type"
				word_type = str(raw_input("Word Type: "))
			self.types[word_type].append(word) #add word to it's list
			self.all_words.append(word) #add word to full list
			with open("%s.txt" % (word_type), "a") as f:
				f.write("%s\n" % (word)) #add word to appropriate file
	def gen_sen(self, lower, upper):
		self.random = {}
		for a in range(5):
			self.random[a] = randrange(lower, upper)
		return "%s %s the %s %s" % (self.types["noun"][self.random[1]], self.types["verb"][self.random[2]], self.types["adjective"][self.random[3]], self.types["noun"][self.random[4]])'''