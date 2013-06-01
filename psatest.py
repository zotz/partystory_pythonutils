#!/usr/bin/python
#
# use nltk to read a text and create files for each type of word and for sentence structures.
# psatest.py
# quick and dirty test of psauto.py generated files
#
# by drew Roberts
#
import sys
import os
import random
#from random import randint

#TESTING = True
TESTING = False

# Script starts from here
if len(sys.argv) < 2:
	print "Yes to if."
	totsenti = 20
else:
	print "else to if - " + sys.argv[1]
	totsenti = int(sys.argv[1])

# Begin Function definitions ============================================

def checkfilex( str ):
	filename = str
	if not os.path.exists(filename):
		file(filename, 'w').close()
		return

def writeSentence( str ):
	"This function writes a sentence based on a random sentence structure."
	# String ranSentStru = psSSs[randomGenerator.nextInt(psSSs.length)];
	sentindex = random.randint(0, len(pssentstru)-1)
	#print len(pssentstru)
	#print sentindex
	ranSentStru = pssentstru[sentindex]
	#print ranSentStru
	# completeSentence = fillSentence(ranSentStru)+" ";
	completeSentence = fillSentence(ranSentStru)
	return completeSentence
	

def fillSentence( str ):
	# public String fillSentence(String sentStru)
	"This function fills out sentence based on a passed in sentence structure."
	# String newSent;
	# String sentence, front, tword, back;
	# int lbreak;
	sentence = str
	#print "Sentence structure passes in to fillSentence is: "
	#print sentence
	newSent = ""
	# while (sentence.indexOf("{") > 0)
	while  (sentence.find("{") <> -1):
		lbreak = sentence.find("{")
		#print "lbreak is: %i"% lbreak
		npos = sentence.find("}");
		#print "npos is: %i"% npos
		# front = sentence.substring(0,lbreak);
		front = sentence[0:lbreak]
		#print "front is: " + front
		# tword = sentence.substring(lbreak+1,lbreak+3);
		tword = sentence[(lbreak+1):(npos)]
		#print "tword is: " + tword
		# back = sentence.substring(lbreak+4);
		back = sentence[(npos+1):]
		#print "back is: " + back
		# newSent += front;
		newSent += front
		# String chosenWord = chword(tword);
		chosenWord = chword(tword)
		#print "-*-*-*-*-*-*-* chosenWord is: " + chosenWord
		if (chosenWord == "i"):
			chosenWord = "I"
			if TESTING: print "--------------chosenWord was i and should now be I---------------"
		newSent += chosenWord
		#print "newSent is: " + newSent
		sentence = back
		#print "back while in the loop is: " + back
	#print "===================================back after exiting the loop is: " + back
	#print "after exiting the loop, newSent is: " + newSent
	newSent += back
	#print "after adding back on exiting the loop, newSent is: " + newSent
	sentfl = newSent[0:1].upper()
	sentrest = newSent[1:]
	newSent = sentfl+sentrest
	return newSent
	

def chword( str ):
	"This function chooses a random word of the type passed in."
	rword = "";
	tword = str
	#print "tword is: "+tword
	rword = psDict[tword][random.randint(0, len(psDict[tword])-1)]
	#print "rword is: " + rword
	# tryingto get rid of newlines that I don't know where they are coming from.
	rword = rword[:-1]
	#print "**********
	return rword

# End Function definitions ============================================


datadir="/var/dat1/psauto/data"

arrDict = {}
filDict = {}
psDict = {}
for mf in ['CC', 'CD', 'DT', 'EX', 'IN', 'JJ', 'JJR', 'JJS', 'LS', 'MD', 'NN', 'NNP', 'NNPS', 'NNS', 'PDT', 'POS', 'PRP', 'PRP$', 'RB', 'RBR', 'RBS', 'RP', 'SYM', 'TO', 'UH', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$', 'WRB']:
	arrDict[mf] = 'mf_'+mf
	filDict[mf] = 'file_'+mf+'.dat'
	psDict[mf] = 'ps'+mf



# check all key data files exist, if not create
for mf in ['CC', 'CD', 'DT', 'EX', 'IN', 'JJ', 'JJR', 'JJS', 'LS', 'MD', 'NN', 'NNP', 'NNPS', 'NNS', 'PDT', 'POS', 'PRP', 'PRP$', 'RB', 'RBR', 'RBS', 'RP', 'SYM', 'TO', 'UH', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$', 'WRB']:
	checkfilex("%s/%s" % (datadir, filDict[mf]))
	arrDict[mf] = open('%s/file_%s.dat' % (datadir, mf), 'r')
	psDict[mf] = arrDict[mf].readlines()
	#print psDict[mf][2]


fixsent = ""

# open sentence structure file
mf_sent_stru = open('%s/file_sentstru.dat' % datadir, 'r')
pssentstru = mf_sent_stru.readlines()
if TESTING: print "read in %i sentence structures." % len(pssentstru)




for x in range(0,totsenti):
	thissentence = writeSentence("")
	print "===================================================="
	print thissentence


mf_sent_stru.close()
# ftagged.close()

for mf in ['CC', 'CD', 'DT', 'EX', 'IN', 'JJ', 'JJR', 'JJS', 'LS', 'MD', 'NN', 'NNP', 'NNPS', 'NNS', 'PDT', 'POS', 'PRP', 'PRP$', 'RB', 'RBR', 'RBS', 'RP', 'SYM', 'TO', 'UH', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$', 'WRB']:
	arrDict[mf].close()
	#print "closing file: ", 'file_'+mf+'.dat'
