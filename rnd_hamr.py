#!/usr/bin/env python
import os, time, subprocess
import sys
import re, glob, shutil, socket
from os.path import getsize
from scipy import *
import copy
import scipy.interpolate

def now(): return time.strftime(' at %c') #%Y:%H HH:%M MM:%S SS')

#natom=int(input("How many atoms are in your window?:"))
#norb=int(input("How many orbitals total in window?? (s:1, p:3, d:5, f:7) :"))



if __name__ == '__main__':
   fyle1=str(input("What is the final perturbed file named?:"))
   fyle2=str(input("What is the initial perturbed file named?:"))

   if os.path.isfile(fyle1) and os.path.isfile(fyle2):
      cmd="awk 'NR>4{a=$6;getline<f;$6-=a}1'> wannier_90_dhr.dat f="+fyle1+' '+fyle2
      print os.popen(cmd).read()
   else: print "files not present!";exit() 

#   fi=open('wannier90_dhr_post.dat','w')
#   print >>fi, 'written on',now()
#   print >>fi, '%10d' %(num_wann)
#   print >>fi, '%10d' %(nrpts)
#   for i in range(nrpts): print >>fi,'%5d' %(1),
#   print >>fi, ''
#   for key in dHr.keys():
#      for i in range(num_wann):
#         for j in range(num_wann):
#            print >>fi, '%5d  %5d  %5d  %5d  %5d' %(key[0],key[1],key[2],j,i),
#            print >>fi,'%15.8f %15.8f' %(dHr[key][j][i].real,dHr[key][j][i].imag),
#            print >>fi, ''
#   fi.close() 
