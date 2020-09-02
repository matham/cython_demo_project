"""Numeric
==========

"""
__all__ = ('NumericComputation', 'Numbers')


cdef class NumericComputation:
    """Computes something numerically."""

    def __cinit__(self, int a, int b):
        self.a = a
        self.b = b

    cpdef compute_sum(self):
        """Returns the sum of the input.
        """
        return self.a + self.b


cpdef enum Numbers:
    one = 1
    two = 2
"""Number list."""
