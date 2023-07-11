#command line assignment using sys and argv variable 
import sys
                      # Method 1
# try:
#     print(" Hello, welcome again to ", sys.argv[1])
# except IndexError:
#     print("Too few arguments")

                      #Method 2
if len(sys.argv) < 2:
    sys.exit("too few arguments ")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments ")

print("Welcome to ", sys.argv[1])