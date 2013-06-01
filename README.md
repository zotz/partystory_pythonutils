partystory_pythonutils
======================

Utilities for PartyStory

I have written many versions of my little PartyStory program over 
the years. I think the first may have been in BASIC on a TRS-80 
Model I. I had one in QuickBasic, one in php3 and perhaps others.

I don't know why I keep coming back to this but I do. My latest 
effort is in Java for some reason. Perhaps to learn a bit of Java 
for work related reasons.

In any case, I came upon The Stanford Natural Language Processing Group 
and The Stanford Parser whick led me to the Stanford Log-linear 
Part-Of-Speech Tagger which then led me to:

NLTK — the Natural Language Toolkit 
http://code.google.com/p/nltk/

and hence these python utilities for what hopefully will be an improved 
PartyStory program soon.

More on that later.

The idea behind these utilities was to use a natural language parser to 
ease the creation of a robust set of data files for PartyStory to work from.

Always in the past I have been creating files of nouns, verbs, etc. and of 
coded sentence structures by hand. Let's say I had mixed results.

I thought to use the parser/tagger to read existing english texts, create 
the files of the various parts of speech and a file fo sentence structures 
for me automatically. This should make PartyStory more robust.

psauto.py is the utility that will do this. After it finishes processing 
the given text, ir calls pssortem.sh which sorts the files and removes 
duplicates.

psatest.py is a little test program that uses the sentence structures and the 
parts of speech datafiles created by psauto.py and writes random sentences 
fomr them.

I don't program daily and python is not that familiar to me. These little 
programs are very rough, lack sophistication and likely contain dumb errors.

I am putting them out in this state in the hopes that they may be useful to 
someone and also that I may find some help in improving them.

all the best from the rainy Bahamas where I was flooded last week and am 
watching the weather warily this week hoping for no repeat.

drew
