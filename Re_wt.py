import os, time, subprocess

if __name__=='__main__':
   trigger=str(raw_input("Which deg. of fredom do you want from OUTCAR?\n (Please mind your whitespace and if mode is imaginary):"))

   count_me = int(raw_input("How many atoms are there:"))

   trig1='band No.'
   bands= int(raw_input("how many bands are there:"))
   dof = 1

   xwt=0.
   ywt=0.
   zwt=0.
   

   begin=10**10
   kpt=1
   
   if os.path.exists('OUTCAR'):
      lines=open('OUTCAR','r').readlines()[1:]
      for i, line in enumerate(lines):
         if trigger in lines[i]:
            print('hello darkness my old friend')
            begin=i
            for el in range(i+2,i+2+count_me):
               xwt=float(lines[el].split()[3])
               tmp_nome=str('deltEps_%s.deig' %str(dof))
               cmd="awk '{print $1, $2, $3*(%f)}' " %(xwt)+tmp_nome+" > deltEps_%s_primo.deig" %str(dof)
               tmp_nome=str('deltEps_%s.deig' %str(dof))
               print os.popen(cmd).read()
               print(xwt) 
               dof+=1
               ywt=float(lines[el].split()[4])
               tmp_nome=str('deltEps_%s.deig' %str(dof))
               cmd="awk '{print $1, $2, $3*(%f)}' " %(ywt)+tmp_nome+" > deltEps_%s_primo.deig" %str(dof)
               print os.popen(cmd).read()
               dof+=1
               print(ywt)
               zwt=float(lines[el].split()[5])
               tmp_nome=str('deltEps_%s.deig' %str(dof))
               cmd="awk '{print $1, $2, $3*(%f)}' " %(zwt)+tmp_nome+" > deltEps_%s_primo.deig" %str(dof)
               print os.popen(cmd).read()
               dof+=1
               print(zwt)
