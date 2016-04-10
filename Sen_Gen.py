from random import randrange
import os
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
	def __init__(self, structure=[]):
		self.structure = structure
		self.words = {"noun":{}, "adjective":{}, "verb":{}, "adverb":{}, "conjunction":{}, "preposition":{}, "interjection":{}}
		self.path = os.getcwd()
		with open("%s/words.txt" % (self.path), "r") as f:
			temp = f.read().splitlines()
		for word in temp:
			temp2 = word.split("|")
			if temp2[1]=="verb":
				self.words["verb"][temp2[0]] = Word(temp2[0], "verb", eval(temp2[2]))
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
		with open("%s/words.txt" % (self.path), "a") as f:
			f.write(self.words[w_type][word].save())
	def random_word(self, w_type): #find random word with inputed type
		rand_num = randrange(0, len(self.words[w_type]))
		i = 0
		for word in self.words[w_type]:
			if i==rand_num:
				return word
			i += 1
	def get_verb(self, infinitive, tense="present"):
			return self.words["verb"][infinitive].forms[tense]
	def make_sen(self, amount=3, structure=[]):
		if not len(structure) ==0:
			self.structure = structure
		senl = []
		for i in range(amount):
			stc = ""
			for e in self.structure:
				if e == "verb":
					stc+= "%s " % (self.get_verb(self.random_word(e)))
				elif e in self.words:
					stc+= "%s " % (self.random_word(e))
				else:
					stc+= "%s " % (e)
			stc = stc[0:-1]
			senl.append(stc)
		return senl


stru = ["adjective", "noun", "verb", "noun"] #, "adverb", "verb", "noun"
simplesen = Sen_Gen(stru)
print simplesen.make_sen(1)
print simplesen.make_sen(1,["adjective", "noun", "verb", "adjective", "noun", "verb"])