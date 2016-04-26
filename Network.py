import random
import Sen_Gen as sg
from os import getcwd

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
		print "OLD save for links, use new system"
	def return_node(self, lean=0):
		randome = random.randrange(0,1); randome += lean
		if randome > 0.5: return node2
		else: return node1

links = []

def add_link(thing, things, thingie=1):
	links.append(Link(thing, things, thingie))


"""words = {"noun":{}, "adjective":{}, "verb":{}, "adverb":{}, "conjunction":{}, "preposition":{}, "interjection":{}}
blue = sg.words"""
#Link read in
for w_type in sg.words:
	for ind in sg.words[w_type]:
		for link in sg.words[w_type][ind].links:
			add_link(sg.words[w_type][ind], sg.words[sg.words[w_type][ind].links[link][0]][link], sg.words[w_type][ind].links[link][1])
			#print link, sg.words[w_type][ind].links[link][0]


class Word(object):
	def __init__(self, word, w_type, forms={}):
		self.word = word; self.type = w_type; self.local_links = []; self.word_out = []
		if w_type == "verb": self.forms = forms
	def add_word_ref(self, word, recip=False):
		for e in links:
			if e.node1 == word:
				self.local_links.append(e)
		if recip:
			word.add_word_ref(self, False)
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
		self.all_nodes_lists.add_to(nl.name, nl)

def add_mega_net_to(selfie=Mega_Net(""), mn=Mega_Net("")):
	selfie.all_nodes_lists(mn.name, mn)

def choose(b=[Word("","")], lean=0):
	length = len(b)
	randome = random.randrange(0,len(b)) #if randrange were inclusive, we would use len(b)-1
	randome+=lean
	if randome>len(b)-1:
		return b[-1]
	return b[int(randome)]

def full_follow(sw=Word("",""), limit=4):
	out = sw.word_out
	word = choose(out)
	i=0
	path=[]
	path.append(sw)
	while True:
		if word not in path:
			path.append(word)
		word = choose(word.word_out)
		i+=1
		if i>limit:
			break
	return path
	

#instead of putting dictionaries within dictionaries, just put lists in dictionaries
#no need for the a member of a class to reference the class. That is redundant.



snake = Word("snake", "noun")
snail = Word("snail", "noun")
animal = Word("animal", "noun")
animals = Sub_Net("animals", "noun", [snake, snail])
food = Word("food", "noun")
bread = Word("bread", "noun")
cake = Word("bread", "noun")
t_eat = Word("to eat", "verb")
foods = Sub_Net("foods", "misc", [bread, cake, t_eat])
animal_foods = Mega_Net("af", "misc", animals)
animal_foods.add_nodes_list(foods)
snake.add_word_ref(snail, True)
snake.add_word_ref(animal)
snake.add_word_ref(t_eat)
cake.add_word_ref(bread, True)
animal.add_word_ref(food)
t_eat.add_word_ref(food)
food.add_word_ref(cake)
snail.add_word_ref(animal)
for e in bread.word_out:
	print e.word
b = full_follow(snake)
print "----"
for e in b:
	print e.word






