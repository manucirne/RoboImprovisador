from music21 import *
from random import randint
import json
from copy import deepcopy

# class NoteDur():
# 	def __init__(self,temp,w):
# 		self.temp = temp
# 		self.w = w

# DURAÇÕES:
# breve = NoteDur(4,1/5)
# minima = NoteDur(2,1/5)
# seminima = NoteDur(1,1/5)
# colcheia = NoteDur(0.5,1)
# semicolcheia = NoteDur(0.25,1/5)
#Lduration = [breve,minima,seminima,colcheia,semicolcheia]

arquivo = open("dados.json", "r")
dados = arquivo.read()
dados = json.loads(dados)

tom = "Am"
chords = ["Am", "Bm", "E7", "Am", "Dm", "G7", "C", "Bm", "Em", "Am"]
Ctemp = 4
s = stream.Stream()
s.id = 'melody'
notes = []
scaleNote = []
inicio = 0
comp = 0
print(len(dados["zero"]))

for ch in chords:
	mesureT = 0
	inicio = 0
	comp += 1
	if tom[-1] == "m":
		if "m" in ch: 
			if (ch[1] == "-") or (ch[1] == "#"):
				scaleT = scale.MinorScale(ch[0:2])
			else:
				scaleT = scale.MinorScale(ch[0]) 
		elif "7" in ch: 
			if (ch[1] == "-") or (ch[1] == "#"):
				scaleT = scale.MixolydianScale(ch[0:2])
			else:
				scaleT = scale.MixolydianScale(ch[0])
		else:
			if len(ch) > 1:
				if (ch[1] == "-") or (ch[1] == "#"):
					scaleT = scale.MajorScale(ch[0:2])
			else:
				scaleT = scale.MajorScale(ch[0])
	scalePit = scaleT.getPitches()
	for i in range(0,len(scalePit)-1):
		scaleNote.append(note.Note(scalePit[i]))
	r = note.Rest()
	r.duration.quarterLength = 1.0
	scaleNote.append(r)

	while mesureT < Ctemp:
		if inicio == 0:
			numnot = randint(0,len(scaleNote)-1)
			inicio = 2
		
		else:
			if numnot == 0:
				indice ="zero"
			elif numnot == 1:
				indice ="um"
			elif numnot == 2:
				indice ="dois"
			elif numnot == 3:
				indice ="tres"
			elif numnot == 4:
				indice ="quatro"
			elif numnot == 5:
				indice ="cinco"
			elif numnot == 6:
				indice ="seis"
			elif numnot == 7:
				indice ="sete"
			else:
				indice = "um"
			numindice = randint(0,len(dados[indice])-1)
			numnot = dados[indice][numindice]
					
		mesureT += 1
		scaleNote[numnot].duration.quarterLength = 1

		clone = deepcopy(scaleNote[numnot])

		s.append(clone)

mf = midi.translate.streamToMidiFile(s)
mf.open('imp1.mid', 'wb')
mf.write()
mf.close()
print(comp)
s.show('midi')

