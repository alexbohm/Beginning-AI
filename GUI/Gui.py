from Tkinter import *
class Add_Word(object):
	def __init__(self):
		self.types = ["noun", "adjective", "verb", "adverb", "conjunction", "preposition", "interjection"]
		self.win = Tk()
		self.win.geometry('{}x{}'.format(200, 200))
		self.type_w = StringVar(self.win)
		self.type_w.set(self.types[0])
		self.type_w.trace("w", lambda a,b,c: self.callback(self.type_w.get()))
		self.menu = apply(OptionMenu, (self.win, self.type_w) + tuple(self.types))
		self.menu.grid(row=0, column=0)
		self.verb_ent = {
			1:Entry(self.win),#'infinitive'
			2:Entry(self.win),#'past'
			3:Entry(self.win),#'present'
			4:Entry(self.win)#'future'	
		}
		self.verb_lbl = {
			1:Label(self.win, text='infinitive'),
			2:Label(self.win, text='past'),
			3:Label(self.win, text='present'),
			4:Label(self.win, text='future')}
		self.word_ent= Entry(self.win)
		self.word_lbl= Label(self.win, text="Word")
		self.word_ent.grid(row=1, column = 1)
		self.word_lbl.grid(row=1, column = 0)
		self.win.mainloop()
	def callback(self,w_type):
		if w_type == "verb":
			self.word_ent.grid_remove()
			self.word_lbl.grid_remove()
			for ind in self.verb_ent:
				self.verb_ent[ind].grid(row=ind, column=1)
				self.verb_lbl[ind].grid(row=ind, column=0)
		else:
			for ind in self.verb_ent:
				self.verb_ent[ind].grid_remove()
				self.verb_lbl[ind].grid_remove()
			self.word_ent.grid(row=1, column = 1)
			self.word_lbl.grid(row=1, column = 0)
Add_Word()