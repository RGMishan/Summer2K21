#! /usr/bin/python3

import cgi
import subprocess
import time

print("content-type: text/html")
print()

# taking input from field in HTML
field = cgi.FieldStorage()
cmd = field.getvalue("x")

# passing command in process and using sudo

output = subprocess.getoutput("sudo " + cmd)
print(output)
