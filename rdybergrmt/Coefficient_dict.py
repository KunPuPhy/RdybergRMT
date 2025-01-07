"""
Coefficient_dict
================
Used to determine the coefficient of the corresponding hopping or interaction term.

Provides
> Field_coefficient_dict
> Interaction_coefficient_dict

"""
import numpy as np
from .Hopping_list import *

__all__ = ["Field_coefficient_dict", "Interaction_coefficient_dict"]


class Field_coefficient_dict(object):
    """

    Field_coefficient_dict
    ----------------------
    > constant term e.g. h_x \sum_{Pos_i} S^{Pos_i}_x
    > quasiperiodic term e.g. V*cos(2\pi*\alpha*Pos_i + \delta) \sum_{Pos_i} S^{Pos_i}_x
    > constant + quasiperiodic term e.g. (h_x + V*cos(2\pi*\alpha*Pos_i + \delta)) \sum_{Pos_i} S^{Pos_i}_x

    Parameters
    ----------
    L : length of lattice; type : int.
    h : strength of the field; type : float.
    alpha : Wave number to determine spatial periodic distribution of the field; type : float.
    delta : phase offset; type : float.
    
    Returns
    -------
    Coefficient_dict :  type : dict
    e.g. {Site_index'i' : Coefficient, ...}

    """
    
    def __init__(self, L = None, h = None, alpha = (np.sqrt(5) - 1)/2, delta = 0):
        self.L = L
        self.h = h
        self.alpha = alpha
        self.delta = delta
        self.coefficient_dict = {}

    def get_constant_coefficient(self):
        """
        
        get the coefficient of the constant term.
        e.g. h_x \sum_{Pos_i} S^{Pos_i}_x


        Example output:
        ---------------
        {0 : h_x, 1 : h_x, 2 : h_x, ...}

        """
        for i in range(self.L):
            self.coefficient_dict[i] = self.h
        return self.coefficient_dict
    
    
    def get_quasiperiodic_coefficient(self):
        """
        
        get the coefficient of the quasiperiodic term.
        e.g. V*cos(2\pi*\alpha*Pos_i + \delta) \sum_{Pos_i} S^{Pos_i}_x

        Example output:
        ---------------
        {0 : V*cos(2\pi*\alpha*0 + \delta), 1 : V*cos(2\pi*\alpha*1 + \delta), 2 : V*cos(2\pi*\alpha*2 + \delta), ...}

        """
        for i in range(self.L):
            self.coefficient_dict[i] = self.h * np.cos(2*np.pi*self.alpha*i + self.delta)
        return self.coefficient_dict
    
    def get_constant_vs_quasiperiodic_coefficient(self):
        """
        
        get the coefficient of the constant + quasiperiodic term.
        e.g. (h_x + V*cos(2\pi*\alpha*Pos_i + \delta)) \sum_{Pos_i} S^{Pos_i}_x

        Example output:
        ---------------
        {0 : h_x + V*cos(2\pi*\alpha*0 + \delta), 1 : h_x + V*cos(2\pi*\alpha*1 + \delta), 2 : h_x + V*cos(2\pi*\alpha*2 + \delta), ...}

        """
        for i in range(self.L):
            self.coefficient_dict[i] = self.h + self.h * np.cos(2*np.pi*self.alpha*i + self.delta)
        return self.coefficient_dict




