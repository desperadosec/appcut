from ctypes import *
import sys

# TODO: allow the user to go through files, and get function pointers back by offset/ordinal
#           while defining prototypes as necessary

#       - Maybe move this to another file as well
#lib = WinDLL("dumped.exe")
#unexported_funcs = {"datemath": {"offset": 0x4FD1, "prototype":CFUNCTYPE(c_int, c_int, c_int, c_int)}}
#BASE = lib._handle

#kernel32 = windll.kernel32
"""
for func in unexported_funcs.keys():
    funcoffset = unexported_funcs[func]["offset"]
    funcptr = unexported_funcs[func]["prototype"](BASE+funcoffset)
    setattr(lib, func, funcptr)
"""

if __name__ == "__main__":
    if len(sys.argv) == 2:
        libname = sys.argv[1]
        print libname
        try: 
            import func
            func.LdLibrary(libname)
        except Exception as e:
            pass

    else:
        print "Usage: python unex.py (DLL Name to load)"

    import code
    code.interact(local=locals())

    # Load DLL into memory space

#addr = kernel32.GetProcAddress(kernel32._handle, "Sleep")
#print hex(kernel32._handle)
#print hex(addr)
#print hex(addr-kernel32._handle)

#addr = kernel32.GetProcAddress(kernel32._handle, "GetModuleHandleA")
#proto = WINFUNCTYPE(c_int, c_char_p)
#func = proto(addr)
#print hex(func("dumped.exe"))

# Base address of loaded exe
#print hex(exe._handle)


