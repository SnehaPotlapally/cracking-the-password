import base64
import hashlib
import time
import itertools
import sys

counter = 1
sha1_pass = open('passwords.txt','r')
passw=sha1_pass.read().splitlines()

dic_open = open('dictionary.txt','r')
dic = dic_open.read().splitlines()
dic_open.close()
sha1_pass.close()
hashed_dic = []

 


#Case 1 : Straight Search
for i in dic:
	hashed_dic.append(hashlib.sha1(i.encode('utf-8')).hexdigest())	
for j in passw:
	k = j.split(' ')[1]
	for l in hashed_dic:
		if(str(k) == str(l)):
			print("Match found   " + dic[hashed_dic.index(l)] + " " +l)
			counter=counter+1

#Case 2 : Number Combinations using permutations

nums = [int(str(i)) for i in range(0,9)]

for j in range (1,9):
	for j in itertools.product(nums, repeat=j):
		j = ''.join(str(j))
		h = hashlib.sha1(j.encode('utf-8')).hexdigest()
		if h in passw:
			print("Match found " +j+"  "+h)
			counter=counter+1
#Case 3 :  Word Combinations
two_word = []
for i in dic :
	for j in dic :
		word = i+j
		two_word.append(hashlib.sha1(word.encode('utf-8')).hexdigest())
for j in passw:
	k = j.split(' ')[1]
	for l in two_word:
		if(str(k) == str(l)):
			print("Match found   " + dic[two_word.index(l)]+ " " + l)
			counter=counter+1



#Case 4 Combination of Words and Numbers

for j in itertools.product(dic, repeat = 2):
	for k in range(1,6):
		for i in itertools.product(nums, repeat = k):
			combined_string = ''.join(str(j)) + ''.join(str(i))
			hash1 = hashlib.sha1(combined_string.encode('utf-8')).hexdigest()
			if( hash1 in passw):
				print("Match found " + combined_string +"  " + hash1)
				counter=counter+1



print( "The number of passwords cracked are " + counter)