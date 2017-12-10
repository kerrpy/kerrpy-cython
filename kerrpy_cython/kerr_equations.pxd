#cython: language_level=3, boundscheck=False,cdivision=True


################################################
##                C FUNCTIONS                 ##
################################################

# This functios will be (hopefully) compliled in pure C and they will not have any Python overhead
# of any kind. This means that all the loops and math operations are free of the python-lag.

# ¡IMPORTANT!
# Please, check using cython -a {this_file_name}.pyx that these functions do not have python-related code,
# which is indicated by yellow lines in the html output.
cdef void KerrGeodesicEquations(double* y, double* f,double* data) nogil
