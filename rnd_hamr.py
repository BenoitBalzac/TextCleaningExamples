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
#   fyle1p="fyle1p"
#   fyle2p="fyle2p"
   if os.path.isfile(fyle1) and os.path.isfile(fyle2):
      cmd="sed -e '1,5d' "+fyle1+">fyle1p.dat"
      os.popen(cmd,'w',1)
      cmd="sed -e '1,5d' "+fyle2+">fyle2p.dat"
      os.popen(cmd,'w',1)

      cmd=" awk '{a=$6;getline<f;$6-=a}1'> wannier_90_dhr_noh.dat f=fyle1p.dat fyle2p.dat"
      os.popen(cmd,'w',1)
   else: print("files not present!");exit() 

   num_vun=int(input("How many orbitals in your Wannier window?:    "))
   fresh=float(input("How small is ignorable for overlap?:   "))



   dHr={(1,0,0) : [], # Be careful if Hermitian
      (-1,0,0) : [],
      (0,1,0) :  [],
      (0,-1,0) : [],
      (0,0,0) :  [],
      (0,0,1) :  [],
      (0,0,-1) : []}
   for c in range(num_vun):
      dHr[(1,0,0)].append([])
      dHr[(-1,0,0)].append([])
      dHr[(0,1,0)].append([])
      dHr[(0,-1,0)].append([])
      dHr[(0,0,0)].append([])
      dHr[(0,0,1)].append([])
      dHr[(0,0,-1)].append([])

   print(dHr)
   trackxp=0
   trackxm=0
   trackyp=0
   trackym=0
   tracknaw=0
   trackzp=0
   trackzm=0

   red=0
   indr=[]


   if os.path.exists('wannier_90_dhr_noh.dat'):
      fee=open('wannier_90_dhr_noh.dat','r').readlines()[1:]
      for i,line in enumerate(fee): 
         if i==0:
            if int(fee[i].split()[0])==1 and int(fee[i].split()[1])==0 and int(fee[i].split()[2])==0:
               for j in range(num_vun):
                  print(trackxp)
                  dHr[(1,0,0)][trackxp].append(float(fee[i+j].split()[5]))
               trackxp+=1
               i+=num_vun
         else:
            if int(fee[i].split()[0])==1 and int(fee[i].split()[1])==0 and int(fee[i].split()[2])==0 and (int(fee[i].split()[4])!=int(fee[i-1].split()[4])):
               for j in range(num_vun):
                  dHr[(1,0,0)][trackxp].append(float(fee[i+j].split()[5]))
               trackxp+=1
            if int(fee[i].split()[0])==-1 and int(fee[i].split()[1])==0 and int(fee[i].split()[2])==0 and (int(fee[i].split()[4])!=int(fee[i-1].split()[4])):
               for j in range(num_vun):
                  dHr[(-1,0,0)][trackxm].append(float(fee[i+j].split()[5]))
               trackxm+=1
            if int(fee[i].split()[0])==0 and int(fee[i].split()[1])==1 and int(fee[i].split()[2])==0 and (int(fee[i].split()[4])!=int(fee[i-1].split()[4])):
               for j in range(num_vun):
                  dHr[(0,1,0)][trackyp].append(float(fee[i+j].split()[5]))
               trackyp+=1
            if int(fee[i].split()[0])==0 and int(fee[i].split()[1])==-1 and int(fee[i].split()[2])==0 and (int(fee[i].split()[4])!=int(fee[i-1].split()[4])):
               for j in range(num_vun):
                  dHr[(0,-1,0)][trackym].append(float(fee[i+j].split()[5]))
               trackym+=1
            if int(fee[i].split()[0])==0 and int(fee[i].split()[1])==0 and int(fee[i].split()[2])==0 and (int(fee[i].split()[4])!=int(fee[i-1].split()[4])):
               for j in range(num_vun):
                  dHr[(0,0,0)][tracknaw].append(float(fee[i+j].split()[5]))
               tracknaw+=1
            if int(fee[i].split()[0])==0 and int(fee[i].split()[1])==0 and int(fee[i].split()[2])==1 and (int(fee[i].split()[4])!=int(fee[i-1].split()[4])):
               for j in range(num_vun):
                  dHr[(0,0,1)][trackzp].append(float(fee[i+j].split()[5]))
               trackzp+=1
            if int(fee[i].split()[0])==0 and int(fee[i].split()[1])==0 and int(fee[i].split()[2])==-1 and (int(fee[i].split()[4])!=int(fee[i-1].split()[4])):
               for j in range(num_vun):
                  dHr[(0,0,-1)][trackzm].append(float(fee[i+j].split()[5]))
               trackzm+=1


   print(tracknaw)
   print (dHr)
   indy=[]
   for i in range(1,num_vun+1): 
      indy.append(i)
   print(indy) 
   for x in range(num_vun):
      red=0
      for y in range(num_vun):
         if abs(dHr[(0,0,0)][x][y])<fresh:
            red+=1
         if red==(num_vun-1):
            indr.append(x)


   print(indr)  
   ghost=list(indr)
   print(ghost)
   for el in range(len(indr)):
      del indy[indr[el]]
      indr[:]=[x-1 for x in indr]
   for key in dHr.keys():
      print(shape(dHr[key]))
      indr=list(ghost)
      for i in range(len(indr)):
         holder=indr[i]
         print(holder)
         dHr[key].pop(holder)
         indr[:]=[x-1 for x in indr]


      indr=list(ghost)
      print(indr)
      print(ghost)

      for j in range(len(dHr[key])):
         for k in range(len(indr)):
           holden=indr[k]
           print(holden)
           dHr[key][j].pop(holden)
           indr[:]=[x-1 for x in indr]
         indr=list(ghost)
      indr=list(ghost)
   print(dHr)      
 
   print(num_vun)
   nrpts=len(dHr.keys())
   num_red=len(indy)
   print(num_red)

   fi=open('wannier90_dhr.dat','w')
   print('written on'+str(now()),file=fi) 
   print('%10d' %(num_red),file=fi)
   print('%10d' %(nrpts),file=fi)
   for i in range(nrpts): print('%5d' %(1),end="",file=fi)
   print( '',file=fi)
   for key in dHr.keys():
      for i in range(1,num_red+1):
         for j in range(1,num_red+1):
            print( '%5d  %5d  %5d  %5d  %5d%15.8f %15.8f' %(key[0],key[1],key[2],indy[j-1],indy[i-1],dHr[key][j-1][i-1].real,dHr[key][j-1][i-1].imag),file=fi)
            print( '',file=fi)
   fi.close()
 
