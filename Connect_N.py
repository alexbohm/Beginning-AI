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
	def follow(self, word1):
		crawled, self.path = [], [] #crawled will become useful later
		for e in links:				#path is the sentence
			if e.node1==word1:
				old_link = e
				crawled.append(e)
		self.path.append(old_link.node1)
		i = 0
		while self.chg>0:
			for e in links: #The problem lies here
				if e.node1 == old_link.node2 and e not in crawled: #check second element of link
					self.path.append(e.node1)
					self.chg = e.charge_reduc(self.chg) #make sure the thought only goes so far
					old_link = e #used for next iteration
					crawled.append(e)
				elif links[-1] == e:
					self.chg = self.chg - 1


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
juice = sg.words["noun"]["juice"]
cake = sg.words["noun"]["cake"]
apple = sg.words["noun"]["apple"]
banana = sg.words["noun"]["banana"]
corn = sg.words["noun"]["corn"]
milk = sg.words["noun"]["milk"]
pear = sg.words["noun"]["pear"]
water = sg.words["noun"]["water"]
bread = sg.words["noun"]["bread"]
goose = sg.words["noun"]["goose"]
horse = sg.words["noun"]["horse"]
kitten = sg.words["noun"]["kitten"]
loaf = sg.words["noun"]["loaf"]
owl = sg.words["noun"]["owl"]
rabbit = sg.words["noun"]["rabbit"]
robin = sg.words["noun"]["robin"]
song = sg.words["noun"]["song"]
rainstorm = sg.words["noun"]["rainstorm"]
sound = sg.words["noun"]["sound"]
stick = sg.words["noun"]["sound"]
wood = sg.words["noun"]["wood"]
add_link(pie, likes) #adding words that are linked together. This will become easer later on
add_link(likes, eat)
add_link(robin, stick, 2)
add_link(stick, wood)
add_link(wood, water, 2)
add_link(eat, corn, 1.5)
add_link(rainstorm, water, 1.5)
add_link(sound, rainstorm)
add_link(song, sound)
add_link(horse, rainstorm)
add_link(eat, food)
add_link(food, pie)
add_link(food, cake)
add_link(apple, juice)
add_link(apple, banana)
add_link(juice, milk, 3)
add_link(milk, water)
add_link(pear, juice, 2)
add_link(water, bread)
add_link(bread, cake, 1.5)
add_link(loaf, bread)
add_link(bread, loaf)
add_link(loaf, corn, 3)
add_link(robin, song, 1.5)
add_link(owl, robin, 2)
add_link(apple, horse, 1.25)
add_link(eat, apple)
big_net = Network(nodes, links)
big_net.follow(apple)
for e in big_net.path:
	print e.word
sentence_sequence.append(big_net.path)

#in this case, the path is the sentence
#by adding connections, we construct a network in big_net
#which allows the ai to come up with paths that actually make sense
#the sentence sequence allows us to store the sentences
#do not fix anything.
#this is officially my first machine learning network.


















