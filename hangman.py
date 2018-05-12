import os
import random

def get_new_word():
	words = [
			['J','O','H','N',' ','W','I','C','K'],
			['I','N','C','E','P','T','I','O','N'],
			['A','V','E','N','G','E','R','S'],
			['G','R','A','V','I','T','Y'],
			['T','H','E',' ','R','E','V','E','N','A','N','T'],
			['F','I','T','O','O','R'],
			['S','P','I','D','E','R','M','A','N',' ','H','O','M','E','C','O','M','I','N','G'],
			['F','I','G','H','T',' ','C','L','U','B'],
			['K','U','R','B','A','A','N'],
			['I','N','T','E','R','S','T','E','L','L','A','R'],
			['I','C','E',' ','A','G','E',' ','3'],
			['D','E','A','D',' ','P','O','E','T','S',' ','S','O','C','I','E','T','Y'],
			['P','U','L','P',' ','F','I','C','T','I','O','N'],
			['M','S',' ','D','H','O','N','I',' ','T','H','E',' ','U','N','T','O','L','D',' ','S','T','O','R','Y'],
			['F','I','F','T','Y',' ','S','H','A','D','E','S',' ','O','F',' ','G','R','E','Y'],
			['I','R','O','N',' ','M','A','N',' ','2'],
			['C','H','E','N','N','A','I',' ','E','X','P','R','E','S','S']
			]
	secure_random=random.SystemRandom()
	word=secure_random.choice(words)
	'''
	Random.randint(beginning, end) can be used to 
	generate random integers between beginning and end.
	return a random movie name from the list of words
	'''
	return word

def new_game():
	k=0
	word=get_new_word()
	current_word=""
	tries=4
	stri=''
	for i in range(len(word)):
		if(word[i]==' '):
			continue
		else:
			stri+=word[i]

	if stri.isalnum():
		status=True	
	
	else:
		status=False
		word=""
		current_word=""
		tries=4
			 
	return (status,word,current_word, tries)
		


def guess(word, current_word, tries, letter):
	z=list(current_word)
	wordk=""
	for i in range(len(word)):
		wordk+=word[i]
		
	word=list(wordk)
	k=0
	if letter in wordk :
		for i in range(len(word)):
				if word[i]==letter:
					z[i]=letter
				elif word[i]==" ":
					z[i]='/'

	else:
		k=1
	if k==0:
		current_word=""
		for i in range(len(z)):
			current_word+=z[i]
		status=True
	else:
		tries-=1
		status=False
	return (status,current_word,tries)




def display(current_word):
	os.system('cls')
	print("\n\nCurrent Word = ", end = '')
	for i in current_word:
		print(i,end = '')
	print()

def get_letter():
	letter=input("Enter a letter : ")
	letter=letter.upper()
	'''
	Return an upper case letter
	'''
	return letter

def if_won(word, current_word):
	wordk,rev="",""
	for i in range(len(word)):
		if(word[i]!=' '):
			wordk+=word[i]
	s=list(current_word)
	for i in range(len(s)):
		if s[i]!='/':
			rev+=s[i]

	if wordk==rev :
		print("Congratulations!! You won!")
		return True	   
	else:
		return False

	'''
	return if game is won
	'''

def if_lost(tries):
	if tries==0:
		print("You have lost ! :(")
		return True
	else:
		return False
	'''
	Return if game has been lost
	'''

def game():
	(status, word, current_word, tries) = new_game()
	for i in range(len(word)):
		if word[i]==" ":
			current_word+='/'
		else:
			current_word+='_'
	sw=list(current_word)
	for i in range(len(sw)):
		print(sw[i],end=" ")
	if not status:
		print("Initialization failed")
		return -1
	done = False
	display(current_word)
	while not done:
		letter = get_letter()
		(result, current_word, tries) = guess(word, current_word, tries, letter)
		display(current_word)
		if result:
			print('Well done')
		else:
			print(letter + ' was not in the word')
			print('remaining tries = ' + str(tries))
		done = if_won(word, current_word) or if_lost(tries)

if __name__ == '__main__':
	game()
