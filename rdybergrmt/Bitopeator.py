"""
Bit Operator
============
Used to operate on bits of decimal base vectors

Provides
--------
> read_bit : Reads the 'n'-th bit of 'i'
> flip_bit : Flips the 'n'-th bit of 'i'
> count_bit : Counts how many 1 bits in 'i'

"""

__all__ = ['read_bit', 'flip_bit', 'count_bit']


def read_bit(i,n):
    """
    Reads the 'n'-th bit of 'i'

    Parameters
    ----------
    i : int
        input integer
    n : int
        bit index; starting from 0 and right to left; 

    Returns
    -------
    0 or 1
    
    """
    return (i&(1<<n))>>n


def flip_bit(i ,n):
    """
    Flips the 'n'-th bit of 'i'
    
    Parameters
    ----------
    i : int
        input integer
    n : int
        bit index; 

    Returns
    -------
    Fliped 'i' : int

    """
    return i^(1<<n)


def count_bit(i):
    """
    Counts how many 1 bits in 'i'
    
    Parameters
    ----------
    i : int
        input integer
    
    Returns
    -------
    Total number of 1 bits : int

    """
    return bin(i).count("1")