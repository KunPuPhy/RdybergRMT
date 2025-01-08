"""

Lattice
=======
Familiar field hamiltonian and interaction hamiltonian in spin-1/2 system

Provides
--------
> Spin field hamiltonian
> Spin interaction hamiltonian

"""

import numpy as np
from scipy import sparse
from .Bitopeator import *
from .Hopping_list import *
from .Basis import *
from .Coefficient_dict import *


class Spin_field_hamiltonian:
    """
    
    Class for field hamiltonian of spin system.
    > Sx term
    > Sz term
    > Sy term

    Parameters
    ----------
    L : int
        The length of the lattice.
    h : float
        The field strength.
    coefficient_type : str
        The type of coefficient.

    Returns
    -------
    H : array
        The Hamiltonian matrix.

    """
    

    def __init__(self, L, h, coefficient_type = None):
        Field_coefficient = {"Constant" : Field_coefficient_dict(L, h).get_constant_coefficient, 
                         "Quasiperiodic" : Field_coefficient_dict(L, h).get_quasiperiodic_coefficient}
        
        self.L = L
        self.basis = get_spin_basis(L)
        self.hdict = Field_coefficient[coefficient_type]()


    #S_x term
    def get_Hamiltonian_Sx(self):
        '''

        get the hamiltonian matrix of x-direction field
        i.e. h_x \sum_{Pos_i} S^{Pos_i}_x term

        Example
        -------
        >>> L = 1
        >>> h = 1
        >>> H = Spin_field_hamiltonian(L, h, coefficient_type = "Constant").get_hamiltonian_Sx()
        >>> print(H) # H = Sx
        [[0. 1.]
         [1. 0.]] 

        '''
        HR = [] # Row-indexed array
        HC = [] # Column-indexed array
        HV = [] # Value-indexed array
        for j in self.basis:
            # right vector 'j' and column-indexed 'j-id'
            j_id = search_i(self.basis, j)
            for pos_i in range(self.L):
                HC.append(j_id)
                # S^{Pos_i}_x operations
                i = flip_bit(j,pos_i) 
                # left vector 'i' and Row-indexed 'i-id'
                i_id = search_i(self.basis, i)
                HR.append(i_id)
                # Matrix element H_{i_id,j_id} = h_x
                HV.append(self.hdict[pos_i])
        H = sparse.coo_matrix((HV,(HR,HC)), shape = (len(self.basis), len(self.basis))).toarray()
        return H
    
    def get_Hamiltonian_Sz(self):
        '''
        
        get the hamiltonian matrix of z-direction field
        i.e. h_z \sum_{Pos_i} S^{Pos_i}_z term

        Example
        -------
        >>> L = 1
        >>> h = 1
        >>> H = Spin_field_hamiltonian(L, h, coefficient_type = "Constant").get_Hamiltonian_Sz()
        >>> print(H) # H = Sz
        [[-1. 0.]
         [0. 1.]]

        '''
        HR = [] # Row-indexed array
        HC = [] # Column-indexed array
        HV = [] # Value-indexed array
        for j in self.basis:
            # right vector 'j' and column-indexed 'j-id'
            j_id = search_i(self.basis, j)
            coefficient = 0
            for pos_i in range(self.L):
                # S^{Pos_i}_z operations
                coefficient = coefficient + (2*read_bit(j,pos_i)-1)*self.hdict[pos_i]
            # left vector 'i' and Row-indexed 'i-id'
            i_id = j_id
            HC.append(j_id)
            HR.append(i_id)
            HV.append(coefficient)
        H = sparse.coo_matrix((HV,(HR,HC)), shape = (len(self.basis), len(self.basis))).toarray()
        return H
        
    def get_Hamiltonian_Sy(self):
        '''
        get the hamiltonian matrix of y-direction field
        i.e. h_y \sum_{Pos_i} S^{Pos_i}_y term

        Example
        -------
        >>> L = 1
        >>> h = 1
        >>> H = Spin_field_hamiltonian(L, h, coefficient_type = "Constant").get_Hamiltonian_Sy()
        >>> print(H) # H = Sy
        [[0. 0.+ 1.j]
         [0.-1.j 0.]]

        '''
        HR = [] # Row-indexed array
        HC = [] # Column-indexed array
        HV = [] # Value-indexed array
        for j in self.basis:
            # right vector 'j' and column-indexed 'j-id'
            j_id = search_i(self.basis, j)
            for pos_i in range(self.L):
                HC.append(j_id)
                # S^{Pos_i}_y operations
                i = flip_bit(j,pos_i)
                coefficent = (2*read_bit(j,pos_i)-1)*1j*self.hdict[pos_i]
                # left vector 'i' and Row-indexed 'i-id'
                i_id = search_i(self.basis, i)
                HR.append(i_id)
                # Matrix element H_{i_id,j_id} = h_x
                HV.append(coefficent)
        H = sparse.coo_matrix((HV,(HR,HC)), shape = (len(self.basis), len(self.basis))).toarray()
        return H


