from random import randint
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
	def return_node(self):
		randome = randint(0,1)
		if randome == 1:
			return self.node2
		else:
			return self.node1
	def save(self):
		with open("%s/links_save.py" % (getcwd()), "a") as f:
			f.write("%s, %s, %d\n" % ("sg.words['%s']['%s']" % (self.node1.type, self.node1.word), "sg.words['%s']['%s']" % (self.node2.type, self.node2.word), self.cd))

links = []

class Network(object):
	def __init__(self, nodes=[], links=[]):
		self.nodes = nodes #just words--not sure whether I have need the nodes
		self.links = links #essential for the follow function
		self.chg = 10

	def follow(self, word1):
		self.path, old_link = [], []
		for e in links:				#path is the sentence
			if e.node1.word==word1.word:
				old_link.append(e)
		#self.path.extend(old_link)
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
			for i in e:
				if i.node1.word not in holder:
					holder.append(i.node1.word)
				if i.node2.word not in holder:
					holder.append(i.node2.word)
			print "New Branch of length %d: " % (len(holder))
			for i in e:
				if e.index(i)==0:
					print i.node1.word
				print i.node2.word

			sizes.append(len(holder))
			holder = []
		sizes.sort()
		sizes.reverse()
		print sizes

def add_link(one, two, charge_deduc=1):
	links.append(Link(one, two, charge_deduc))
nodes = []
sentence_sequence = [[]]

with open("%s/links_save.py" % (getcwd()), "r") as f: # save read in
	bob = f.read().splitlines()
for line in bob:
	eval("add_link(%s)" % (line))

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