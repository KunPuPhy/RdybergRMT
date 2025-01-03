"""
Basis
=====
This module contains the basis of the lattice.

"""
__all__ = ['get_spin_basis', 'search_i']

# get the idex of a basis
def search_i(basis, i):
    """
    Search the idex of 'i' in the basis.

    Parameters
    ----------
    basis : list
        The basis of the lattice.
    i : int
        The element of the basis.
    
    Return
    -------
    idex : int
        The idex of 'i' in the basis.
        Starts from 0 and left to right.

    """
    L = len(basis)
    if L == 0:
        return False
    
    idex = 0
    for temp in basis:
        if temp == i:
           break
        idex = idex + 1
        if idex >= L:
            return False
    return idex

def get_spin_basis(L):
    """
    Get the spin basis of the lattice with no symmetry.

    Parameters
    ----------
    L : int
        The length of the lattice.

    Returns
    -------
    basis : list
        The basis of the lattice.
    
    """
    basis = []
    for i in range(2**L):
        basis.append(i)
    return basis
