
__all__ = ('NumericComputation', )


cdef class NumericComputation:

    def __cinit__(self, int a, int b):
        self.a = a
        self.b = b

    cpdef compute_sum(self):
        return self.a + self.b
