import MDUtilities as MDU
import numpy as np
import math
import VectorMethods as VM
import VerletVelocity as Vv
from Particle3D import Particle3D as Particle3D


if len(sys.argv)!=2:
	print ("Wrong number of arguments.")
	print ("Usage: " + sys.argv[0] + " <output file>")
	quit()
else:
	outfileName = sys.argv[1]
#Open output file for writing data to
outfile = open(outfileName,"w")


file_handle = open("inFile.txt","r")

#set up the intial positions of all particles
InitialPosition = MDU.setInitialPositions(rho, particles)
