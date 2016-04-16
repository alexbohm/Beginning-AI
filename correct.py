with open("words.txt", "r") as f:
	words = f.read().splitlines()
index = 1
for word in words:
	if word[0:3]=="to ":
		print "Is '%s' Correct?\nAt Line %d" % (word, index)
		raw_input("")
	index +=1