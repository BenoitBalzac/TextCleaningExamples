# TextCleaningExamples


These are some scripts I wrote in Python to post-process text file outputs from Wannier90 and VASP quantum chemistry packages. 

rnwHamr.py- This is to post-process the hr.dat file, the real-space overlap between wannier orbitals. This is used to construct
the tight-binding model, that is atomic approximation, of the solid using only nearest neighbor k-points

rndHamr.py- this takes the difference between Hr.dat files. For example, from one geometry to another slightly perturbed one.
There will soon be a new prompt and loop to get rid of orbitals that are virtually unaffected by perturbations in a given
direction. This can speed up Hamiltonian calculations and be modified to quantify marginal differences in energy-scales,
and hopefully next-nearest-neighbors one day

