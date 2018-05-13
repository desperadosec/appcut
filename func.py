import ctypes
import ctypes.wintypes

# This file contains convenience wrappers for common Windows functions
# we'll need to do some of the unexported stuff we need to.

PAGE_EXECUTE_READ = 0x20
PAGE_EXECUTE_READWRITE = 0x40

MEM_COMMIT = 0x00001000
MEM_RESERVE = 0x00002000

# cannot use c_void_p as return value of functions :-(
PTR = ctypes.POINTER(ctypes.c_char)

def VAlloc(size):
    ctypes.windll.kernel32.VirtualAlloc
    # cannot use c_void_p as return value of functions :-(

    VirtualAlloc = ctypes.windll.kernel32.VirtualAlloc
    VirtualAlloc.argtypes = [PTR, ctypes.c_size_t, ctypes.wintypes.DWORD, ctypes.wintypes.DWORD]
    VirtualAlloc.restype = ctypes.c_int
    result = ctypes.c_int(0)
    result = VirtualAlloc(None, ctypes.c_size_t(size), ctypes.wintypes.DWORD(MEM_COMMIT | MEM_RESERVE), ctypes.wintypes.DWORD(PAGE_EXECUTE_READWRITE))
    return result

def MCpy(dstaddr, srcaddr):
    memcpy = ctypes.windll.msvcrt.memcpy
    memcpy.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t]
    memcpy.restype = None
    memcpy(ctypes.c_void_p(dstaddr), ctypes.c_void_p(srcaddr))
    return

def LdLibrary(dllname):
    LoadLibrary = ctypes.windll.kernel32.LoadLibraryW
    LoadLibrary.argtypes = [ctypes.wintypes.LPCWSTR]
    LoadLibrary.restype = ctypes.wintypes.HMODULE
    print dllname
    result = LoadLibrary(dllname)
    return result

def funcFromFile(filename, args=[None]):
    # Opens function file created by dump function.
    # Filename format is: <funcname>.<return type>.<arg1type>.<arg2type>.funcblob
    # Casts arguments to the types specified in filename, then calls function
    blob = open(filename,'rb').read()
    a = ctypes.create_string_buffer(blob)
    funcaddress = ctypes.addressof(a)

    funcmem = VAlloc(ctypes.sizeof(a))#ctypes.cast(funcaddress, PTR), ctypes.c_size_t(ctypes.sizeof(a)), ctypes.wintypes.DWORD(PAGE_EXECUTE_READWRITE), ctypes.byref(old))
    
    # TODO: We should use the size of a?
    MCpy(funcmem, funcaddress, ctypes.sizeof(blob))

#funcFromFile("f:\\temp\\AddOne.funcblob",[423])

