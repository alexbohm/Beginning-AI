from random import randrange
all_tags = []
all_verbs = []
all_words = [] #not verbs
all_types = {"noun":[], "adjective":[], "adverb":[], "conjunction":[], "preposition":[], "interjection":[]}

class Word(object):
	def __init__(self, word,w_type,tags = {},forms = {}):
		self.word = word
		self.type = w_type
		self.tags = tags
		self.forms = forms
	def save(self):
		return "%s:%s:%s:%s" % (self.word, self.type, str(self.tags), str(self.forms))

class Verb(object):
	def __init__(self, infinitive, past, present, future, tag):
		self.infinitive = infinitive
		self.past = past
		self.present = present
		self.future = future
		self.tag = tag

def add_tag(tag):
	all_tags.append(tag)

def make_word(word, type_):
	if type_!="verb":
		if word not in all_words:
			all_words.append(Word(word, type_))
	elif type_ == "verb":
		infinitive = raw_input("Infinitive: ")
		past = raw_input("Past Tense: ")
		present = raw_input("Present Tense: ")
		future = raw_input("Future Tense: ")
		tag = raw_input("Tag: ")
		if tag not in all_tags:
			all_tags.append(tag)
		if verb not in all_verbs:
			all_verbs.append(Verb(infinitive, past, present, future, tag))
	else:
		print "Sorry, you mispelled the type."

class Sen_Gen(object):
	def __init__(self, structure=[]):
		self.structure = structure
		for e in all_types:
			with open("%s.txt" % (e), "r") as f:
				all_types[e] = f.read().splitlines()
		with open("%s.txt" % ("verb"), "a") as f:
			lines = f.read().splitlines()
			for e in lines:
				verb_parts = e.split(":")
				all_verbs.append(Verb(verb_parts[0], verb_parts[1], verb_parts[2], verb_parts[3], verb_parts[4], verb_parts[5]))
	def add_words(self, amount):
		i = 0
		while True:
			word = raw_input("Word: ") #this program takes it for granted that the user does not make typos or repeats
			type_ = raw_input("Type: ")
			i+=1
			if type_ == "verb":
				blue = make_word(word, type_, tag)
			else:
				blue = make_word(word, type_)
			if i > amount-1:
				break
			if type_!="verb":
				for type_w in all_types:
						if type_ == type_w:
							all_types[type_w].append()
							with open("%s.txt" % (type_w), "a") as f:
								f.write("%s\n" %(blue))
			else:
				with open("%s.txt" % ("verb"), "a") as f:
					f.write("%s:%s:%s:%s:%s\n" % (blue.infinitive, blue.past, blue.present, blue.future, blue.tag))














