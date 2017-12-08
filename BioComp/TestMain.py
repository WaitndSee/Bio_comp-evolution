import numpy as np
import os
import time


print "Hello world!"

nbgenes = 10

Transcript = []
Genome = []
Range = (0,0)
for i in range(nbgenes):
  Transcript.append(0)
  Genome.append((0,0))
  
def load_res():
  global Transcript
  f = open("EnregistrementTranscrits.txt","r")
  lignes = f.readlines()
  f.close()
  for i in range(len(lignes)):
     Transcript[i] = int(lignes[i].split(" ")[2].split("\n")[0])
  

def load_genome(directoryAddress):
  global Genome,Range
  f = open(directoryAddress+'tousgenesidentiques.gff','r')
  lignes = f.readlines()
  f.close()
  for i in range(5,len(lignes)):
    l = lignes[i].split("\t")
    Genome[i-5] = (int(l[3]),int(l[4]))
  ligneRange = lignes[4].split("\t")
  Range = (ligneRange[3],ligneRange[4])


load_res()
load_genome("tousgenesidentiques/")

print Transcript
print Genome
print Range

#~ def load_resultats_sym()


#~ def Metropolis (params)
  
  #~ A = 0 # Note that this line is useless
  



#~ def zyup(pos_1,pos_2)
