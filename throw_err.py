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
    filename = "NON_EXIST.txt"
    with open(filename, 'r') as infile:
        infile.write("GitHub username\t%s\n" % github_username)
elif error_type == "import":
    from array import vector
elif error_type == "index":
    a = array('c', [a, b, c, d, e])
    print (a[6])
elif error_type == "key":
    raise KeyError
elif error_type == "name":
    print(donut)
elif error_type == "os":
    raise OSError
elif error_type == "tab":
print("error")
elif error_type == "type":
    cat = 2
    dog = "fish"
    print (cat + dog) 
elif error_type == "value":
    contains('team', 'i')
elif error_type == "zerodivision":
    print(1/0)
else:
    sys.stderr.write("Sorry, not able to throw a(n) ")
    sys.stderr.write(error_type + " error\n")
    print_usage()
