from Tkinter import *
class GUI(object):
	def __init__(self):
		self.win = Tk()
		self.win.geometry('{}x{}'.format(220, 150))
		self.win.title("AI")
		self.main_ent = Entry(self.win)
		self.main_ent.bind("<Return>", lambda a: self.ent_callback())
		self.main_ent.grid(row=6, column=0)
		ent_but = Button(self.win, text="Say", command=self.ent_callback)
		ent_but.grid(row=6, column=1)
		self.ent_hist = []#["", "", "", ""]
		self.rep_hist = []#["", "", "", ""]
		for ind in range(0,4):
			self.ent_hist.append("")
			self.rep_hist.append("")
		print self.ent_hist, self.rep_hist
		self.hist = {
			0:Label(self.win, text=self.ent_hist[0]),
			1:Label(self.win, text=self.rep_hist[0]),
			2:Label(self.win, text=self.ent_hist[1]),
			3:Label(self.win, text=self.rep_hist[1]),
			4:Label(self.win, text=self.ent_hist[2]),
			5:Label(self.win, text=self.rep_hist[2])}
		for ind in self.hist:
			self.hist[ind].grid(row=ind, column=0)
		self.win.mainloop()
	def ent_callback(self):
		user = self.main_ent.get()
		if user != "":
			self.main_ent.delete(0, END)
			self.ent_hist[3] = user
			self.rep_hist[3] = "reply" #reply from ai
			for ind in range(0,3):
				self.ent_hist[ind] = self.ent_hist[ind+1]
				self.rep_hist[ind] = self.rep_hist[ind+1]
			self.hist[0].configure(text=self.ent_hist[0]) # will turn into for loop if possible
			self.hist[1].configure(text=self.rep_hist[0])
			self.hist[2].configure(text=self.ent_hist[1])
			self.hist[3].configure(text=self.rep_hist[1])
			self.hist[4].configure(text=self.ent_hist[2])
			self.hist[5].configure(text=self.rep_hist[2])			
GUI()