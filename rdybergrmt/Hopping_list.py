"""
Hopping list
============
Used to determine where hopping or interaction occurs

Provides
--------
Functions to generate hopping list.
> OneDimension_chain_hopping_list
> TwoDimension_square_hopping_list
> TwoDimension_honeycomb_hopping_list

"""

__all__ = ['OneDimension_chain_hopping_list']

class OneDimension_chain_hopping_list:
    """
    One Dimension chain hopping list

    Parameters
    ----------
    L : type: int 
        lattice number of system

    Returns
    -------
    Hopping_list : type: 2D list; 
        list element : int

    """
    def __init__(self, L):
        self.L = L
        
    def get_hopping_list_NN_OBC(self):
        """
        get 1 Dimension hopping or spin chain nearest hopping list
        for open boundary condition.

        Example
        ------- 
        >>> L = 4
        >>> hopping_list = OneDimension_chain_hopping_list(L).get_hopping_list_N_OBC()
        >>> print(hopping_list)
        [[0, 1], [1, 2], [2, 3]]

        """
        hopping_list = []
        for j in range(self.L - 1):  
            hopping_list.append([j, (j+1)])
        return hopping_list

    def get_hopping_list_NNN_OBC(self):
        """
        get 1 Dimension hopping or spin chain next-nearest hopping list
        for open boundary condition.

        Example
        -------
        >>> L = 4
        >>> hopping_list = OneDimension_chain_hopping_list(L).get_hopping_list_NN_OBC()
        >>> print(hopping_list)
        [[0, 2], [1, 3]]

        """
        hopping_list = []
        for j in range(self.L - 2):
            hopping_list.append([j,j+2])
        return hopping_list

    def get_hopping_list_NN_PBC(self):
        """
        get 1 Dimension hopping or spin chain nearest hopping list
        for periodic boundary condition.

        Example
        -------
        >>> L = 4
        >>> hopping_list = OneDimension_chain_hopping_list(L).get_hopping_list_N_PBC()
        >>> print(hopping_list)
        [[0, 1], [1, 2], [2, 3], [3, 0]]

        Note
        -----
        In order to avoid repetition, 'L' is perferly bigger than 'L = 2'.

        """
        hopping_list = []
        for j in range(self.L):  
            hopping_list.append([j, (j+1)%self.L])
        return hopping_list


    def get_hopping_list_NNN_PBC(self):
        """
        get 1 Dimension hopping or spin chain next-nearest hopping list
        for periodic boundary condition.

        Example
        -------
        >>> L = 5
        >>> hopping_list = OneDimension_chain_hopping_list(L).get_hopping_list_NN_PBC()
        >>> print(hopping_list)
        [[0, 2], [1, 3], [2, 4], [3, 0], [4, 1]]

        Note
        -----
        In order to avoid repetition, 'L' is perferly bigger than 'L = 4'.

        """
        hopping_list = []
        for j in range(self.L):
            hopping_list.append([j, (j+2)%self.L])
        return hopping_list

    def get_hopping_list_fully_connected(self):
        """
        get 1 Dimension hopping or spin chain fully connected hopping list
        
        Example
        -------
        >>> L = 4
        >>> hopping_list = OneDimension_chain_hopping_list(L).get_hopping_list_fully_connected()
        >>> print(hopping_list)
        [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]]

        """
        hopping_list = []
        for j in range(self.L-1):
            for i in range(self.L-1):
                intob = i + j + 1    
                hopping_list.append([j, intob])
                if intob == self.L - 1:
                    break
        return hopping_list

#class TwoDimension_square_hopping_list:

#class TwoDimension_honeycomb_hopping_list:

if __name__ == '__main__':
    L = 3
    hopping_list = OneDimension_chain_hopping_list(L).get_hopping_list_N_OBC()
    print("nearest_OBC : ", hopping_list)
    hopping_list = OneDimension_chain_hopping_list(L).get_hopping_list_NN_OBC()
    print("next_nearest_OBC : ", hopping_list)
    hopping_list = OneDimension_chain_hopping_list(L).get_hopping_list_N_PBC()
    print("nearest_PBC : ", hopping_list)
    hopping_list = OneDimension_chain_hopping_list(L).get_hopping_list_NN_PBC()
    print("next_nearest_PBC : ", hopping_list)
    hopping_list = OneDimension_chain_hopping_list(L).get_hopping_list_fully_connected()
    print("Fully_connected : ", hopping_list)


