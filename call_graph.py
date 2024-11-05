
from ghidra.util.task import TaskMonitor
import networkx as nx
def create_call_graph():
    cg = nx.DiGraph()
    fm = getCurrentProgram().getFunctionManager()
    functions = fm.getFunctions(True)
    for func in functions:
        func_name = func.getName()
        
        callees = find_callee_func(func)
        cg.add_node(func_name)
        for f in callees:
            callee_name = f.getName()
            cg.add_node(callee_name)
            cg.add_edge(func_name, callee_name)
    return cg

def find_callee_func( caller_func):
    monitor = TaskMonitor.DUMMY
    callees = caller_func.getCalledFunctions(monitor)
    return callees





if __name__ == "__main__":
    
    call_g = create_call_graph()
    print(call_g.edges())
        
        
        
