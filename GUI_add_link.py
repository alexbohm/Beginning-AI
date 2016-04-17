from Tkinter import Entry, END, Tk, Button, Label
import Sen_Gen as sg
import Connect_N as cn
import correct_gui as cg
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
	1:Entry(win, bg="grey"),
	2:Entry(win, bg="grey")
}
ty = {
	0:Label(win, text="Type"),
	1:Entry(win, bg="grey"),
	2:Entry(win, bg="grey")
}

def Save():
	#check if words are in Sen_Gen
	word1 = ent[1].get()
	word2 = ent[2].get()
	type1 = ty[1].get()
	type2 = ty[2].get()
	if word1 != "" and word2 != "" and type1 != "" and type2 != "":
		chv = ch.get()
		if chv == "":
			charge = 1
		else:
			charge = float(ch.get())
		cn.add_link(sg.words[type1][word1], sg.words[type2][word2], charge)
		#print cn.links[-1].node1.word, cn.links[-1].node2.word
		print "linked '%s' with '%s'" % (word1, word2)
		ent[1].focus_set()
	else:
		print "Empty Text"
def check(num):
	word = ent[num].get()
	w_type = ty[num].get()
	if w_type in sg.words and word in sg.words[w_type]:
		ent[num].configure(bg="green")
		ty[num].configure(bg="green")
	else:
		ent[num].configure(bg="red")
		ty[num].configure(bg="red")
		if w_type not in sg.words:
			print "invalid type"
		else:
			cg.Add_Word()
			cg.exit_save()



sv = Button(win, text="Save", command= lambda: Save())
ch = Entry(win)
for en in ent:
	slbl[en].grid(row=en, column=0)
	ent[en].grid(row=en, column=1)
	ty[en].grid(row=en, column=2)

sv.grid(row=3, column=3)
ch.grid(row=3, column=1)
slbl[3].grid(row=3, column=0)
ent[1].bind("<Return>", lambda a: ty[1].focus_set())
ent[2].bind("<Return>", lambda a: ty[2].focus_set())
ty[1].bind("<Return>", lambda a: ent[2].focus_set())
ty[2].bind("<Return>", lambda a: ch.focus_set())
ch.bind("<Return>", lambda a: sv.focus_set())
sv.bind("<Return>", lambda a: Save())
ty[1].bind("<FocusOut>", lambda a: check(1))
ty[2].bind("<FocusOut>", lambda a: check(2))
win.mainloop()