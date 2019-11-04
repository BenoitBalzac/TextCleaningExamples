import os, time, subprocess

if __name__=='__main__':
   trigger='band No.'
#   trig1='band No.'
   bands=int(raw_input("Enter number of bands: "))
   flag=0
   begin=10**10
   kpt=0
   ct=0
#   holder=None
   
   if os.path.exists('OUTCAR'):
      lines=open('OUTCAR','r').readlines()[1:]
      Dells=open('tot_Order.deig','w')
      for i, line in enumerate(lines):
         if trigger in lines[i]:
            kpt+=1
            print('hello darkness my old friend')
            ct+=1
            begin=i
            flag+=1
            for j in range(i+1,i+1+bands):
#              holder=str( lines[j])
               bandno=int(lines[j].split()[0])
               celta= float(lines[j].split()[1])
              
               Dells.write("%d        %d        %.6f\n" %(bandno,kpt,celta))
   print(ct)
   print("Rename your file for post-processing! good night, good luck")
