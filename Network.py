from random import randint, randrange
import Sen_Gen as sg
from os import getcwd
import fileinput

class Tuple_Dict(object):
	def __init__(self):
		self.keys = []
		self.list = ()
	def add_to(self, key, value):
		self.keys.append(key)
		self.keys.append(value)
	def at_k(self, key):
		a = self.keys.index(key)
		return self.keys[a]
	def at_v(self, value):
		for e in self.list:
			for i in e:
				if i==value:
					good_one = e
		place = self.list.index(good_one)
		return key[place]

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

sub_net_uni = {}
sub_net_multi = {}

class Sub_Net(object):
	def __init__(self, name, w_type="misc", nodes=[]):
		self.name = name
		self.w_type = w_type
		self.nodes = nodes
		sub_net_uni[name] = self
	def add_to_nodes(node):
		self.nodes.append(node)

class Mega_Net(object):
	def __init__(self, name, w_type="misc", nodes1=Sub_Net(""), nodes2=Sub_Net("")):
		self.name = name
		self.w_type = w_type
		self.all_nodes_lists = Tuple_Dict()
		if nodes1:
			self.all_nodes_lists.add_to(nodes1.name, nodes1)
		if nodes2:
			self.all_nodes_lists.add_to(nodes2.name, nodes2)
	def add_nodes_list(self, nl=Sub_Net("")):
		self.all_nodes_lists.add_to(nl.name, name)

def add_mega_net_to(selfie=Mega_Net(""), mn=Mega_Net("")):
	selfie.all_nodes_lists(mn.name, mn)

#def find_sub_net(list_of_links=[]):
#def follow(list_of_links=[]):




snake = Word("snake", "noun")
snail = Word("snail", "noun")
animal = Word("animal", "noun")
animals = Sub_Net("animals", "noun", [snake, snail])
food = Word("food", "noun")
bread = Word("bread", "noun")
cake = Word("bread", "noun")
t_eat = Word("to eat", "verb")
foods = Sub_Net("foods", "misc", [bread, cake, eat])
animal_foods = Mega_Net("af", "misc", animals)
animal_foods.add_nodes_list(foods)






