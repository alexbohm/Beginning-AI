from Tkinter import Entry, END, Tk, Button, Label
import Sen_Gen as sg
import correct_gui as cg
win = Tk()
win.title("New Link")
slbl = {
	0:Label(win),
	1:Label(win, text="Node 1"),
	2:Label(win, text="Node 2"),
	3:Label(win, text="Charge")}

ent= {
	0:Label(win, text="Index"),
	1:Entry(win, bg="grey"),
	2:Entry(win, bg="grey")}
ty = {
	0:Label(win, text="Type"),
	1:Entry(win, bg="grey"),
	2:Entry(win, bg="grey")}

def Save():
	#check if words are in Sen_Gen
	word1 = ent[1].get()
	word2 = ent[2].get()
	type1 = ty[1].get()
	type2 = ty[2].get()
	if word1 != "" and word2 != "" and type1 != "" and type2 != "":
		chv = ch.get()
		if chv == "": charge = 1.0
		else:
			try: charge = float(ch.get())
			except ValueError: print "Charge must be a number"; return
		sg.words[type1][word1].links[word2] = [type2, charge]
		sg.save()
		print "linked '%s' with '%s' with a charge of %d" % (word1, word2, charge)
		ent[1].focus_set()
		for num in range(1,3):
			ent[num].configure(bg="grey")
			ty[num].configure(bg="grey")
			ent[num].delete(0, END)
	else: print "Empty Text"
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