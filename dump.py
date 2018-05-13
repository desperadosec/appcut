import idaapi
import os.path

# TODO: Automagically create header file with calling convention, etc.

PATH = "f:\\temp"

def getFunctionEa(funcname):
    # Returns the EA of a function given the name (as IDA sees it)
    for f in Functions():
        if GetFunctionName(f) == funcname:
            print GetFunctionName(f)
            return f
    raise Exception("Function not found!")

def dumpFunc(funcname,restype=None,args=[]):
    # Find the function with funcname in the IDA database
    # Dump the raw bytes to a file named <funcname>.<restype>.<arg1type>.<arg2type>.funcblob
    funcstart = getFunctionEa(funcname)
    funcend = FindFuncEnd(funcstart)
    functionbytes = idaapi.get_many_bytes(funcstart, funcend-funcstart)

    outfilename = os.path.join(PATH, "%s.%s." % (funcname, restype) + ".".join(args) + ".funcblob")
    f = open(outfilename,"wb")
    f.write(functionbytes)
    f.close()

dumpFunc("AddOne", "c_int", ["c_int"])
