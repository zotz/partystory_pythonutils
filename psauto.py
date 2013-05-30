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
for mf in ['CC', 'CD', 'DT', 'EX', 'IN', 'JJ', 'JJR', 'JJS', 'LS', 'MD', 'NN', 'NNP', 'NNPS', 'NNS', 'PDT', 'POS', 'PRP', 'PRP$', 'RB', 'RBR', 'RBS', 'RP', 'SYM', 'TO', 'UH', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$', 'WRB']:
	print "opening file: ", 'file_'+mf
	# I can't get this to work right for me.
	# hence I open and close repeatedly in the loops further below
	# file = open('myfile.dat', 'a+')
	# f = open('%s.csv' % name, 'wb')
	#locals()[ "f%02d" % i ] = open( "file%02d.txt" % i )
	# locals()[ "%s/file_%s.dat" % (datadir,mf) ] = open('%s/file_%s.dat' % (datadir, mf), 'a+')

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
			fixsent = fixsent+stuple[0]
			mfile = open('%s/file_%s.dat' % (datadir, stuple[1]), 'a+')
			#datadir+"/file_"+str(stuple[1])+".dat".write(str(stuple[1]))
			mfile.write(stuple[0].lower())
			mfile.write("\n")
			mfile.close()
		else:
			#print stuple[1]
			if stuple[1] in [',','.','?','!',':',';']:
				# print stuple[1]
				fixsent = fixsent[0:-1]
				fixsent = fixsent+stuple[0]
				fixsent = fixsent+" "
			else:
				#print "not punctuation"
				fixsent = fixsent+"{"+stuple[1]+"}"
				fixsent = fixsent+" "
				# write to speech part data files
				mfile = open('%s/file_%s.dat' % (datadir, stuple[1]), 'a+')
				mfile.write(stuple[0].lower())
				mfile.write("\n")
				mfile.close()
	fixsent = fixsent[0:-1]
	fixsent += '\n'
	# write to sentence structure file	
	fsent_stru.write(fixsent)
	print "Progress: finished %i of %i sentences." % (tsent, numsentences)
	tsent += 1
	# clear fixsent
	fixsent = ""


rfile.close()
fsent_stru.close()
ftagged.close()

# Now sort data files and eliminate duplicates
# call(["ls", "-l"])
call(["/var/dat1/psauto/pssortem.sh"])
