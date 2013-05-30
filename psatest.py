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
		#print "chosenWord is: " + chosenWord
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
	# String chword(String ptword)
	# String rword, tword;
	# int choose;
	rword = "";
	tword = str
	#print "tword inside chword() is: " + tword
	# if (tword.equals("AD"))
	if (tword == "CC"):
		rword = pscc[random.randint(0, len(pscc)-1)]
	elif (tword == "CD"):
		if TESTING: print "len(pscd) is %i)" % len(pscd)
		rword = pscd[random.randint(0, len(pscd)-1)]
	elif (tword == "DT"):
		rword = psdt[random.randint(0, len(psdt)-1)]
	elif (tword == "EX"):
		rword = psex[random.randint(0, len(psex)-1)]
	elif (tword == "IN"):
		rword = psin[random.randint(0, len(psin)-1)]
	elif (tword == "JJ"):
		rword = psjj[random.randint(0, len(psjj)-1)]
	elif (tword == "JJR"):
		rword = psjjr[random.randint(0, len(psjjr)-1)]
	elif (tword == "JJS"):
		rword = psjjs[random.randint(0, len(psjjs)-1)]
	elif (tword == "LS"):
		rword = psls[random.randint(0, len(psls)-1)]
	elif (tword == "MD"):
		rword = psmd[random.randint(0, len(psmd)-1)]
	elif (tword == "NN"):
		rword = psnn[random.randint(0, len(psnn)-1)]
	elif (tword == "NNP"):
		rword = psnnp[random.randint(0, len(psnnp)-1)]
	elif (tword == "NNPS"):
		rword = psnnps[random.randint(0, len(psnnps)-1)]
	elif (tword == "NNS"):
		rword = psnns[random.randint(0, len(psnns)-1)]
	elif (tword == "PDT"):
		rword = pspdt[random.randint(0, len(pspdt)-1)]
	elif (tword == "POS"):
		rword = pspos[random.randint(0, len(pspos)-1)]
	elif (tword == "PRP"):
		rword = psprp[random.randint(0, len(psprp)-1)]
	elif (tword == "PRP$"):
		rword = psprpdol[random.randint(0, len(psprpdol)-1)]
	elif (tword == "RB"):
		# print "len(psrb) is %i)" % len(psrb)
		rword = psrb[random.randint(0, len(psrb)-1)]
	elif (tword == "RBR"):
		rword = psrbr[random.randint(0, len(psrbr)-1)]
	elif (tword == "RBS"):
		rword = psrbs[random.randint(0, len(psrbs)-1)]
	elif (tword == "RP"):
		rword = psrp[random.randint(0, len(psrp)-1)]
	elif (tword == "SYM"):
		rword = pssym[random.randint(0, len(pssym)-1)]
	elif (tword == "TO"):
		rword = psto[random.randint(0, len(psto)-1)]
	elif (tword == "UH"):
		rword = psuh[random.randint(0, len(psuh)-1)]
	elif (tword == "VB"):
		rword = psvb[random.randint(0, len(psvb)-1)]
	elif (tword == "VBD"):
		rword = psvbd[random.randint(0, len(psvbd)-1)]
	elif (tword == "VBG"):
		rword = psvbg[random.randint(0, len(psvbg)-1)]
	elif (tword == "VBN"):
		rword = psvbn[random.randint(0, len(psvbn)-1)]
	elif (tword == "VBP"):
		rword = psvbp[random.randint(0, len(psvbp)-1)]
	elif (tword == "VBZ"):
		rword = psvbz[random.randint(0, len(psvbz)-1)]
	elif (tword == "WDT"):
		if TESTING: print "len pswdt = %i" % len(pswdt)
		rword = pswdt[random.randint(0, len(pswdt)-1)]
	elif (tword == "WP"):
		rword = pswp[random.randint(0, len(pswp)-1)]
	elif (tword == "WP$"):
		rword = pswpdol[random.randint(0, len(pswpdol)-1)]
	elif (tword == "WRB"):
		rword = pswrb[random.randint(0, len(pswrb)-1)]
	#print "rword is: " + rword
	# tryingto get rid of newlines that I don't know where they are coming from.
	rword = rword[:-1]
	#print "******************** "+rword+" "+rword+" "+rword+"****************"
	return rword

# End Function definitions ============================================


datadir="/var/dat1/psauto/data"

