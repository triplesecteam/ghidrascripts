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



if __name__ == "__main__":
    args = getScriptArgs()
    if args:
        function_name = args[0]
        extract_function_info(function_name)
