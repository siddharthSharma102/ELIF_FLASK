import os
from ctypes import *

file_name = "test.c"
os.system('cmd /c "cc -fPIC -shared -o  test.so test.c "')
so_file = os.getcwd() + '\\test.c'
print(so_file)
test = CDLL(so_file)

print(type(test))
print(test.main())


