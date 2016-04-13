from Tkinter import *
import Sen_Gen
class Add_Word(object):
	def __init__(self):
		self.types = ["noun", "adjective", "verb", "adverb", "conjunction", "preposition", "interjection"]
		self.win = Tk()
		self.win.title("Correct Word")
		self.win.geometry('{}x{}'.format(280, 140))
		self.type_w = StringVar(self.win)
		self.type_w.set(self.types[0])
		self.type_w.trace("w", lambda a,b,c: self.type_select(self.type_w.get()))
		self.menu = apply(OptionMenu, (self.win, self.type_w) + tuple(self.types))
		self.menu.grid(row=0, column=0)
		self.verb_ent = {
			'infinitive':Entry(self.win),#
			'past':Entry(self.win),#
			'present':Entry(self.win),#
			'future':Entry(self.win)#
		}
		self.verb_order = {
			'infinitive':2,
			'past':3,
			'present':4,
			'future':5
		}
		self.verb_lbl = {
			'infinitive':Label(self.win, text='infinitive'),
			'past':Label(self.win, text='past'),
			'present':Label(self.win, text='present'),
			'future':Label(self.win, text='future')}
		self.word_ent= Entry(self.win)
		self.word_ent.bind("<Return>", lambda a: self.data_in())
		self.word_edit = Entry(self.win)
		self.word_editlbl = Label(self.win, text="Word")
		self.word_lbl= Label(self.win, text="Index")
		self.word_edit.grid(row=2, column = 1)
		self.word_editlbl.grid(row=2, column=0)
		self.word_ent.grid(row=1, column = 1)
		self.word_lbl.grid(row=1, column = 0)
		self.win.mainloop()
	def type_select(self,w_type):
		if w_type == "verb":
			self.word_edit.grid_remove()
			self.word_editlbl.grid_remove()
			for ind in self.verb_ent:
				self.verb_ent[ind].grid(row=self.verb_order[ind], column=1)
				self.verb_lbl[ind].grid(row=self.verb_order[ind], column=0)
		else:
			self.word_edit.grid(row=2, column=1)
			self.word_editlbl.grid(row=2, column=0)
			for ind in self.verb_ent:
				self.verb_ent[ind].grid_remove()
				self.verb_lbl[ind].grid_remove()
	def data_in(self):
		ind = self.word_ent.get()
		w_type = self.type_w.get()
		if w_type == "verb":
			if ind in Sen_Gen.words["verb"]:
				print "already in verbs"
				for form in Sen_Gen.words["verb"][ind].forms:
					self.verb_ent[form].delete(0, END)
					self.verb_ent[form].insert(0, Sen_Gen.words["verb"][ind].forms[form])
		else:
			if ind in Sen_Gen.words[w_type]:
				print "already in %ss" % (w_type)
				self.word_edit.delete(0, END)
				self.word_edit.insert(0, Sen_Gen.words[w_type][ind].word)
Add_Word()