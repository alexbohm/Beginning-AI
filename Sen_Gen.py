from random import randrange
from os import getcwd
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

words = {"noun":{}, "adjective":{}, "verb":{}, "adverb":{}, "conjunction":{}, "preposition":{}, "interjection":{}}
with open("%s/words.txt" % (getcwd()), "r") as f:
	temp = f.read().splitlines()
for word in temp:
	temp2 = word.split("|")
	if temp2[1]=="verb":
		words["verb"][temp2[0]] = Word(temp2[0], "verb", eval(temp2[2]))
	else:
		words[temp2[1]][temp2[0]] = Word(temp2[0], temp2[1])
class Sen_Gen(object):
	def __init__(self, structure=[]):
		self.structure = structure
	def random_word(self, w_type): #find random word with inputed type
		rand_num = randrange(0, len(words[w_type]))
		i = 0
		for word in words[w_type]:
			if i==rand_num:
				return word
			i += 1
	def get_verb(self, infinitive, tense="present"):
			return words["verb"][infinitive].forms[tense]
	def make_sen(self, amount=3, structure=[]):
		if not len(structure) == 0:
			self.structure = structure
		senl = []
		for i in range(amount):
			stc = ""
			for e in self.structure:
				if e == "verb":
					stc+= "%s " % (self.get_verb(self.random_word(e)))
				elif e in words:
					stc+= "%s " % (self.random_word(e))
				else:
					stc+= "%s " % (e)
			stc = stc[0:-1]
			senl.append(stc)
		return senl