# check all key data files exist, if not create
#filename = "%s/file_CC.dat" % datadir
#if not os.path.exists(filename):
#    file(filename, 'w').close()
checkfilex("%s/file_CC.dat" % datadir)
checkfilex("%s/file_CD.dat" % datadir)
checkfilex("%s/file_DT.dat" % datadir)
checkfilex("%s/file_EX.dat" % datadir)
checkfilex("%s/file_IN.dat" % datadir)
checkfilex("%s/file_JJ.dat" % datadir)
checkfilex("%s/file_JJR.dat" % datadir)
checkfilex("%s/file_JJS.dat" % datadir)
checkfilex("%s/file_LS.dat" % datadir)
checkfilex("%s/file_MD.dat" % datadir)
checkfilex("%s/file_NN.dat" % datadir)
checkfilex("%s/file_NNP.dat" % datadir)
checkfilex("%s/file_NNPS.dat" % datadir)
checkfilex("%s/file_NNS.dat" % datadir)
checkfilex("%s/file_PDT.dat" % datadir)
checkfilex("%s/file_POS.dat" % datadir)
checkfilex("%s/file_PRP.dat" % datadir)
checkfilex("%s/file_PRP$.dat" % datadir)
checkfilex("%s/file_RB.dat" % datadir)
checkfilex("%s/file_RBR.dat" % datadir)
checkfilex("%s/file_RBS.dat" % datadir)
checkfilex("%s/file_RP.dat" % datadir)
checkfilex("%s/file_SYM.dat" % datadir)
checkfilex("%s/file_TO.dat" % datadir)
checkfilex("%s/file_UH.dat" % datadir)
checkfilex("%s/file_VB.dat" % datadir)
checkfilex("%s/file_VBD.dat" % datadir)
checkfilex("%s/file_VBG.dat" % datadir)
checkfilex("%s/file_VBN.dat" % datadir)
checkfilex("%s/file_VBP.dat" % datadir)
checkfilex("%s/file_VBZ.dat" % datadir)
checkfilex("%s/file_WDT.dat" % datadir)
checkfilex("%s/file_WP.dat" % datadir)
checkfilex("%s/file_WP$.dat" % datadir)
checkfilex("%s/file_WRB.dat" % datadir)

fixsent = ""
# Until I figure out how to make use of loops like the on below, I will have to brute force things.

