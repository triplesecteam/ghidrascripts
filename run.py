import subprocess
headlessanalyzer_path = "/workspaces/tutorial1/ghidra_11.0_PUBLIC/support/analyzeHeadless"
project_directory_path = "/workspaces/tutorial1/temp/"
binaryPath = "/workspaces/tutorial1/CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_01.out"
binaryname = "CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_01.out"
function_name = "CWE121_Stack_Based_Buffer_Overflow__char_type_overrun_memcpy_01_bad"
command = [headlessanalyzer_path, project_directory_path, binaryname ,  '-deleteProject', '-import', binaryPath, '-postscript', 'ghidrascript.py', f"{function_name}" ]
subprocess.run(command, check=True)
