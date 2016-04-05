from random import randrange
all_words = [] #this list does change over time
all_types = {"noun":[], "adjective":[], "verb":[], "adverb":[], "conjunction":[], "preposition":[], "interjection":[]} #this list is constant
all_tags = [] #this list does change over time
class Word(object):
	def __init__(self, word, typew, tag=""):
		self.word = word
		self.type_w = typew
		self.tag = tag #for later



class Sen_Gen(object):
	def __init__(self):
		global all_words
		global all_types
		global all_tags
		for type_w in all_types:
			with open("%s.txt" % (type_w), "r") as f:
				all_types[type_w] = f.read().splitlines()
			all_words.append(Word(all_types[type_w], type_w))
	def add_words(self, number):
		for a in range(number):
			word = ''
			word = str(raw_input("Word: "))
			while word in all_words:
				if word in all_words:
					print "already in list"
				word = str(raw_input("Word: "))
			word_type = ""
			word_type = str(raw_input("Word Type: "))
			while word_type not in all_types:
				if word_type not in all_types:
					print "invalid type"
				word_type = str(raw_input("Word Type: "))
			tag = str(raw_input("Tag: "))
			if tag not in all_tags:
				all_tags.append(tag)
			for type_w in all_types:
				if word_type == type_w:
					all_types[type_w].append(word)
					with open("%s.txt" % (type_w), "a") as f:
						f.write("%s:%s\n" %(word, tag))
			all_words.append(Word(word, type_w, tag))
	def gen_sen(self, lower, upper):
		self.random = {}
		for a in range(5):
			self.random[a] = randrange(lower, upper)
		return "%s %s the %s %s" % (all_types["noun"][self.random[1]], all_types["verb"][self.random[2]], all_types["adjective"][self.random[3]], all_types["noun"][self.random[4]])

sg = Sen_Gen()
liste = sg.gen_sen(2,5)
print liste