from Tkinter import Button, Label, END, Entry, Tk, StringVar, OptionMenu
import Sen_Gen
class Add_Word(object):
	def __init__(self):
		self.types = ["noun", "adjective", "verb", "adverb", "conjunction", "preposition", "interjection"]
		self.win = Tk()
		self.win.title("Correct Word")
		self.win.geometry('{}x{}'.format(340, 150))
		self.type_w = StringVar(self.win)
		self.type_w.set(self.types[0])
		self.type_w.trace("w", lambda a,b,c: self.type_select(self.type_w.get()))
		self.menu = apply(OptionMenu, (self.win, self.type_w) + tuple(self.types))
		self.menu.grid(row=0, column=0)
		self.verb_ent = {
			'infinitive':Entry(self.win),
			'past':Entry(self.win),
			'present':Entry(self.win),
			'future':Entry(self.win)
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
		self.ind_ent= Entry(self.win)
		self.ind_ent.bind("<Return>", lambda a: self.data_in())
		self.word_edit = Entry(self.win)
		self.word_editlbl = Label(self.win, text="Word")
		self.word_lbl= Label(self.win, text="Index")
		self.save_but = Button(self.win, text="Save", command= lambda: self.save())
		self.save_but.grid(row=5, column=2)
		self.word_edit.grid(row=2, column = 1)
		self.word_editlbl.grid(row=2, column=0)
		self.ind_ent.grid(row=1, column = 1)
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
			self.word_edit.delete(0, END)
			self.word_edit.grid(row=2, column=1)
			self.word_editlbl.grid(row=2, column=0)
			for ind in self.verb_ent:
				self.verb_ent[ind].grid_remove()
				self.verb_lbl[ind].grid_remove()
	def data_in(self):
		ind = self.ind_ent.get()
		w_type = self.type_w.get()
		if w_type == "verb":
			if ind in Sen_Gen.words["verb"]:
				print "In verbs"
				for form in Sen_Gen.words["verb"][ind].forms:
					self.verb_ent[form].delete(0, END)
					self.verb_ent[form].insert(0, Sen_Gen.words["verb"][ind].forms[form])
		else:
			if ind in Sen_Gen.words[w_type]:
				print "In %ss" % (w_type)
				self.word_edit.delete(0, END)
				self.word_edit.insert(0, Sen_Gen.words[w_type][ind].word)
	def save(self):
		w_type = self.type_w.get()
		ind = self.ind_ent.get()
		if ind != "":
			if w_type == "verb":
				if ind in Sen_Gen.words["verb"]:
					Sen_Gen.words["verb"][ind].forms = {'infinitive':self.verb_ent['infinitive'].get(),'past':self.verb_ent['past'].get(),'present':self.verb_ent['present'].get(),'future':self.verb_ent['future'].get()}
					Sen_Gen.words["verb"][ind].word = self.verb_ent['infinitive'].get()
				else:
					Sen_Gen.words["verb"][ind] = Sen_Gen.Word(ind, "verb", {'infinitive':self.verb_ent['infinitive'].get(),'past':self.verb_ent['past'].get(),'present':self.verb_ent['present'].get(),'future':self.verb_ent['future'].get()})
				for w_ind in self.verb_ent:
					self.verb_ent[w_ind].delete(0, END)
			else:
				if ind in Sen_Gen.words[w_type]:
					Sen_Gen.words[w_type][ind].word = self.word_edit.get()
				else:
					Sen_Gen.words[w_type][ind] = Sen_Gen.Word(ind, w_type)
				self.word_edit.delete(0, END)
			print "Unfunctional\nDid not actually save to file"
Add_Word()