from random import randrange
class Sen_Gen(object):
	def __init__(self):
		self.all_words = []
		self.types = {"noun":[], "adjective":[], "verb":[], "adverb":[], "conjunction":[], "preposition":[], "interjection":[]}
		for type_w in self.types:
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
		return "%s %s the %s %s" % (self.types["noun"][self.random[1]], self.types["verb"][self.random[2]], self.types["adjective"][self.random[3]], self.types["noun"][self.random[4]])