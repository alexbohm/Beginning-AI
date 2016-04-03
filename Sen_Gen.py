from random import randrange

#types = ["noun", "verb"]
class Sen_Gen(object):
	def __init__(self):
		self.noun, self.verb, self.ext, self.adjective = [], [], [], []
		with open('nouns.txt') as f:
		    self.noun = f.read().splitlines()
		with open('verbs.txt') as f:
		    self.verb = f.read().splitlines()
		with open('adjectives.txt') as f:
		    self.adjective = f.read().splitlines()
		self.all_words = {}
	def add_words(self, number):
		for a in range(7):
			self.word = str(raw_input("Word: "))
			self.type_w = raw_input("Type: ")
			if self.word not in self.all_words:
				self.all_words[self.word] = self.type_w
				if self.type_w == "noun":
					noun.append(self.word)
					self.nouns = open("nouns.txt", "a")
					self.nouns.write(self.word)
					self.nouns.close()
				elif self.type_w == "verb":
					self.verb.append(self.word)
					self.verbs = open("verbs.txt", "a")
					self.verbs.write(self.word)
					self.verbs.close()
				elif self.type_w == "adjective":
					self.adjective.append(self.word)
					self.adjectives = open("adjectives.txt", "a")
					self.adjectives.write(self.word)
					self.adjectives.close()
				else:
					self.ext.append(self.word)
			else:
				print "In List"
	def gen_sen(self, lower, upper):
		self.random = {}
		self.random[1] = randrange(lower, upper)
		self.random[2] = randrange(lower, upper)
		self.random[3] = randrange(lower, upper)
		return "%s %s the %s" % (self.noun[self.random[1]], self.verb[self.random[2]], self.noun[self.random[3]])
sen = Sen_Gen()
#sen.add_words(10) add ten? words
print sen.gen_sen(5, 500)