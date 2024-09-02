#!/usr/bin/python3
import sys

if len(sys.argv) < 2:
    print("Usage: python script_name.py <arguments>")
    sys.exit(1)

for arg in sys.argv[1:]:
    print(arg)