class Interaction_coefficient_dict(object):
    """

    Interaction_coefficient_list
    > constant term e.g. h_x \sum_{Pos_i} S^{Pos_i}_x S^{Pos_j}_x
    > quasiperiodic term  e.g. V*cos(2\pi*\alpha*Pos_i + \delta) \sum_{Pos_i} S^{Pos_i}_x S^{Pos_{i+1}}_x
    > constant + quasiperiodic term e.g. (h_x + V*cos(2\pi*\alpha*Pos_i + \delta)) \sum_{Pos_i} S^{Pos_i}_x S^{Pos_{i+1}}_x
    > exponential decay term e.g.  V(i - j)\sum_{Pos_i} S^{Pos_i}_x S^{Pos_j}_x


    Parameters
    ----------
    L : length of lattice; type : int.
    V : strength of the interaction; type : float.
    alpha : Wave number to determine spatial periodic distribution of the interaction; type : float.
    delta : phase offset; type : float.
    hopping_type : hopping list type; type : str.

    Returns
    -------
    Coefficient_dict :  type : dict
    e.g. {Hopping_list_index'i' : Coefficient, ...}

    """

    def __init__(self, L = None, V = None, alpha = (np.sqrt(5) - 1)/2, delta = 0,  hopping_type = None):
        Hopping_dict = {"1D_NN_OBC" : OneDimension_chain_hopping_list(L).get_hopping_list_NN_OBC,
                        "1D_NN_PBC" : OneDimension_chain_hopping_list(L).get_hopping_list_NN_PBC,
                        "1D_NNN_OBC" : OneDimension_chain_hopping_list(L).get_hopping_list_NNN_OBC,
                        "1D_NNN_PBC" : OneDimension_chain_hopping_list(L).get_hopping_list_NNN_PBC,
                        "1D_Fully_connected" : OneDimension_chain_hopping_list(L).get_hopping_list_fully_connected}

        self.L = L
        self.V = V 
        self.alpha = alpha
        self.delta = delta
        self.hopping_list = Hopping_dict[hopping_type]()
        self.coefficient_dict = {}
    
    def get_constant_coefficient(self):
        """
        
        get the coefficient of the constant term.
        e.g. h_x \sum_{Pos_i} S^{Pos_i}_x S^{Pos_{i+1}}_x

        Example output:
        ---------------
        {0 : V, 1 : V, 2 : V, ...}

        """
        for i in range(len(self.hopping_list)):
            pos_i = self.hopping_list[i][0]
            self.coefficient_dict[i] = self.V
        return self.coefficient_dict
    
    def get_quasiperiodic_coefficient(self):
        """
        
        get the coefficient of the quasiperiodic term.
        e.g. V*cos(2\pi*\alpha*Pos_i + \delta) \sum_{Pos_i} S^{Pos_i}_x S^{Pos_{i+1}}_x

        Example output:
        ---------------
        {0 : V*cos(2\pi*\alpha*0 + \delta), 1 : V*cos(2\pi*\alpha*1 + \delta), 2 : V*cos(2\pi*\alpha*2 + \delta), ...}

        """
        for i in range(len(self.hopping_list)):
            pos_i = self.hopping_list[i][0]
            self.coefficient_dict[i] = self.V * np.cos(2*np.pi*self.alpha*pos_i + self.delta)
        return self.coefficient_dict

    def get_constant_vs_quasiperiodic_coefficient(self):
        """
        
        get the coefficient of the constant + quasiperiodic term.
        e.g. (h_x + V*cos(2\pi*\alpha*Pos_i + \delta)) \sum_{Pos_i} S^{Pos_i}_x S^{Pos_{i+1}}_x

        Example output:
        ---------------
        {0 : h_x + V*cos(2\pi*\alpha*0 + \delta), 1 : h_x + V*cos(2\pi*\alpha*1 + \delta), 2 : h_x + V*cos(2\pi*\alpha*2 + \delta), ...}

        """
        for i in range(len(self.hopping_list)):
            pos_i = self.hopping_list[i][0]
            self.coefficient_dict[i] = self.V + self.V * np.cos(2*np.pi*self.alpha*pos_i + self.delta)
        return self.coefficient_dict

    def get_exponential_decay_coefficient(self):
        """
        
        get the coefficient of the exponential decay term.
        e.g.  V(i - j)\sum_{Pos_i} S^{Pos_i}_x S^{Pos_{i+1}}_x
        
        Example output:
        ---------------
        {0 : V(i - j), 1 : V(i - j), 2 : V(i - j), ...}


        """
        for i in range(len(self.hopping_list)):
            pos_i = self.hopping_list[i][0]
            pos_j = self.hopping_list[i][1]
            self.coefficient_dict[i] = self.V * (abs(pos_i - pos_j)**(-6))
        return self.coefficient_dict


if __name__ == "__main__":
    L = 3
    h = 1
    alpha = (np.sqrt(5) - 1)/2
    delta = 0
    V = 1
    hlist = "1D_NN_OBC"
    Field_coefficient = Field_coefficient_dict(L, h, alpha, delta)
    Interaction_coefficient = Interaction_coefficient_dict(L, V, hlist = "1D_NN_OBC")
    print(Field_coefficient.get_constant_coefficient())
    print(Interaction_coefficient.get_constant_coefficient())
    print(Interaction_coefficient_dict(L,V,alpha,delta,"1D_Fully_connected").get_exponential_decay_coefficient())
