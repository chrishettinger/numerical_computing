# The system function is used to run commands
# as if they were run in the terminal.
from os import system
# Get the directory for the NumPy header files.
from numpy import get_include
# Get the directory for the Python header files.
from distutils.sysconfig import get_python_inc

# Now we construct a string for the flags we need to pass to
# the compiler in order to give it access to the proper
# header files and to allow it to link to the proper
# object files.
# Use the -I flag to include the directory containing
# the Python headers for C extensions.
# This header is needed when compiling Cython-made C files.
ic = " -I" + get_python_inc()
# Use the -I flag to include the directory for the NumPy
# headers that allow C to interface with NumPy arrays.
# This is necessary since we want the Cython file to operate
# on NumPy arrays.
npy = " -I" + get_include()
# This links to the actual object file itself
o = " ctridiag.o"

# Make a string of all these flags together.
# Add another flag that tells the compiler to make
# position independent code.
# This isn't necessary on Windows.
flags = ic + npy + o + " -fPIC"

# Build the object file from the C source code.
system("gcc ctridiag.c -c -o ctridiag.o -fPIC")
# Compile the Cython file to C code.
system("cython -a cython_ctridiag.pyx --embed")
# Compile the C code generated by Cython to an object file.
system("gcc -c cython_ctridiag.c" + flags)
# Make a Python extension containing the compiled
# object file from the Cython C code.
system("gcc -shared cython_ctridiag.o -o cython_ctridiag.so" + flags)
