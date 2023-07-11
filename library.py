# using custom_library module 
import sys

from custom_library import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])