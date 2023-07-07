import string

text = input("Enter a sentence:")
table = str.maketrans("", "", string.punctuation)
new_text = text.translate(table)
new_text = new_text.lower()
wordlist = new_text.split()
dict = {}

for i in wordlist:
	if i not in dict:
		dict[i] = 1
	else:
		dict[i] += 1

for i in dict.keys():
	print(i,":",dict[i])
	

