# TextCleaningExamples


These are some scripts I wrote in Python to post-process text file outputs from Wannier90 and VASP quantum chemistry packages. 

rnwHamr.py- This is to post-process the hr.dat file, the real-space overlap between wannier orbitals. This is used to 
construct
the tight-binding model, that is atomic approximation, of the solid using only nearest neighbor k-points

rndHamr.py- this takes the difference between Hr.dat files. For example, from one geometry to another slightly perturbed one.
There will soon be a new prompt and loop to get rid of orbitals that are virtually unaffected by perturbations in a given
direction. This can speed up Hamiltonian calculations and be modified to quantify marginal differences in energy-scales,
and hopefully next-nearest-neighbors one day

WannProfiler.py - This script can output gnuplot files to show the Bloch wavefunction composition in a given energy window 
(The NBANDS index) for a given Wannier function. Will add user prompt flexibility soon, curren version only does first d1 
orbital

oreo.py - this script strips the change in Kohn-Sham eigenvalues and changes in its occupation with respect to different 
geometries to a .dat file. This output is then passed 
to a Fortran program that calculates linear-response for strongly-correlated materials

Re-wt.py - in principle can reproduce any change in geometry with the cartesian components given by VASP's IBRION=7 routine
(the linear-response calculations)