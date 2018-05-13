#import idaapi
import ctypes
import ctypes.wintypes

# TODO: Automagically create header file with calling convention, etc.
# TODO: Will need to do this in a smarter way for calls to linked libraries, etc.

PAGE_EXECUTE_READ = 0x20
PAGE_EXECUTE_READWRITE = 0x40

def getFunctionEa(funcname):
    # Returns the EA of a function given the name (as IDA sees it)
    for f in Functions():
        if GetFunctionName(f) == funcname:
            print GetFunctionName(f)
            return f
    raise Exception("Function not found!")

def dumpFunc(funcname):
    # Given the name of a function, dump its opcodes to disk as a raw file
    # The function does not have to be exported, just labeled in the IDA DB
	# FIXME: This will only work for functions that do not call out anywhere
	# 	i.e. shared library, or jmp/call anywhere outside the function itself
    funcstart = getFunctionEa(funcname)
    funcend = FindFuncEnd(funcstart)
    functionbytes = idaapi.get_many_bytes(funcstart, funcend-funcstart)

    prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
    self.prot_ref = prototype
    AddOne = prototype(funcaddress)
    #print type(AddOne)
    res = ctypes.c_int(0)
    res = AddOne(ctypes.c_int(43))
    f = open("f:\\temp\\%s.funcblob" % funcname,"wb")
    f.write(functionbytes)
    f.close()

def funcFromFile(filename="f:\\temp\\AddOne.funcblob"):
    blob = open(filename,'rb').read()
    a = ctypes.create_string_buffer(blob)
    funcaddress = ctypes.addressof(a)
    print hex(funcaddress)

    prototype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
    #self.prot_ref = prototype
    #ctypes.windll.kernel32.VirtualProtect

    # cannot use c_void_p as return value of functions :-(
    PTR = ctypes.POINTER(ctypes.c_char)

    VirtualProtect = ctypes.windll.kernel32.VirtualProtect
    VirtualProtect.argtypes = [PTR, ctypes.c_size_t, ctypes.wintypes.DWORD, ctypes.POINTER(ctypes.wintypes.DWORD)]
    VirtualProtect.restype = ctypes.c_bool
    old = ctypes.wintypes.DWORD()
    # Do lengths match??
    VirtualProtect(ctypes.cast(funcaddress, PTR), ctypes.c_size_t(1024), ctypes.wintypes.DWORD(PAGE_EXECUTE_READWRITE), ctypes.byref(old))

    AddOne = prototype(funcaddress)
    res = ctypes.c_int(0)
    res = AddOne(ctypes.c_int(43))
    print res

# prototype = CFUNCTYPE(ctypes.c_int)
#dumpFunc("DateMath")
#dumpFunc("AddOne")
funcFromFile()
# Appcall.proto("AddOne","int __cdecl AddOne(int);")
# Appcut("AddOne", "int", "
# AppCut()

