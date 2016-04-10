import Sen_Gen as sg
class Link (object):
	def __init__(self, node1, node2, charge_deduc=1):
		self.node1 = node1 #word1
		self.node2 = node2 #word2
		self.cd = charge_deduc #the amount of charge deducted from initial
	def charge_reduc(self, charge):
		return charge - self.cd #charge only goes 10 links
		#that way, if the starting word of the network is "ridiculous", it doesn't end up on the other end
		#of the network saying "mommy"

links = []

class Network(object):
	def __init__(self, nodes=[], links=[]):
		self.nodes = nodes #just words--not sure whether I have need the nodes
		self.links = links #essential for the follow function
		self.chg = 10
	def follow(self, word1):
		crawled, self.path = [], [] #crawled will become useful later
		for e in links:				#path is the sentence
			if e.node1==word1:
				good_link = e
				crawled.append(e)
		old_node = good_link
		self.path.append(old_node.node1)
		while self.chg>0:
			for e in links:
				if e.node1 == old_node.node2: #check second element of link
					self.path.append(e.node1)
					self.chg = e.charge_reduc(self.chg) #make sure the thought only goes so far
					old_node = e #used for next iteration



def add_link(one, two, charge_deduc=1):
	links.append(Link(one, two, charge_deduc))

blue = sg.words
nodes = []
sentence_sequence = [[]]
y = sg.Word("","")
for e in blue:
	for i in e:
		nodes.append(sg.Word(i, e))
pie = sg.words["noun"]["pie"]
likes = sg.words["verb"]["to like"]
eat = sg.words["verb"]["to eat"]
food = sg.words["noun"]["food"]
add_link(pie, likes) #adding words that are linked together. This will become easer later on
add_link(likes, eat)
add_link(eat, food)
add_link(food, pie)
big_net = Network(nodes, links)
big_net.follow(pie)
for e in big_net.path:
	print e.word
sentence_sequence.append(big_net.path)

#in this case, the path is the sentence
#by adding connections, we construct a network in big_net
#which allows the ai to come up with paths that actually make sense
#the sentence sequence allows us to store the sentences
#do not fix anything.
#this is officially my first machine learning network.



















