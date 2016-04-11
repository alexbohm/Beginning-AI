from Tkinter import *
class AI(object):
  def __init__(self):
    self.win = Tk()
    self.main_ent = Entry(win)
    self.main_ent.grid(row=6, column=0)
    self.ent_hist = []
    self.rep_list = []
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
    def ent_callback(self, string):
      self.ent_hist[3] = string
      self.rep_list[3] = #reply from ai
      for ind in range(0,2):
        self.ent_hist = self.ent_hist[ind+1]
        self.rep_hist = self.rep_hist[ind+1]
      #Update labels?