#===================================================================================================

class Spin_interaction_hamiltonian:
    """
    
    Class for interaction hamiltonian of spin system. 

    Parameters
    ----------
    L : int
        The length of the lattice.
    V : float
        The interaction strength.
    alpha : float
        Wave number to determine spatial periodic distribution of the field.
    delta : float
        phase offset.
    hopping_type : str
        The type of hopping.
    coefficient_type : str
        The type of coefficient.

    Returns
    -------
    H : array
        The Hamiltonian matrix.


    """
    def __init__(self, L = None, V = None, alpha = (np.sqrt(5) - 1)/2, delta = 0, hopping_type = None, coefficient_type = None):
        #
        Hopping_dict = {"1D_NN_OBC" : OneDimension_chain_hopping_list(L).get_hopping_list_NN_OBC,
                        "1D_NN_PBC" : OneDimension_chain_hopping_list(L).get_hopping_list_NN_PBC,
                        "1D_NNN_OBC" : OneDimension_chain_hopping_list(L).get_hopping_list_NNN_OBC,
                        "1D_NNN_PBC" : OneDimension_chain_hopping_list(L).get_hopping_list_NNN_PBC,
                        "1D_Fully_connected" : OneDimension_chain_hopping_list(L).get_hopping_list_fully_connected}
        #
        Interaction_coefficient = {"Constant" : Interaction_coefficient_dict(L, V, alpha = alpha, delta = delta, hopping_type = hopping_type).get_constant_coefficient, 
                         "Quasiperiodic" : Interaction_coefficient_dict(L, V, alpha = alpha, delta = delta, hopping_type = hopping_type).get_quasiperiodic_coefficient,
                         "Exponential_Decay" : Interaction_coefficient_dict(L, V, alpha = alpha, delta = delta, hopping_type = hopping_type).get_exponential_decay_coefficient}
        
        
        self.L = L
        self.V = V
        self.basis = get_spin_basis(L)
        self.hopping_list = Hopping_dict[hopping_type]()
        self.vdict = Interaction_coefficient[coefficient_type]()

    #S_xx term
    def get_Hamiltonian_Sxx(self):
        """
        
        get the hamiltonian matrix of x-direction interaction
        i.e. V_xx \sum_{Pos_i,Pos_j} S^{Pos_i}_x S^{Pos_j}_x term

        Example
        -------
        >>> L = 2
        >>> V = 1
        >>> H = Spin_interaction_hamiltonian(L, V, coefficient_type = "Constant").get_Hamiltonian_Sxx()
        >>> print(H) # H = S^{1}_x S^{2}_x
        [[0 0 0 1]
         [0 0 1 0]
         [0 1 0 0]
         [1 0 0 0]]
        
        """
        HR = []
        HC = []
        HV = []
        basis = self.basis
        hopping_list = self.hopping_list
        for j in basis:
            # right vector 'j' and column-indexed 'j-id'
            j_id = search_i(basis, j)
            for pos in range(len(hopping_list)):
                HC.append(j_id)
                # S^{Pos_i}_x S^{Pos_j}_x operations
                Pos0 = hopping_list[pos][0]
                Pos1 = hopping_list[pos][1]
                i = flip_bit(j,Pos0) 
                i = flip_bit(i,Pos1)
                # left vector 'i' and Row-indexed 'i-id'
                i_id = search_i(self.basis, i)
                HR.append(i_id)
                HV.append(self.vdict[pos])
        H = sparse.coo_matrix((HV,(HR,HC)), shape = (len(basis), len(basis))).toarray()
        return H

    #S_zz term
    def get_Hamiltonian_Szz(self):
        """
        
        get the hamiltonian matrix of z-direction interaction
        V_zz \sum_{Pos_i,Pos_j} S^{Pos_i}_z S^{Pos_j}_z term

        Example
        -------
        >>> L = 2
        >>> V = 1
        >>> H = Spin_interaction_hamiltonian(L, V, coefficient_type = "Constant").get_Hamiltonian_Szz()
        >>> print(H) # H = Szz
        [[ 1  0  0  0]
         [ 0 -1  0  0]
         [ 0  0 -1  0]
         [ 0  0  0  1]]

        """
        HR = []
        HC = []
        HV = []
        basis = self.basis
        hopping_list = self.hopping_list
        for j in basis:
            # right vector 'j' and column-indexed 'j-id'
            j_id = search_i(basis, j)
            coefficient = 0
            for pos in range(len(hopping_list)):
                Pos0 = hopping_list[pos][0]
                Pos1 = hopping_list[pos][1]
                # S^{Pos_i}_z S^{Pos_j}_z operations
                coefficient = coefficient + (2*read_bit(j,Pos0)-1)*(2*read_bit(j,Pos1)-1)*self.vdict[pos]
            # left vector 'i' and Row-indexed 'i-id'
            i_id = j_id
            print("coefficient : ", coefficient)
            print("Total : ", self.V*coefficient)
            HC.append(j_id)
            HR.append(i_id)
            HV.append(coefficient)
        H = sparse.coo_matrix((HV,(HR,HC)), shape = (len(basis), len(basis))).toarray()
        return H

    #S_yy term
    def get_Hamiltonian_Syy(self):
        """
        
        get the hamiltonian matrix of y-direction interaction
        V_yy \sum_{Pos_i,Pos_j} S^{Pos_i}_y S^{Pos_j}_y term

        Example
        -------
        >>> L = 2
        >>> V = 1
        >>> H = Spin_interaction_hamiltonian(L, V, coefficient_type = "Constant").get_Hamiltonian_Syy()
        >>> print(H) # H = Syy
        [[ 0  0  0 -1]
         [ 0  0  1  0]
         [ 0  1  0  0]
         [-1  0  0  0]]

        """
        HR = []
        HC = []
        HV = []
        basis = self.basis
        hopping_list = self.hopping_list
        for j in basis:
            # right vector 'j' and column-indexed 'j-id'
            j_id = search_i(basis, j)
            for pos in range(len(hopping_list)):
                HC.append(j_id)
                # S^{Pos_i}_y S^{Pos_j}_y operations
                Pos0 = hopping_list[pos][0]
                Pos1 = hopping_list[pos][1]
                i = flip_bit(j,Pos0) 
                i = flip_bit(i,Pos1)
                coefficient = -1*(2*read_bit(j,Pos0)-1)*(2*read_bit(j,Pos1)-1)*self.vdict[pos]
                # left vector 'i' and Row-indexed 'i-id'
                i_id = search_i(self.basis, i)
                HR.append(i_id)
                HV.append(coefficient)
        H = sparse.coo_matrix((HV,(HR,HC)), shape = (len(basis), len(basis))).toarray()
        return H



if  __name__ == "__main__":
    '''
    L = 3
    hx = 1
    H = Spin_field_hamiltonian(L, hx, clist = "Constant")
    print(H.get_hamiltonian_Sx())
    print(H.get_Hamiltonian_Sz())
    print(H.get_Hamiltonian_Sy())
    '''
    L = 2
    V = 1
    H = Spin_interaction_hamiltonian(L, V, coefficient_type = "Constant", hopping_type = "1D_NN_OBC")
    print(H.get_Hamiltonian_Sxx())
    print(H.get_Hamiltonian_Szz())
    print(H.get_Hamiltonian_Syy())
