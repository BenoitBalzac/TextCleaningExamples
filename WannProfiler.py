#!/usr/bin/env python
import os, time, subprocess
import sys
import re, glob, shutil, socket
from os.path import getsize
from scipy import *
import copy
import scipy.interpolate


if __name__== '__main__':
   ###############This is Gamma point only version- bW ##############
   bandz=int(input('How many bloch bands did you use?:'))
   wannz=int(input('How many wannier functions did you project onto?:'))
   windx=list(range(1,wannz+1))
   print(windx)
   wct=0
   if os.path.exists('wannier90.amn'):
      fee=open('wannier90.amn','r').readlines()[1:]
      print(windx[wct])
      for i,line in enumerate(fee):
         if (int(fee[i].split()[1])==windx[wct]) and (int(fee[i].split()[2])==1):
            print(i)
            print(int(fee[i].split()[1]))
            f=open('FourCompOfWann%d' %(windx[wct]),'w')
            for j in range(bandz):
               wt=float(fee[i+j].split()[3])**2+float(fee[i+j].split()[4])**2
               f.write("%.10f \n" % (wt))
            i+=bandz
            print i
            wct+=1
         if wct>=wannz:
            break
   else:
      print 'file dne!'
