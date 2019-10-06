#basic, repeat, len(), count(), find(), replace()

def monty_python_quote():
	return "We interrupt this program to annoy you and make things generally irritating!"
print(monty_python_quote())

def spam(text, n):
	return text * n
print(spam("developers", 4))

def same_length(word1, word2):
	return len(word1) == len(word2)
print(same_length('hello', 'world'))
print(same_length('hovercraft', 'eels'))

def occurences(text, token):
	return text.count(token)

def replace_text(sentence):
	sentence = sentence.replace('cheeky', 'naughty')
	return sentence