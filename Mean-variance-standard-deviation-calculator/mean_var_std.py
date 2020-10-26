import numpy as np

def calculate (inp):
    if len(inp)!=9:
        raise ValueError("List must contain nine numbers.")
    output={}
    inp_np = np.array(inp)
    inp_np = inp_np.reshape((3,3))
    output['mean']=[list(inp_np.mean(axis=0)),list(inp_np.mean(axis=1)),inp_np.mean()]
    output['variance']=[list(inp_np.var(axis=0)),list(inp_np.var(axis=1)),inp_np.var()]
    output['standard deviation']=[list(inp_np.std(axis=0)),list(inp_np.std(axis=1)),inp_np.std()]
    output['max']=[list(inp_np.max(axis=0)),list(inp_np.max(axis=1)),inp_np.max()]
    output['min']=[list(inp_np.min(axis=0)),list(inp_np.min(axis=1)),inp_np.min()]
    output['sum']=[list(inp_np.sum(axis=0)),list(inp_np.sum(axis=1)),inp_np.sum()]
    
    return output