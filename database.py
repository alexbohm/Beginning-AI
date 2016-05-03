from random import randrange
from os import getcwd
class Word(object):
	def __init__(self, word,w_type,links = {}, forms = {}):
		self.line = line; self.word = word; self.type = w_type; self.links = links
		if w_type == "verb": self.forms = forms
	def add_link(self, word, charge):
		if word not in self.links[word]:
			self.links[word] = charge
words = {"noun":{}, "adjective":{}, "verb":{}, "adverb":{}, "conjunction":{}, "preposition":{}, "interjection":{}}
def save():
	with open("%s/words.txt" % (getcwd()), "w") as f:
		for w_type in words:
			for cla in words[w_type]:
				if w_type =="verb": f.write("%s|%s|%s|%s\n" % (words[w_type][cla].word, words[w_type][cla].type, str(words[w_type][cla].links), str(words[w_type][cla].forms)))
				else: f.write("%s|%s|%s\n" % (words[w_type][cla].word, words[w_type][cla].type, str(words[w_type][cla].links)))

with open("%s/words.txt" % (getcwd())) as f:
	for line in f.read().splitlines():
		temp = line.split("|")
		if temp[1]=="verb": words["verb"][temp[0]] = Word(temp[0], "verb", eval(temp[2]), eval(temp[3]))
		else: words[temp[1]][temp[0]] = Word(temp[0], temp[1], eval(temp[2]))