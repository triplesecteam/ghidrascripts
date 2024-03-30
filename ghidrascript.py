

from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import ConsoleTaskMonitor
def extract_binary_info():
    current_program = getCurrentProgram()
    print(type(current_program))
    print(current_program.getExecutablePath())
    print(current_program.getLanguage())
    print(type(current_program.getLanguage()))
    print(current_program.getLanguage().getProcessor())
    print(current_program.getExecutableFormat())

def extract_function_info(func_name):
    current_program = getCurrentProgram()
    fm = current_program.getFunctionManager()
    funcs = fm.getFunctions(True)
    for func in funcs:
        #print(type(func))
        if func.getName() == func_name:
            print(func.getEntryPoint())
            print(type(func.getBody()))
            print(func.getBody().getMinAddress())
            print(func.getBody().getMaxAddress())
def decompile_function(function_name):
    func_address = return_function_addr(function_name)
    current_program = getCurrentProgram()
    decomp_interface = DecompInterface()
    decomp_interface.openProgram(current_program)
    
    # Get the function at the address
    function = getFunctionAt(func_address)

    if function:
        # Decompile the function
        decomp_results = decomp_interface.decompileFunction(function, 0,ConsoleTaskMonitor())
        
        if decomp_results.decompileCompleted():
            # Get the decompiled code
            decompiled_code = decomp_results.getDecompiledFunction().getC()
            print(decompiled_code) 



def return_function_addr(func_name):
    current_program = getCurrentProgram()
    fm = current_program.getFunctionManager()
    funcs = fm.getFunctions(True)
    for func in funcs:
        #print(type(func))
        if func.getName() == func_name:
            return func.getEntryPoint()


if __name__ == "__main__":
    args = getScriptArgs()
    if args:
        function_name = args[0]
        decompile_function(function_name)
        
        
