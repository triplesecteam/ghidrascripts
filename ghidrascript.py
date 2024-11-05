
from ghidra.util.task import ConsoleTaskMonitor
from ghidra.util.task import TaskMonitor
from ghidra.program.model.block import BasicBlockModel
from edu.uci.ics.jung.graph import DirectedSparseGraph
from ghidra.util.graph import Vertex
from ghidra.util.graph import Edge 
def create_cfg(function_name):
    #breakpoint()
    current_program = getCurrentProgram()
    fm = current_program.getFunctionManager()
    funcs = fm.getFunctions(True)
    monitor = ConsoleTaskMonitor()
    for func in funcs: 
        if func.getName() == function_name:
            print(function_name)
            func_cfg = create_cfg_function(current_program, func, monitor)
            
            #cfg = func_cfg
            #monitor = m

def create_cfg_function( cu_program, function, mon):
    # create cfg for a single function
    #print("address in cdg")
    breakpoint()
    block_model_iterator = BasicBlockModel(cu_program)
    function_addresses = function.getBody()
    code_blocks_iterator = block_model_iterator.getCodeBlocksContaining(function_addresses, mon)
    cfg = DirectedSparseGraph()
    while (code_blocks_iterator.hasNext()):
        
        block = code_blocks_iterator.next()
        addr = hex(block.getFirstStartAddress().getOffset())
        #print(addr)
        v = Vertex(block)
        cfg.addVertex(v)
        dstBlocks = block.getDestinations(mon)
        srcBlocks = block.getSources(mon)
        while(srcBlocks.hasNext()):
            source = srcBlocks.next()
            vsrc = Vertex(source)
            cfg.addVertex(vsrc)
            edge1 = Edge(vsrc, v)
            res = cfg.addEdge(edge1, vsrc, v )
            src_addr = hex(source.getSourceAddress().getOffset())
            #print(src_addr)
            
        while (dstBlocks.hasNext()):
            destination = dstBlocks.next()
            des_addr = hex(destination.getDestinationAddress().getOffset())
            vdes = Vertex(destination)
            cfg.addVertex(vdes)
            edge2 = Edge(v, vdes)
            cfg.addEdge(edge2, v, vdes)
            #print(des_addr)
    #breakpoint()
    return cfg


if __name__ == "__main__":

    args = getScriptArgs()
    if args:
        function_name = args[0]
        breakpoint()
        create_cfg(function_name)
    
        
