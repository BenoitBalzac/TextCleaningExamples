# TextCleaningExamples


These are some scripts I wrote in Python to post-process text file outputs from Wannier90 and VASP quantum chemistry packages. 

co_eff_phon.py - This script will extract from 'OUTCAR' file outputted from VASP package, the DFPT (IBRION=7) changes in eigenvalues per cartersian displacement, and recombine them according to the Raman eigenmodes to yield the energetic change per band attributed to that Raman mode.

rnwHamr.py- This is to post-process the hr.dat files, the real-space overlap between wannier orbitals. This is used to 
construct
the tight-binding model, that is atomic approximation, of the solid using only nearest neighbor k-points

rndHamr.py- this takes the difference between Hr.dat files. For example, from one geometry to another slightly perturbed one.
There is now a prompt and loop to get rid of orbitals that are virtually unaffected by perturbations in a given
direction, choosing the sub-space appropriate for tight-binding like calculation. This yield the low-energy model Hamiltonian and quantify marginal differences in energy-scales. Next-nearest-neighbors version soon and full integration with rnwHamr.py maybe in the future...

WannProfiler.py - This script can output gnuplot files to show the Bloch wavefunction composition in a given energy window 
(The NBANDS index) for a given Wannier function. Will add user prompt flexibility soon, curren version only does first d1 
orbital

E_pt_by_pt.py - Just a simple script to extract total Kohn-Sham energies, k-point, and band index for post-processing with awk later (finite-difference). Will update such that files can be prompted to be renamed, then subtracted with the awk commands via Python os module.
