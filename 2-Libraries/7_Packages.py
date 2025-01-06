#These are mainly third party modules found at pypi.org
#Python packages are a way to organize and structure related modules into a single directory hierarchy, making it easier to manage large codebases
#pip is the package manager command for python and is used to manage packages
#pip install cowsay
import cowsay
import sys
if len(sys.argv) == 2:
    cowsay.trex("Hello , "+sys.argv[1])
 #try cowsay.cow and trex XDDD