from random import randint, randrange
import Sen_Gen as sg
from os import getcwd
import fileinput

class Link(object):
	def __init__(self, node1, node2, cd):
		self.node1 = node1
		self.node2 = node2
		self.cd = cd
	def chg_rdc(chg):
		return chg-self.cd
	def save(self):
		with open("%s/links_save.py" % (getcwd()), "a") as f:
			f.write("%s, %s, %d\n" % ("sg.words['%s']['%s']" % (self.node1.type, self.node1.word), "sg.words['%s']['%s']" % (self.node2.type, self.node2.word), self.cd))
		return "Saved"
	def return_node(self, lean=0):
		randome = random.randrange(0,1); randome += lean
		if randome > 0.5: return node2
		else: return node1

links = []

def add_link(thing, things, thingie=1):
	links.append(Link(thing, things, thingie))




words = {"noun":{}, "adjective":{}, "verb":{}, "adverb":{}, "conjunction":{}, "preposition":{}, "interjection":{}}
blue = sg.words
with open("%s/links_save.py" % (getcwd()), "r") as f: # save read in
	bob = f.read().splitlines()
for line in bob:
	eval("add_link(%s)" % (line))


class Word(object):
	def __init__(self, word, w_type, forms={}):
		self.word = word; self.type = w_type; self.local_links = []; self.word_out = []
		if w_type == "verb": self.forms = forms
	def add_word_ref(self, word):
		for e in links:
			if e.node1 == word:
				self.local_links.append(e)
		self.word_out.append(word)
#make a tree class







charlie = Word("snake", "noun")
bob = Word("snail", "noun")
bob.add_word_ref(charlie)






