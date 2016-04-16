from random import randrange
import Sen_Gen as sg
from os import getcwd
class Link(object):
	def __init__(self, node1, node2, charge_deduc=1):
		self.node1 = node1 #word1
		self.node2 = node2 #word2
		self.cd = charge_deduc #the amount of charge deducted from initial
	def charge_reduc(self, charge):
		return (charge - self.cd) #charge only goes 10 links
		#that way, if the starting word of the network is "ridiculous", it doesn't end up on the other end
		#of the network saying "mommy"
	def save(self):
		with open("%s/links_save.py" % (getcwd()), "a") as f:
			f.write("add_link(%s, %s, %d)\n" % ("sg.words['%s']['%s']" % (self.node1.type, self.node1.word), "sg.words['%s']['%s']" % (self.node2.type, self.node2.word), self.cd))

links = []

class Network(object):
	def __init__(self, nodes=[], links=[]):
		self.nodes = nodes #just words--not sure whether I have need the nodes
		self.links = links #essential for the follow function
		self.chg = 10
	def return_node(self):
		randome = random.randint(0,1)
		if randome == 1:
			return node2
		else:
			return node1
	def follow(self, word1):
		self.path, old_link = [], []
		for e in links:				#path is the sentence
			if e.node1.word==word1.word:
				old_link.append(e)
		#self.path.extend(old_link)
		i = 0
		current = []
		big = [] #actually lists within list, therefore "big"
		old_current = []
		restart = True
		for e in old_link:
			cont = True
			for k in big:
				if k==current:
					cont = False
			if cont:
				big.append(current)
			current = []
			o = e
			current.append(o)
			restart = True
			while restart:
				restart = False
				for li in links:
					if o.node2.word == li.node1.word and li not in current:
						restart = True
						o = li
						current.append(o)
						break
		big.append(current)
		holder, sizes = [], []
		for e in big:
			if e == []:
				big.remove(e)
			for i in e:
				if i == "":
					e.remove(i)
		for e in big:
			b = 0
			b = len(e)
			print "New Branch of length %x: " %(b)
			sizes.append(b)
			for i in e:
				if i.node1.word not in holder:
					holder.append(i.node1.word)
					print i.node1.word
				if i.node2.word not in holder:
					holder.append(i.node2.word)
					print i.node2.word
		sizes.sort()
		sizes.reverse()
		print sizes

def add_link(one, two, charge_deduc=1):
	links.append(Link(one, two, charge_deduc))
blue = sg.words
nodes = []
sentence_sequence = [[]]
#y = sg.Word("","")
for e in blue:
	for i in e:
		nodes.append(sg.Word(i, e))
with open("%s/links_save.py" % (getcwd()), "r") as f: # save read in
	bob = f.read().splitlines()
for line in bob:
	eval(line)

big_net = Network(nodes, links)
big_net.follow(sg.words["verb"]["to eat"])

#in this case, the path is the sentence
#by adding connections, we construct a network in big_net
#which allows the ai to come up with paths that actually make sense
#the sentence sequence allows us to store the sentences
#do not fix anything.
#this is officially my first machine learning network.
for e in big_net.path:
	print e.node1.word
sentence_sequence.append(big_net.path)
