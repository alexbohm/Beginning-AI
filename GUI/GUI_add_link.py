from Tkinter import Entry, END, Tk, Button, Label
import Sen_Gen as sg
import Connect_N as cn
win = Tk()
win.title("New Link")
slbl = {
	0:Label(win),
	1:Label(win, text="Node 1"),
	2:Label(win, text="Node 2"),
	3:Label(win, text="Charge")
}

ent= {
	0:Label(win, text="Index"),
	1:Entry(win),
	2:Entry(win)
}
ty = {
	0:Label(win, text="Type"),
	1:Entry(win),
	2:Entry(win)
}
def Save():
	#check if words are in Sen_Gen
	word1 = ent[1].get()
	word2 = ent[2].get()
	type1 = ty[1].get()
	type2 = ty[2].get()
	if word1 != "" and word2 != "":
		chv = ch.get()
		if chv == "":
			charge = 1
		else:
			charge = float(ch.get())
		temp = cn.add_link(sg.words[type1][word1], sg.words[type2][word2], charge)
		print temp
	else:
		print "Empty Text"


sv = Button(win, text="Save", command= lambda: Save())
ch = Entry(win)
for en in ent:
	slbl[en].grid(row=en, column=0)
	ent[en].grid(row=en, column=1)
	ty[en].grid(row=en, column=2)

sv.grid(row=3, column=3)
ch.grid(row=3, column=1)
slbl[3].grid(row=3, column=0)

win.mainloop()