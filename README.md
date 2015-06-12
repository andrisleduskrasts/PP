
Pieturzīmju Palīgs
==
Program code aviable in 'src' folder, PP.py contains interface, grammar module and used rules.
Sentence splitter and text loading modules can be replaced and are in seperate files "textsplitter.py" and "textload.py".

Unit and combined tests aviable in "tests" folder
Tests are sorted as WORDtest files, in which WORD means a WORD from the list of rules, for example, "bet" test is aviable in BETtest.

To use the tool, Python 3.4.3 has to be installed on your computer.

All 3 files (PP.py, textsplitter.py and textload.py) have to be located in the same folder. The default input file is set to be /tests/testin.txt , the programm will output testout.txt in the same location. To change this, open PP.py with a text editor and change the input and output files near the end of the file, as specified in the code.

The default task is to accept the input text and add commas if neccesary. This means that a sentence with correct punctuation will most likely be unchanged.
To change the task, comment the loadtext() line with a #: "#data = ..."; and uncomment the other line by removing the #: data = textload.loadtextNC to remove commas and have only the tool put them in the output.

Rule list: https://docs.google.com/document/d/1EVI_PqPjdKnTLOqalh3-Ci9aIC-tRd8VRT7OQaC3C84/edit

Andris Leduskrasts, 2015
