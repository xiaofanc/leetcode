"""
a) You have a package repository in which there are dependencies between packages for building like package A has to be built before package B. If you are given dependencies between the packages and package name x, we have find the build order for x.
Ex: A → {B,C}
B → {E}
C → {D,E,F}
D → {}
F → {}
G → {C}

For package A, build order is E B F D C A (may not unique)

Given a function Set getDependencies (Package packageName) which returns a set of dependencies for a given package name, write a method List getBuildOrder(Package packageName) which returns the build order

b) How would you handle cyclic dependencies (Algo only)
"""
