#!/usr/bin/env python

import os
import jpg
from tree import *

def load(dossier_in) :
	Image = []
	i = 1
	liste = os.listdir(dossier_in)
	liste.sort()
	
	for file in liste:
		print file
		Image.append(jpg.Ima(dossier_in + "/" + file, i))
		i += 1
		
	
	for j in xrange(0, Image[0].getHeight()) :
			for i in xrange(0, Image[0].getWidth()) :
				treeSet = TreeSet(80, 3, 255, 8)
				for im in Image : 
					s = Sample(im.getSample((i,j)), im.getFrame())
					treeSet.insertSample(s)
		
				for im in Image :
					s = Sample(im.getSample((i,j)), im.getFrame())
					im.setBG((i,j), treeSet.isSampleBG2(s,40))
					#print treeSet.isSampleBG(s) , " " , im.getFrame()
					
					#print "----"
			print j	
	
	for im in Image :
		im.save("out", 0.80, True)
		
	


def main():
	dossier_in = "in"
	dossier_out = "out"
	os.system("mkdir out")
	load(dossier_in)
	return 0

if __name__ == '__main__': 
	main()
