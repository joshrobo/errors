#!/usr/bin/env python

# This script raises an error based on 
# user-supplied command line argument

import sys
import argparse

available_errors = ["assertion","io","import","index","key","name", "os","type", "value", "zerodivision"]
parser = argparse.ArgumentParser()
parser.add_argument("error_type",choices = available_errors)
args = parser.parse_args()
error_type= args.error_type

if error_type == "assertion":
    raise AssertionError
elif error_type == "io":
    raise IOError
elif error_type == "import":
    raise ImportError
elif error_type == "index":
    raise IndexError
elif error_type == "key":
    raise KeyError
elif error_type == "name":
    raise NameError
elif error_type == "os":
    raise OSError
elif error_type == "type":
    raise TypeError
elif error_type == "value":
    raise ValueError
elif error_type == "zerodivision":
    raise ZeroDivisionError
else:
    sys.stderr.write("Sorry, not able to throw a(n) ")
    sys.stderr.write(error_type + " error\n")
    print_usage()
