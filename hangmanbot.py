import telepot 
import sys
import os
import random
import time
from pprint import pprint
from telepot.loop import MessageLoop
import string
KEY = "420050136:AAFN5dIMcyE9GE8Or1exUweWZ4aTHo4m034"
bot = telepot.Bot(KEY)
print ('hi')
chat_id=435591435
global word,current_word,tries,letter
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
	letter=letter.upper()
	wordk=""
	for i in range(len(word)):
		wordk+=word[i]
	f=0
	if letter in wordk :
		for i in range(len(word)):
				if word[i]==letter:
					z[i]=letter					

	else:
		f=1
	if f==0:
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
	k=""
	for i in current_word:
		k+=i
	k="Current Word = "+k
	bot.sendMessage(chat_id,k)
	


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
		bot.sendMessage(chat_id,"Congratulations!! You won!")	
		return True		   
	else:
		return False

	'''
	return if game is won
	'''

def if_lost(tries):
	if tries==0:
		bot.sendMessage(chat_id,"You have lost ! :(")
		return True
	else:
		return False

def handle(msg):
	global done,word,current_word,tries,b
	b=""
	content_type, chat_type, chat_id = telepot.glance(msg)
	print(content_type, chat_type, chat_id)
	if content_type=='text' :
		k=msg['text']
		if k=='/startgame':
			(status, word, current_word, tries) = new_game()
			for i in range(len(word)):
				if word[i]==' ':
					current_word+='/'
					b+=' / '
				else:
					current_word+='_'
					b+=' _ '
			if not status:
				bot.sendMessage(chat_id,"Initialization failed")
			else:
				bot.sendMessage(chat_id,"New game is starting!")
				bot.sendMessage(chat_id,"You get 4 tries to guess the correct movie name, All the best!!")
				b='The movie name : '+b
				bot.sendMessage(chat_id,b)				
				bot.sendMessage(chat_id,"Enter a letter")
		else:
			if len(k)==1:
				(result, current_word, tries) = guess(word, current_word, tries, k)
				
				if result:
					bot.sendMessage(chat_id,"Well Done")
					display(current_word)
				else:
					we=k+ ' was not in the word'
					tr='remaining tries= '+str(tries)
					bot.sendMessage(chat_id,we)
					bot.sendMessage(chat_id,tr)
					display(current_word)
				done = if_won(word, current_word) or if_lost(tries)
				if not done:
						bot.sendMessage(chat_id,"Enter a letter:")
				else:
					wordk=""
					for i in range(len(word)):
						wordk+=word[i]
					wordk="The Answer is "+wordk
					bot.sendMessage(chat_id,wordk) 
MessageLoop(bot, handle).run_as_thread()
print('Listening ...')
while 1:
    time.sleep(10)