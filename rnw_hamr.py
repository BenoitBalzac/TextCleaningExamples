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

   num_vun=int(input("How many orbitals in your Wannier window?:    "))
   fresh=float(input("How small is ignorable for overlap?:   "))
   Hr={(1,0,0) : [], # Be careful if Hermitian
      (-1,0,0) : [],
      (0,1,0) :  [],
      (0,-1,0) : [],
      (0,0,0) :  [],
      (0,0,1) :  [],
      (0,0,-1) : []}


   for c in range(num_vun):
      Hr[(1,0,0)].append([])
      Hr[(-1,0,0)].append([])
      Hr[(0,1,0)].append([])
      Hr[(0,-1,0)].append([])
      Hr[(0,0,0)].append([])
      Hr[(0,0,1)].append([])
      Hr[(0,0,-1)].append([])

#   print Hr[(-1,0,0)] 
   trackxp=0
   trackxm=0
   trackyp=0
   trackym=0
   tracknaw=0
   trackzp=0
   trackzm=0
    
   red=0
   indr=[]
   
   
   if os.path.exists('wannier90_hr.dat'):
      fee=open('wannier90_hr.dat','r').readlines()[1:]
      for i,line in enumerate(fee):
         if int(fee[i].split()[0])==1 and int(fee[i].split()[1])==0 and int(fee[i].split()[2])==0 and (int(fee[i].split()[4])!=int(fee[i-1].split()[4])):
            for j in range(num_vun):
               Hr[(1,0,0)][trackxp].append(float(fee[i+j].split()[5]))
            trackxp+=1
         if int(fee[i].split()[0])==-1 and int(fee[i].split()[1])==0 and int(fee[i].split()[2])==0 and (int(fee[i].split()[4])!=int(fee[i-1].split()[4])):
            for j in range(num_vun):
               Hr[(-1,0,0)][trackxm].append(float(fee[i+j].split()[5]))
            trackxm+=1
         if int(fee[i].split()[0])==0 and int(fee[i].split()[1])==1 and int(fee[i].split()[2])==0 and (int(fee[i].split()[4])!=int(fee[i-1].split()[4])):
            for j in range(num_vun):
               Hr[(0,1,0)][trackyp].append(float(fee[i+j].split()[5]))
            trackyp+=1
         if int(fee[i].split()[0])==0 and int(fee[i].split()[1])==-1 and int(fee[i].split()[2])==0 and (int(fee[i].split()[4])!=int(fee[i-1].split()[4])):
            for j in range(num_vun):
               Hr[(0,-1,0)][trackym].append(float(fee[i+j].split()[5]))
            trackym+=1
         if int(fee[i].split()[0])==0 and int(fee[i].split()[1])==0 and int(fee[i].split()[2])==0 and (int(fee[i].split()[4])!=int(fee[i-1].split()[4])):
            for j in range(num_vun):
               Hr[(0,0,0)][tracknaw].append(float(fee[i+j].split()[5]))
            tracknaw+=1
         if int(fee[i].split()[0])==0 and int(fee[i].split()[1])==0 and int(fee[i].split()[2])==1 and (int(fee[i].split()[4])!=int(fee[i-1].split()[4])):
            for j in range(num_vun):
               Hr[(0,0,1)][trackzp].append(float(fee[i+j].split()[5]))
            trackzp+=1
         if int(fee[i].split()[0])==0 and int(fee[i].split()[1])==0 and int(fee[i].split()[2])==-1 and (int(fee[i].split()[4])!=int(fee[i-1].split()[4])):
            for j in range(num_vun):
               Hr[(0,0,-1)][trackzm].append(float(fee[i+j].split()[5]))
            trackzm+=1
   print Hr
   indy=[]
   for i in range(1,num_vun+1): 
      indy.append(i)
   print indy 
   for x in range(num_vun):
      red=0
      for y in range(num_vun):
         if abs(Hr[(0,0,0)][x][y])<fresh:
            red+=1
         if red==(num_vun-1):
            indr.append(x)

   print indr  
   ghost=list(indr)
   print ghost 
   for el in range(len(indr)):
      del indy[indr[el]]
      indr[:]=[x-1 for x in indr]
   for key in Hr.keys():
      print shape(Hr[key])
      indr=list(ghost)
      for i in range(len(indr)):
         holder=indr[i]
         print holder
         Hr[key].pop(holder)
         indr[:]=[x-1 for x in indr]


      indr=list(ghost)
      print indr
      print ghost 

      for j in range(len(Hr[key])):
         for k in range(len(indr)):
           holden=indr[k]
           print holden
           Hr[key][j].pop(holden)
           indr[:]=[x-1 for x in indr]
         indr=list(ghost)
      indr=list(ghost)
   print Hr      
 
   print num_vun
#   t2=1.4
#   t=0.56;t3=2.0-t2;tp=0.0;ed=6.6;ep=3.85
#   dt=1.0
#   Hr={(1,0,0) : [[0,t2,0],[0,0,0],[0,0,0]], # Be careful if Hermitian
#      (-1,0,0) : [[0,0,0],[t2,0,0],[0,0,0]],
#      (0,1,0) :  [[0,0,t],[0,0,0],[0,0,0]],
#      (0,-1,0) : [[0,0,0],[0,0,0],[t,0,0]],
#      (0,0,0) :  [[ed,-t3,-t],[-t3,ep,0],[-t,0,ep]]}
#   dHr={(1,0,0) : [[0,dt,0],[0,0,0],[0,0,0]], # Be careful if Hermitian
#      (-1,0,0) : [[0,0,0],[dt,0,0],[0,0,0]],
#      (0,1,0) :  [[0,0,0],[0,0,0],[0,0,0]],
#      (0,-1,0) : [[0,0,0],[0,0,0],[0,0,0]],
#      (0,0,0) :  [[0,dt,0],[dt,0,0],[0,0,0]]}
   nrpts=len(Hr.keys())
   num_red=len(indy)
   print num_red
#
   fi=open('wannier90_hr_post.dat','w')
   print >>fi, 'written on',now()  
   print >>fi, '%10d' %(num_red) 
   print >>fi, '%10d' %(nrpts)    
   for i in range(nrpts): print >>fi,'%5d' %(1),
   print >>fi, ''
   for key in Hr.keys():
      for i in range(1,num_red+1):
         for j in range(1,num_red+1):
            print >>fi, '%5d  %5d  %5d  %5d  %5d' %(key[0],key[1],key[2],indy[j-1],indy[i-1]),
            print >>fi,'%15.8f %15.8f' %(Hr[key][j-1][i-1].real,Hr[key][j-1][i-1].imag), 
            print >>fi, ''
   fi.close()
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
