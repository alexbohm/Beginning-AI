from random import randrange
import Sen_Gen as sg
class Link (object):
	def __init__(self, node1, node2, charge_deduc=1):
		self.node1 = node1 #word1
		self.node2 = node2 #word2
		self.cd = charge_deduc #the amount of charge deducted from initial
	def charge_reduc(self, charge):
		return (charge - self.cd) #charge only goes 10 links
		#that way, if the starting word of the network is "ridiculous", it doesn't end up on the other end
		#of the network saying "mommy"

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
		restart = True
		for e in old_link:
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
		holder = []
		for e in big:
			if e == []:
				big.remove(e)
		for e in big:
			print "New Branch: "
			for i in e:
				if i.node1.word not in holder:
					holder.append(i.node1.word)
					print i.node1.word
				if i.node2.word not in holder:
					holder.append(i.node2.word)
					print i.node2.word
			holder=[]


				


def add_link(one, two, charge_deduc=1):
	links.append(Link(one, two, charge_deduc))

blue = sg.words
nodes = []
sentence_sequence = [[]]
y = sg.Word("","")
for e in blue:
	for i in e:
		nodes.append(sg.Word(i, e))
import links_save as l_s # runs save file

"""add_link(sg.words["noun"]["pie"], sg.words["verb"]["to like"]) #adding words that are linked together. This will become easer later on
add_link(sg.words["verb"]["to like"], sg.words["verb"]["to eat"])
add_link(sg.words["noun"]["robin"], sg.words["noun"]["stick"], 2)
add_link(sg.words["noun"]["stick"], sg.words["noun"]["wood"])
add_link(sg.words["noun"]["wood"], sg.words["noun"]["water"], 2)
add_link(sg.words["verb"]["to eat"], sg.words["noun"]["corn"], 1.5)
add_link(sg.words["noun"]["rainstorm"], sg.words["noun"]["water"], 1.5)
add_link(sg.words["noun"]["sound"], sg.words["noun"]["rainstorm"])
add_link(sg.words["noun"]["song"], sg.words["noun"]["sound"])
add_link(sg.words["noun"]["horse"], sg.words["noun"]["rainstorm"])
add_link(sg.words["verb"]["to eat"], sg.words["noun"]["food"])
add_link(sg.words["noun"]["food"], sg.words["noun"]["pie"])
add_link(sg.words["noun"]["food"], sg.words["noun"]["cake"])
add_link(sg.words["noun"]["apple"], sg.words["noun"]["juice"])
add_link(sg.words["noun"]["apple"], sg.words["noun"]["banana"])
add_link(sg.words["noun"]["juice"], sg.words["noun"]["milk"], 3)
add_link(sg.words["noun"]["milk"], sg.words["noun"]["water"])
add_link(sg.words["noun"]["pear"], sg.words["noun"]["juice"], 2)
add_link(sg.words["noun"]["water"], sg.words["noun"]["bread"])
add_link(sg.words["noun"]["bread"], sg.words["noun"]["cake"], 1.5)
add_link(sg.words["noun"]["loaf"], sg.words["noun"]["bread"])
add_link(sg.words["noun"]["bread"], sg.words["noun"]["loaf"])
add_link(sg.words["noun"]["loaf"], sg.words["noun"]["corn"], 3)
add_link(sg.words["noun"]["robin"], sg.words["noun"]["song"], 1.5)
add_link(sg.words["noun"]["owl"], sg.words["noun"]["robin"], 2)
add_link(sg.words["noun"]["apple"], sg.words["noun"]["horse"], 1.25)
add_link(sg.words["verb"]["to eat"], sg.words["noun"]["apple"])"""

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