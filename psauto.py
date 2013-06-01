#!/usr/bin/python
#
# use nltk to read a text and create files for each type of word and for sentence structures.
#
# by drew Roberts
#
import sys
from subprocess import call
from nltk.tag import pos_tag  
from nltk.tokenize import word_tokenize 
import nltk.data

datadir="/var/dat1/psauto/data"
fixsent = ""
arrDict = {}
#arrDict = { 'CC': 'mf_CC', 'CD': 'mf_CD', 'DT': 'mf_DT', 'EX': 'mf_EX', 'IN': 'mf_IN', 'JJ': 'mf_JJ', 'JJR': 'mf_JJR', 'JJS': 'mf_JJS', 'LS': 'mf_LS', 'MD': 'mf_MD', 'NN': 'mf_NN', 'NNP': 'mf_NNP', 'NNPS': 'mf_NNPS', 'NNS': 'mf_NNS', 'PDT': 'mf_PDT', 'POS': 'mf_POS', 'PRP': 'mf_PRP', 'PRP$': 'mf_PRP$', 'RB': 'mf_RB', 'RBR': 'mf_RBR', 'RBS': 'mf_RBS', 'RP': 'mf_RP', 'SYM': 'mf_SYM', 'TO': 'mf_TO', 'UH': 'mf_UH', 'VB': 'mf_VB', 'VBD': 'mf_VBD', 'VBG': 'mf_VBG', 'VBN': 'mf_VBN', 'VBP': 'mf_VBP', 'VBZ': 'mf_VBZ', 'WDT': 'mf_WDT', 'WP': 'mf_WP', 'WP$': 'mf_WP$', 'WRB': 'mf_WRB'}
for mf in ['CC', 'CD', 'DT', 'EX', 'IN', 'JJ', 'JJR', 'JJS', 'LS', 'MD', 'NN', 'NNP', 'NNPS', 'NNS', 'PDT', 'POS', 'PRP', 'PRP$', 'RB', 'RBR', 'RBS', 'RP', 'SYM', 'TO', 'UH', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$', 'WRB']:
	arrDict[mf] = 'mf_'+mf


for mf in ['CC', 'CD', 'DT', 'EX', 'IN', 'JJ', 'JJR', 'JJS', 'LS', 'MD', 'NN', 'NNP', 'NNPS', 'NNS', 'PDT', 'POS', 'PRP', 'PRP$', 'RB', 'RBR', 'RBS', 'RP', 'SYM', 'TO', 'UH', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$', 'WRB']:
#for mf in ['CC', 'CD', 'DT', 'EX']:
	print "opening file: ", 'file_'+mf+'.dat'
	# I can't get this to work right for me.
	# hence I open and close repeatedly in the loops further below
	arrDict[mf] = open('%s/file_%s.dat' % (datadir, mf), 'a+')
	# seems to open things
	#arrDict[mf].write('Processing:  '+mf+"\n")


print "===============Do some cool stuff here.===============================\n"

# open sentence structure file
fsent_stru = open('%s/file_%s.dat' % (datadir, 'sentstru'), 'a+')
ftagged = open("/var/dat1/psauto/data/file_tagged.txt", 'a+')

sentence_detector = nltk.data.load('tokenizers/punkt/english.pickle')

filename = ""
filename = sys.argv[-1]
print filename
if filename == "psauto.py":
	print "no file passed in to work on, quitting."
	sys.exit()

# Script starts from here
if len(sys.argv) < 2:
	print "no file passed in to work on, quitting."
	sys.exit()


print "working on file: "
print filename
print

# this is how we handle each sentence:
# pos_tag(word_tokenize("John's big idea isn't all that bad.")) 

rfile = open(filename)
data = rfile.read()
# print '\n-----\n'.join(sentence_detector.tokenize(data))
sentences = sentence_detector.tokenize(data)
#print '\n-----\n'.join(sentences)
# print type(sentences)
print "Beginning run"
print "===================================================================="
numsentences = len(sentences)
print "working on a total of %i sentences." % numsentences
print "===================================================================="
tsent = 1
for sentence in sentences:
	finsent = pos_tag(word_tokenize(sentence))
	#ftagged.write(str(finsent))
	for stuple in finsent:
		# hmmm, what to do here?
		#print "Tupple is: ", stuple
		#print "\n======================\n"
		if stuple[1] == "FW":
			print "************* Found a Foreigh Word ************************\n"
			sys.exit()
			fixsent = fixsent+stuple[0]
			arrDict[stuple[1]].write(stuple[0].lower())
			arrDict[stuple[1]].write("\n")
		elif stuple[1] in [',','.','?','!',':',';']:
			# print stuple[1]
			fixsent = fixsent[0:-1]
			fixsent = fixsent+stuple[0]
			fixsent = fixsent+" "
		elif stuple[1] in ['CC', 'CD', 'DT', 'EX', 'IN', 'JJ', 'JJR', 'JJS', 'LS', 'MD', 'NN', 'NNP', 'NNPS', 'NNS', 'PDT', 'POS', 'PRP', 'PRP$', 'RB', 'RBR', 'RBS', 'RP', 'SYM', 'TO', 'UH', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$', 'WRB']:
			fixsent = fixsent+"{"+stuple[1]+"}"
			fixsent = fixsent+" "
			# write to speech part data files
			arrDict[stuple[1]].write(stuple[0].lower())
			arrDict[stuple[1]].write("\n")
		else:
			#print "not punctuation"
			#fixsent = fixsent+"{"+stuple[1]+"}"
			#print "=============----------- " + stuple[1] + "--------------======================================"
			#print "=============----------- " + stuple[0] + "--------------======================================"
			fixsent = fixsent+stuple[0]
			fixsent = fixsent+" "

	fixsent = fixsent[0:-1]
	fixsent += '\n'
	# write to sentence structure file	
	fsent_stru.write(fixsent)
	print "Progress: finished %i of %i sentences." % (tsent, numsentences)
	tsent += 1
	# clear fixsent
	fixsent = ""

	
for mf in ['CC', 'CD', 'DT', 'EX', 'IN', 'JJ', 'JJR', 'JJS', 'LS', 'MD', 'NN', 'NNP', 'NNPS', 'NNS', 'PDT', 'POS', 'PRP', 'PRP$', 'RB', 'RBR', 'RBS', 'RP', 'SYM', 'TO', 'UH', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$', 'WRB']:
	arrDict[mf].close()
	print "closing file: ", 'file_'+mf+'.dat'


rfile.close()
fsent_stru.close()
ftagged.close()