for mf in ['CC', 'CD', 'DT', 'EX', 'IN', 'JJ', 'JJR', 'JJS', 'LS', 'MD', 'NN', 'NNP', 'NNPS', 'NNS', 'PDT', 'POS', 'PRP', 'PRP$', 'RB', 'RBR', 'RBS', 'RP', 'SYM', 'TO', 'UH', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$', 'WRB']:
	#print "opening file: ", 'file_'+mf
	#print "hi"
	xn = 1
	# I can't get this to work right for me.
	# hence I open and close repeatedly in the loops further below
	# file = open('myfile.dat', 'a+')
	# f = open('%s.csv' % name, 'wb')
	#locals()[ "f%02d" % i ] = open( "file%02d.txt" % i )
	# locals()[ "%s/file_%s.dat" % (datadir,mf) ] = open('%s/file_%s.dat' % (datadir, mf), 'a+')

# open created data files one by one
mf_cc = open('%s/file_CC.dat' % datadir, 'r')
mf_cd = open('%s/file_CD.dat' % datadir, 'r')
mf_dt = open('%s/file_DT.dat' % datadir, 'r')
mf_ex = open('%s/file_EX.dat' % datadir, 'r')
mf_in = open('%s/file_IN.dat' % datadir, 'r')
mf_jj = open('%s/file_JJ.dat' % datadir, 'r')
mf_jjr = open('%s/file_JJR.dat' % datadir, 'r')
mf_jjs = open('%s/file_JJS.dat' % datadir, 'r')
mf_ls = open('%s/file_LS.dat' % datadir, 'r')
mf_md = open('%s/file_MD.dat' % datadir, 'r')
mf_nn = open('%s/file_NN.dat' % datadir, 'r')
mf_nnp = open('%s/file_NNP.dat' % datadir, 'r')
mf_nnps = open('%s/file_NNPS.dat' % datadir, 'r')
mf_nns = open('%s/file_NNS.dat' % datadir, 'r')
mf_none = open('%s/file_-NONE-.dat' % datadir, 'r')
mf_pdt = open('%s/file_PDT.dat' % datadir, 'r')
mf_pos = open('%s/file_POS.dat' % datadir, 'r')
mf_prp = open('%s/file_PRP.dat' % datadir, 'r')
mf_prpdol = open('%s/file_PRP$.dat' % datadir, 'r')
mf_rb = open('%s/file_RB.dat' % datadir, 'r')
mf_rbr = open('%s/file_RBR.dat' % datadir, 'r')
mf_rbs = open('%s/file_RBS.dat' % datadir, 'r')
mf_rp = open('%s/file_RP.dat' % datadir, 'r')
mf_sym = open('%s/file_SYM.dat' % datadir, 'r')
mf_to = open('%s/file_TO.dat' % datadir, 'r')
mf_uh = open('%s/file_UH.dat' % datadir, 'r')
mf_vb = open('%s/file_VB.dat' % datadir, 'r')
mf_vbd = open('%s/file_VBD.dat' % datadir, 'r')
mf_vbg = open('%s/file_VBG.dat' % datadir, 'r')
mf_vbn = open('%s/file_VBN.dat' % datadir, 'r')
mf_vbp = open('%s/file_VBP.dat' % datadir, 'r')
mf_vbz = open('%s/file_VBZ.dat' % datadir, 'r')
mf_wdt = open('%s/file_WDT.dat' % datadir, 'r')
mf_wp = open('%s/file_WP.dat' % datadir, 'r')
mf_wpdol = open('%s/file_WP$.dat' % datadir, 'r')
mf_wrb = open('%s/file_WRB.dat' % datadir, 'r')

# read in data arrays from files just opened  
pscc = mf_cc.readlines()
if TESTING: print "read in %i CC words." % len(pscc)
pscd = mf_cd.readlines()
if TESTING: print "read in %i CD words." % len(pscd)
psdt = mf_dt.readlines()
if TESTING: print "read in %i DT words." % len(psdt)
psex = mf_ex.readlines()
if TESTING: print "read in %i EX words." % len(psex)
psin = mf_in.readlines()
if TESTING: print "read in %i IN words." % len(psin)
psjj = mf_jj.readlines()
if TESTING: print "read in %i JJ words." % len(psjj)
psjjr = mf_jjr.readlines()
if TESTING: print "read in %i JJR words." % len(psjjr)
psjjs = mf_jjs.readlines()
if TESTING: print "read in %i JJS words." % len(psjjs)
psls = mf_ls.readlines()
if TESTING: print "read in %i LS words." % len(psls)
psmd = mf_md.readlines()
if TESTING: print "read in %i MD words." % len(psmd)
psnn = mf_nn.readlines()
if TESTING: print "read in %i NN words." % len(psnn)
psnnp = mf_nnp.readlines()
if TESTING: print "read in %i NNP words." % len(psnnp)
psnnps = mf_nnps.readlines()
if TESTING: print "read in %i NNPS words." % len(psnnps)
psnns = mf_nns.readlines()
if TESTING: print "read in %i NNS words." % len(psnns)
psnone = mf_none.readlines()
if TESTING: print "read in %i -NONE- words." % len(psnone)
pspdt = mf_pdt.readlines()
if TESTING: print "read in %i PDT words." % len(pspdt)
pspos = mf_pos.readlines()
if TESTING: print "read in %i POS words." % len(pspos)
psprp = mf_prp.readlines()
if TESTING: print "read in %i PRP words." % len(psprp)
psprpdol = mf_prpdol.readlines()
if TESTING: print "read in %i PRP$ words." % len(psprpdol)
psrb = mf_rb.readlines()
if TESTING: print "read in %i RB words." % len(psrb)
psrbr = mf_rbr.readlines()
if TESTING: print "read in %i RBR words." % len(psrbr)
psrbs = mf_rbs.readlines()
if TESTING: print "read in %i RBS words." % len(psrbs)
psrp = mf_rp.readlines()
if TESTING: print "read in %i RP words." % len(psrp)
pssym = mf_sym.readlines()
if TESTING: print "read in %i SYM words." % len(pssym)
psto = mf_to.readlines()
if TESTING: print "read in %i TO words." % len(psto)
psuh = mf_uh.readlines()
if TESTING: print "read in %i UH words." % len(psuh)
psvb = mf_vb.readlines()
if TESTING: print "read in %i VB words." % len(psvb)
psvbd = mf_vbd.readlines()
if TESTING: print "read in %i VBD words." % len(psvbd)
psvbg = mf_vbg.readlines()
if TESTING: print "read in %i VBG words." % len(psvbg)
psvbn = mf_vbn.readlines()
if TESTING: print "read in %i VBN words." % len(psvbn)
psvbp = mf_vbp.readlines()
if TESTING: print "read in %i VBP words." % len(psvbp)
psvbz = mf_vbz.readlines()
if TESTING: print "read in %i VBZ words." % len(psvbz)
pswdt = mf_wdt.readlines()
if TESTING: print "read in %i WDT words." % len(pswdt)
pswp = mf_wp.readlines()
if TESTING: print "read in %i WP words." % len(pswp)
pswpdol = mf_wpdol.readlines()
if TESTING: print "read in %i WP$ words." % len(pswpdol)
pswrb = mf_wrb.readlines()
if TESTING: print "read in %i WRB words." % len(pswrb)

# open sentence structure file
mf_sent_stru = open('%s/file_sentstru.dat' % datadir, 'r')
pssentstru = mf_sent_stru.readlines()
if TESTING: print "read in %i sentence structures." % len(pssentstru)



#while True:
#	thissentence = writeSentence("")
#	print "===================================================="
#	print thissentence

for x in range(0,totsenti):
	thissentence = writeSentence("")
	print "===================================================="
	print thissentence


#rfile.close()
mf_sent_stru.close()
# ftagged.close()
# close created data files one by one
mf_cc.close()
mf_cd.close()
mf_dt.close()
mf_ex.close()
mf_in.close()
mf_jj.close()
mf_jjr.close()
mf_jjs.close()
mf_ls.close()
mf_md.close()
mf_nn.close()
mf_nnp.close()
mf_nnps.close()
mf_nns.close()
mf_pdt.close()
mf_pos.close()
mf_prp.close()
mf_prpdol.close()
mf_rb.close()
mf_rbr.close()
mf_rbs.close()
mf_rp.close()
mf_sym.close()
mf_to.close()
mf_uh.close()
mf_vb.close()
mf_vbd.close()
mf_vbg.close()
mf_vbn.close()
mf_vbp.close()
mf_vbz.close()
mf_wdt.close()
mf_wp.close()
mf_wpdol.close()
mf_wrb.close()
